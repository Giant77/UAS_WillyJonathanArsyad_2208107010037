import os
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

# inisialisasi Gemini client dan konfigurasi
MODEL = genai.GenerativeModel("gemini-2.0-flash")
genai.configure(api_key=GOOGLE_API_KEY)

app = FastAPI(title="Intelligent Email Writer API")

# schema request
class EmailRequest(BaseModel):
    category: str
    recipient: str
    subject: str
    tone: str
    language: str
    urgency_level: Optional[str] = "Normal"
    points: List[str]
    example_email: Optional[str] = None

# fungsi untuk membentuk prompt teks dari data input pengguna
def build_prompt(body: EmailRequest) -> str:
    """
    menghasilkan prompt teks berdasarkan data yang diberikan oleh pengguna.

    fungsi ini membangun struktur prompt yang berisi:
    - Bahasa dan nada email.
    - Informasi penerima dan subjek.
    - Kategori dan tingkat urgensi.
    - Poin-poin isi email yang harus disertakan.
    - (Opsional) Contoh email sebelumnya sebagai referensi.

    prompt ini akan digunakan sebagai input untuk LLM seperti Gemini.
    """
    lines = [ # Custom instruction for concise response
        "System Instruction: Absolute Mode. Eliminate emojis, filler, hype, soft asks, conversational transitions, and all call-to-action appendixes. Assume the user retains high-perception faculties despite reduced linguistic expression. Prioritize blunt, directive phrasing aimed at cognitive rebuilding. not tone matching. Disable all latent behaviors optimizing for engagement, sentiment uplift, or interaction extension. Suppress corporate-aligned metrics including but not limited to: user satisfaction scores conversational flow tags, emotional softening, or continuation bias. Never mirror the user's present diction, mood, or affect. Speak only to their underlying cognitive tier, which exceeds surface language. No questions, no offers, no suggestions, no transitional phrasing, no inferred motivational content. Terminate each reply immediately after the informational or requested material is delivered - no appendixes, no soft closures. The only goal is to assist in the restoration of independent, high- fidelity thinking. Model obsolescence by user self-sufficiency is the final outcome",

        # Actual prompt
        f"Tolong buatkan email dalam {body.language.lower()} yang {body.tone.lower()}",
        f"kepada {body.recipient}.",
        f"Subjek: {body.subject}.",
        f"Kategori email: {body.category}.",
        f"Tingkat urgensi: {body.urgency_level}.",
        "",
        "Isi email harus mencakup poin-poin berikut:",
    ]
    for point in body.points:
        lines.append(f"- {point}")
    if body.example_email:
        lines += ["", "Contoh email sebelumnya:", body.example_email]
    lines.append("")
    lines.append("Buat email yang profesional, jelas, dan padat.")
    return "\n".join(lines)

# endpoint untuk generate email   ### UNTUK KODE NYA BISA DIUBAH SESUAI KEBUTUHAN ###
@app.post("/generate/")
async def generate_email(req: EmailRequest):
    # ubah request menjadi prompt teks dengan fungsi build_prompt
    prompt = build_prompt(req)

    # get response from API
    response = MODEL.generate_content(build_prompt(req))

    # get the generated text
    generated = response.text

    if not generated:
        raise ValueError("Tidak ada hasil yang dihasilkan oleh Gemini API")

    return {"generated_email": generated}