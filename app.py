import fitz  # PyMuPDF
from flask import Flask, render_template, jsonify, send_file
from wordfreq import zipf_frequency
import re
import os
import requests

app = Flask(__name__)

# --- CONFIGURATION ---
# Zipf scale is 0-8.
# 'the' is ~7.5. 'algorithm' is ~5. 'defenestration' is ~1.
# We consider anything below 4.0 to be "rare/difficult".
DIFFICULTY_THRESHOLD = 4.0

# Load your API key from the environment (set with `export GEMINI_API_KEY=...`)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")


def extract_difficult_terms(text):
    """
    Scans plain text and finds words with low Zipf frequency.
    Returns a list of unique strings.
    """
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())

    difficult_words = set()
    for word in words:
        freq = zipf_frequency(word, 'en')
        if freq > 0 and freq < DIFFICULTY_THRESHOLD:
            difficult_words.add(word)

    return list(difficult_words)


@app.route('/pdf')
def serve_pdf():
    """Serves the raw PDF file so PDF.js can render it in the browser."""
    return send_file('sample.pdf', mimetype='application/pdf')


@app.route('/define/<word>')
def define(word):
    # =========================================================
    # YOUR TASK (1/2): Implement this route.
    #
    # Call the Gemini API to return a one-sentence definition
    # of `word`, then return it as JSON: {"definition": "..."}
    #
    # ENDPOINT:
    #   url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    #
    # REQUEST BODY (pass as the `json=` argument to requests.post):
    #   {"contents": [{"parts": [{"text": "<your prompt here>"}]}]}
    #
    # EXTRACTING THE RESPONSE TEXT:
    #   data = response.json()
    #   text = data["candidates"][0]["content"]["parts"][0]["text"]
    #
    # SUGGESTED PROMPT:
    #   f"Define the word '{word}' in exactly one plain sentence."
    # =========================================================

    return jsonify({"definition": "Not yet implemented."})


@app.route('/')
def home():
    # In a real app, you might allow file uploads.
    # For this assignment, we load a local 'sample.pdf'.
    try:
        doc = fitz.open('sample.pdf')
        full_text = ""
        for page in doc:
            full_text += page.get_text("text")
        difficult_terms = extract_difficult_terms(full_text)

    except Exception as e:
        print(f"Error reading sample.pdf: {e}")
        difficult_terms = []

    # Pass only the term list — PDF.js handles rendering in the browser
    return render_template('reader.html', terms=difficult_terms)


if __name__ == '__main__':
    # host='0.0.0.0' allows external access in Codespaces
    app.run(host='0.0.0.0', port=3000, debug=True)
