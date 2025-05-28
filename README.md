# EduLocal AI Hackathon MVP

## Struktur
- `src/`
  - `config.py` → API keys & endpoints
  - `translator.py` → Azure Translator & detect_language
  - `chat_engine.py` → multilingual ChatterBot logic
  - `admin.py` → `/admin/train` retraining endpoint
  - `bot.py` → `/whatsapp` webhook for Twilio
- `data/` → SQLite DB (auto-created)
- `requirements.txt`
- `test_chat.py` → quick CLI test
- `README.md`

## Setup Lokal

1. Buat & aktifkan venv:
    ```bash
    python -m venv .venv
    . .venv/Scripts/Activate.ps1   # PowerShell
    ```
2. Install deps:
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```
3. Isi `src/config.py` dengan kredensialmu.
4. Buat folder `data/`: `mkdir data`

## Run & Test

1. Jalankan server:
    ```bash
    uvicorn src.bot:app --reload --host 0.0.0.0 --port 8000
    ```
2. Expose via ngrok:
    ```bash
    ngrok http 8000
    ```
3. Update Twilio Sandbox webhook → `https://<ngrok-id>.ngrok-free.app/whatsapp`
4. Join Sandbox di WhatsApp:  
   `join <sandbox-name>` → +1 415 523 8886
5. Chat:
   - “What is AI?” → English reply  
   - “Apa itu AI?” → Indonesian reply

## Admin API

Retrain on the fly:

```bash
curl -X POST http://localhost:8000/admin/train \
  -H "Content-Type: application/json" \
  -d '[["Pertanyaan","Jawaban"],["...","..."]]'
