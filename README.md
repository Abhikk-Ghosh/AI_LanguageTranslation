# 🌐 LinguaAI - Language Translation Tool

##  Live Demo

🌐 **Live Application:** https://ai-languagetranslation.onrender.com

An AI-powered multilingual language translation web application
LinguaAI provides a clean and responsive web interface for translating text between multiple languages using a Flask backend and the MyMemory Translation API.

---

## 🚀 Features

- 🌍 Multilingual text translation
- 🔄 Source and target language swapping
- 📝 Text input with character counter
- 📋 Copy translated text to clipboard
- 🗑️ Clear input and output
- ⌨️ `Ctrl + Enter` keyboard shortcut for translation
- ⚡ REST API-based translation
- 📱 Responsive web interface
- 🔐 Backend input validation
- ⚠️ Error handling for failed requests
- 🧪 Automated unit testing
- 🏗️ Modular service-based architecture

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask
- Flask-CORS

### Translation Service

- MyMemory Translation API
- Python Requests

### Testing

- Pytest

---

## 📁 Project Structure

```text
AI_LanguageTranslation/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── services/
│   ├── __init__.py
│   └── translator.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_translator.py
