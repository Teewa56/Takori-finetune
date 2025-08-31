# Tokari Core Finetune – Nigerian Student AI Helper

This project is an AI-powered assistant designed to help Nigerian university students (starting with FUTA) understand academic topics, student life, and more. It uses prompt engineering and curated Q&A data to provide detailed, relevant answers.

---

## Features

- **Ask questions** about FUTA academics, grading, student life, entrepreneurship, and more.
- **Detailed, localized answers** using examples and data from Nigerian universities.
- **Modern web frontend** (HTML + Tailwind CSS).
- **Backend API** (Flask) connects to the Tokari Core GPT-3.5 API.
- **Easy to extend** with more Q&A data.

---

## Project Structure

```
tokari-core-finetune/
│
├── backend/
│   ├── main.py            # Flask backend API
│   └── requirements.txt   # Python dependencies
│
├── src/
│   ├── index.html         # Frontend UI
│   └── main.js            # Frontend JS logic
│
├── ai-model/
│   └── finetune.py        # Prompt builder using Q&A data
│
└── data/
    ├── qa_data.jsonl
    ├── academic_info.jsonl
    ├── business_docs.jsonl
    └── schooldata.jsonl
```

---

## How It Works

1. **Frontend** collects user questions and sends them to the backend.
2. **Backend** builds a prompt using relevant Q&A pairs from the data files.
3. **Backend** sends the prompt to the Tokari Core API and returns the AI’s answer.
4. **Frontend** displays the answer to the user.

---

## Local Development

### 1. Install Python dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the backend server

```bash
python main.py
```

### 3. Serve the frontend

```bash
cd ../src
python -m http.server 8000
```
Visit [http://localhost:8000/index.html](http://localhost:8000/index.html) in your browser.

---

## Deployment

- **Backend:** Deploy `backend/` to Render, Railway, Heroku, etc. Set your `API_KEY` as an environment variable.
- **Frontend:** Deploy `src/` to Netlify, Vercel, or GitHub Pages. Update `main.js` to use your backend’s deployed URL.

---

## Data

- Q&A pairs are stored in `.jsonl` files in the `data/` folder.
- To add more knowledge, extract Q&A from `.txt` files or other sources and append to these files.

---

## License

MIT

---

## Credits
- Tokari core [TOKARI](https://tokari-core.vercel.app/sign-in)
- Built with [Flask](https://flask.palletsprojects.com/),