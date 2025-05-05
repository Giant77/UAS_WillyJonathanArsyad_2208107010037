# 📝 Intelligent Email Writer for Students

Proyek ini merupakan aplikasi berbasis Web yang memungkinkan mahasiswa membuat email secara otomatis dan profesional dengan bantuan teknologi Large Language Model (LLM) dari **Gemini API**.

---

## 📦 Fitur Utama

-   Memilih kategori email: Akademik, Skripsi, Magang, dll.
-   Menentukan nada (tone) penulisan: formal, netral, atau santai.
-   Mendukung Bahasa Indonesia dan Inggris.
-   Mengisi poin-poin utama yang ingin disampaikan dalam email.
-   Menghasilkan email yang profesional, jelas, dan padat secara otomatis.

---

## 📁 Struktur Proyek

```
root
├── .env.example            # Contoh file API key Gemini
├── app.py                  # Frontend dengan Streamlit
├── backend/
│   └── main.py             # Backend API menggunakan FastAPI
├── requirements.txt        # Dependensi backend

```

---

## ⚙️ Instalasi dan Menjalankan Proyek

### 1. Clone repository & setup local environment

-   Clone repository

```bash
git clone https://github.com/Giant77/UAS_WillyJonathanArsyad_2208107010037.git
cd UAS_WillyJonathanArsyad_2208107010037
```

-   Setup local environment
    Copy file env.example. Kemudian masukkan API key anda

```bash
cp .env.example .env
```

### 2. Setup dan jalankan Backend (FastAPI)

-   Buat dan aktifkan environment

```bash
python3 -m venv env       # Aktivasi venv
source env/bin/activate   # Linux/macOS
env\Scripts\activate      # Windows
```

-   install library yang dibutuhkan

```bash
# Install dependencies
pip install -r requirements.txt
```

-   Jalankan server
    note: pastikan anda masih berada pada root project

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Setup dan jalankan Frontend (Streamlit)

-   Buka terminal baru:
    note: Pastikan sudah berada di direktori project

```bash
streamlit run app.py
```

---

## 🔐 Konfigurasi API Key Gemini

1. Buka [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Klik **Create API Key**.
3. Copy API key dan simpan ke dalam file `.env` di root project dengan format:

```env
GEMINI_API_KEY=YourSecretGeminiAPIKey
```

---

## 📬 Contoh Penggunaan

1. Pilih kategori dan gaya penulisan email.
2. Masukkan informasi penerima, subjek, dan poin-poin penting.
3. Klik tombol **"Buat Email"**.
4. Email hasil generate akan ditampilkan di halaman aplikasi.
