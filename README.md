# Augmented Reader — Assignment

This is a a Flask web app that reads a PDF, identifies rare vocabulary using word-frequency analysis, and highlights those words with interactive tooltips. Your job is to make those tooltips useful by connecting them to a the Gemini API.

---

## What You'll Build

Two small changes across two files:

1. **`app.py`** — implement the `/define/<word>` route to call an LLM API and return a definition as JSON
2. **`templates/reader.html`** — update the tooltip JavaScript to fetch from that route and display the result

Both locations are marked with `YOUR TASK` comments.

---

## Initial Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

You might have to use `pip3` instead of `pip` depending on your python environment

### 2. Add the sample PDF

Place a PDF named `sample.pdf` in the project root. Any PDF works — a Wikipedia article, a short paper, a textbook excerpt. The app will highlight rare words in whatever you put here.

### 3. Get a free API key

You need an API key for an LM service. 

**Option A — Google Gemini (recommended)**
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Sign in with your Google account 
3. Click **Get API key** → **Create API key** You might need to create a new project. 
4. Copy the key

The stub code in `app.py` is already written for the Gemini API (`gemini-1.5-flash`).


### 4. Set your API key as an environment variable

Run this in your terminal or powershell. 

**Mac / Linux / GitHub Codespaces terminal:**
```bash
export GEMINI_API_KEY="paste-your-key-here"
```

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="paste-your-key-here"
```

> **GitHub Codespaces:** You can also store the key as a Codespaces secret so you don't have to re-export it each session:
> Repository → Settings → Secrets and variables → Codespaces → New repository secret

### 5. Run the app

```bash
python app.py
```

You might need to use python3.

Then open [http://localhost:3000](http://localhost:3000) in your browser.

**GitHub Codespaces:** The Ports tab (bottom panel) will show port 3000 with a forwarded URL — click the globe icon to open it.

---

## Seeing Your Changes

Flask runs in **debug mode** by default (see `app.py` line 68), so it **automatically restarts** whenever you save a Python file. Just refresh your browser.

For changes to `templates/reader.html`, a browser refresh is all you need — no restart required.

---

## Project Structure

```
├── app.py               # Flask backend — YOUR TASK is in here
├── templates/
│   └── reader.html      # Frontend — YOUR TASK is in here too
├── requirements.txt
├── sample.pdf           # Add this yourself
└── README.md
```
