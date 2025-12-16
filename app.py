import fitz  # PyMuPDF
from flask import Flask, render_template, request, jsonify
from wordfreq import zipf_frequency
import re

app = Flask(__name__)

# --- CONFIGURATION ---
# Zipf scale is 0-8. 
# 'the' is ~7.5. 'algorithm' is ~5. 'defenestration' is ~1.
# We consider anything below 4.0 to be "rare/difficult".
DIFFICULTY_THRESHOLD = 4.0 

def pdf_to_html(pdf_path):
    """Converts a PDF to simple HTML to preserve structure."""
    doc = fitz.open(pdf_path)
    html_content = ""
    for page in doc:
        html_content += page.get_text("html")
    return html_content

def extract_difficult_terms(text_html):
    """
    Scans the text, cleans it, and finds words with low frequency.
    Returns a list of unique strings.
    """
    # 1. Strip HTML tags to get raw text for analysis
    clean_text = re.sub('<[^<]+?>', ' ', text_html)
    
    # 2. Tokenize (simple split by non-letters)
    words = re.findall(r'\b[a-z]{3,}\b', clean_text.lower())
    
    # 3. Filter by difficulty
    difficult_words = set()
    for word in words:
        freq = zipf_frequency(word, 'en')
        if freq > 0 and freq < DIFFICULTY_THRESHOLD:
            difficult_words.add(word)
            
    return list(difficult_words)

@app.route('/')
def home():
    # In a real app, you might allow file uploads. 
    # For this assignment, we load a local 'sample.pdf'.
    try:
        # 1. Convert PDF to HTML
        html_content = pdf_to_html("sample.pdf")
        
        # 2. Analyze text for difficult terms
        difficult_terms = extract_difficult_terms(html_content)
        
    except Exception as e:
        html_content = f"<h3>Error: Could not load sample.pdf</h3><p>{e}</p>"
        difficult_terms = []

    # 3. Render the frontend, passing the data
    return render_template(
        'reader.html', 
        content=html_content, 
        terms=difficult_terms
    )

if __name__ == '__main__':
    # host='0.0.0.0' allows external access in Codespaces
    app.run(host='0.0.0.0', port=5000, debug=True)