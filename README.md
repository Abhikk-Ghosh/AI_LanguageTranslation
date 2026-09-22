# 🌐 LinguaAI - Language Translation Tool

An AI-powered multilingual language translation web application developed as part of the **CodeAlpha Artificial Intelligence Internship**.

LinguaAI provides a simple and responsive interface for translating text between multiple languages using a REST-based translation service.

---

## 🚀 Features

- 🌍 Multilingual text translation
- 🔄 Swap source and target languages
- 📝 Input text with character counter
- 📋 Copy translated text to clipboard
- 🗑️ Clear input and output
- ⌨️ `Ctrl + Enter` keyboard shortcut for translation
- ⚡ Real-time translation through REST API
- 📱 Responsive web interface
- 🔐 Backend API with input validation
- 🧪 Automated unit tests
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
- REST API

### Translation Service

- MyMemory Translation API

### Testing

- Pytest

---

## 📁 Project Structure
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
│   │
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_translator.py


How It Works:-
The application follows a simple client-server architecture:


User
 │
 ▼
Web Interface
 │
 ▼
JavaScript
 │
 │ POST /api/translate
 ▼
Flask Backend
 │
 ▼
TranslationService
 │
 ▼
MyMemory Translation API
 │
 ▼
Translated Text
 │
 ▼
Web Interface
---

## 🌐 Supported Languages

The current interface supports:

- English
- Hindi
- Bengali
- French
- German
- Spanish
- Italian
- Portuguese
- Russian
- Japanese
- Korean
- Arabic
- Chinese

---

## 💻 Installation

### 1. Clone the Repository

bash
git clone https://github.com/Abhikk-Ghosh/AI_LanguageTranslation.git
 
 Open the Project Directory
cd AI_LanguageTranslation


📌 Project Highlights

This project demonstrates practical implementation of:

REST API integration
Flask backend development
Frontend-backend communication
External API consumption
Modular Python architecture
Error handling
Input validation
Automated testing
Responsive UI development


Yesterday 7:47 PM

Absolutely. Here is the complete README.md in one block. Delete everything currently in your GitHub README editor and paste only this.

# 🌐 LinguaAI - Language Translation Tool

An AI-powered multilingual language translation web application developed as part of the **CodeAlpha Artificial Intelligence Internship – Task 1**.

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
- Python `requests`

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
│   │
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_translator.py
⚙️ How It Works

LinguaAI follows a client-server architecture.

User
  │
  ▼
Web Interface
  │
  ▼
JavaScript
  │
  │ POST /api/translate
  ▼
Flask Backend
  │
  ▼
TranslationService
  │
  ▼
MyMemory Translation API
  │
  ▼
Translated Text
  │
  ▼
Web Interface
Translation Flow
The user enters text into the web interface.
The user selects the source language.
The user selects the target language.
JavaScript sends the translation request to the Flask backend.
Flask validates the request.
TranslationService sends the request to the MyMemory Translation API.
The API returns the translated text.
The Flask backend returns the result as JSON.
JavaScript displays the translated text on the webpage.
🌐 Supported Languages

The current interface supports:

🇬🇧 English
🇮🇳 Hindi
🇮🇳 Bengali
🇫🇷 French
🇩🇪 German
🇪🇸 Spanish
🇮🇹 Italian
🇵🇹 Portuguese
🇷🇺 Russian
🇯🇵 Japanese
🇰🇷 Korean
🇸🇦 Arabic
🇨🇳 Chinese
🔌 API Endpoint
Translate Text
POST /api/translate
Request
{
    "text": "Hello, how are you?",
    "source": "en",
    "target": "hi"
}
Successful Response
{
    "success": true,
    "translation": "हैलो, आप कैसे हैं?"
}
Error Response
{
    "success": false,
    "error": "Please enter text to translate."
}
💻 Installation
1. Clone the Repository
git clone https://github.com/Abhikk-Ghosh/AI_LanguageTranslation.git
2. Open the Project Directory
cd AI_LanguageTranslation
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
5. Install Dependencies
pip install -r requirements.txt
6. Run the Application
python app.py
7. Open the Application

Open the following address in your browser:

http://127.0.0.1:5000
📦 Dependencies

The project uses the following Python packages:

Flask==3.1.3
flask-cors==6.0.5
requests==2.31.0

Install them using:

pip install -r requirements.txt
🧪 Testing

The project includes automated tests for the translation service.

Run the test suite using:

python -m pytest tests
Tests Included

The current test suite checks:

Same-language translation
English-to-Hindi translation
Empty text validation
Missing language validation

Expected result:

4 passed
🔒 Input Validation

The application performs validation at the backend level.

It checks for:

Empty text
Missing source language
Missing target language
Invalid translation API responses
Failed external API requests

The frontend also validates empty input before sending a request to the backend.

🔄 Language Swap

The application provides a language swap feature that allows users to quickly exchange:

Source Language ↔ Target Language

The input and translated output are also exchanged when the swap function is used.

📋 Copy Translation

Users can copy the translated result directly to their clipboard using the:

📋 Copy Translation

button.

⌨️ Keyboard Shortcut

Users can press:

Ctrl + Enter

inside the input text area to start translation.

📱 Responsive Design

The interface is designed to work across different screen sizes.

The layout automatically adapts for:

Desktop
Laptop
Tablet
Mobile devices
🏗️ Architecture

The project separates the application into different layers.

Frontend Layer

Responsible for:

User interface
Language selection
Text input
Displaying translation results
User interactions

Files:

templates/index.html
static/css/style.css
static/js/script.js
Backend Layer

Responsible for:

HTTP requests
API routing
Input validation
Error handling
Returning JSON responses

File:

app.py
Service Layer

Responsible for:

Communication with the external translation API
Translation request processing
Translation response handling

File:

services/translator.py
Testing Layer

Responsible for:

Testing translation logic
Testing validation
Checking expected behavior

File:

tests/test_translator.py
📊 Example
Input
Hello, how are you?
Source Language
English
Target Language
Hindi
Output
हैलो, आप कैसे हैं?
🔮 Future Improvements

The following features can be added in future versions:

🎙️ Speech-to-text input
🔊 Text-to-speech output
🤖 Automatic language detection
📚 Translation history
🌙 Light/Dark theme switching
📊 Translation usage analytics
🔐 User authentication
☁️ Cloud deployment
📱 Progressive Web App support
🧠 Integration with advanced translation models
🎯 Learning Outcomes

This project demonstrates practical experience with:

Python development
Flask web development
REST API integration
Frontend-backend communication
External API consumption
JSON data handling
Error handling
Input validation
Modular application design
Automated testing
Responsive web development
👨‍💻 Author

Abhik Ghosh

B.Tech CSE (AIML)
Adamas University, Kolkata

💼 Resume Project Description

LinguaAI – AI-Powered Language Translation Tool

Developed a multilingual language translation web application using Python, Flask, JavaScript, and REST APIs, integrating the MyMemory Translation API for real-time translation. Implemented modular service architecture, input validation, error handling, responsive UI, language swapping, clipboard functionality, and automated unit testing using Pytest.

📄 Internship

This project was developed as:

CodeAlpha Artificial Intelligence Internship – Task 1: Language Translation Tool

The project demonstrates practical implementation of an API-based language translation system with a web-based user interface.

⭐ Acknowledgement

Developed for educational and internship purposes as part of the CodeAlpha Artificial Intelligence Internship.


After pasting everything, use this commit message:

```text
Add professional project documentation

Then click Commit changes.

its required ??🔌 API Endpoint

Translate Text

No, it is not strictly required for the CodeAlpha Task 1. The task mainly requires the translation interface, source/target languages, sending text to a translation API, and displaying the translated result.

However, I recommend keeping the “API Endpoint” section in the README because your project actually has a Flask endpoint:

POST /api/translate

It makes the project look more professional and shows how your frontend communicates with the backend.

If you want the README shorter and cleaner, you can remove the entire:

## 🔌 API Endpoint
### Translate Text
...

section without affecting the project itself.

My recommendation: Keep it. It is documentation, not an extra project requirement.

i just pasted # 🌐 LinguaAI - Language Translation Tool

An AI-powered multilingual language translation web application developed as part of the **CodeAlpha Artificial Intelligence Internship**.

LinguaAI provides a simple and responsive interface for translating text between multiple languages using a REST-based translation service.

---

## 🚀 Features

- 🌍 Multilingual text translation
- 🔄 Swap source and target languages
- 📝 Input text with character counter
- 📋 Copy translated text to clipboard
- 🗑️ Clear input and output
- ⌨️ Ctrl + Enter keyboard shortcut for translation
- ⚡ Real-time translation through REST API
- 📱 Responsive web interface
- 🔐 Backend API with input validation
- 🧪 Automated unit tests
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
- REST API

### Translation Service

- MyMemory Translation API

### Testing

- Pytest

---

## 📁 Project Structure



text
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
│   │
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_translator.py


How It Works:-

    The application follows a simple client-server architecture:


User
 │
 ▼
Web Interface
 │
 ▼
JavaScript
 │
 │ POST /api/translate
 ▼
Flask Backend
 │
 ▼
TranslationService
 │
 ▼
MyMemory Translation API
 │
 ▼
Translated Text
 │
 ▼
Web Interface

Yes 👍 What you pasted is good so far. But there is one small issue: your README currently stops inside the “How It Works” section.

You should continue it with the remaining sections so the README looks complete and professional.

Paste this directly after:

Web Interface
---

## 🌐 Supported Languages

The current interface supports:

- English
- Hindi
- Bengali
- French
- German
- Spanish
- Italian
- Portuguese
- Russian
- Japanese
- Korean
- Arabic
- Chinese

---

## 💻 Installation

### 1. Clone the Repository

``bash
git clone https://github.com/Abhikk-Ghosh/AI_LanguageTranslation.git
2. Open the Project Directory
cd AI_LanguageTranslation
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
5. Install Dependencies
pip install -r requirements.txt
6. Run the Application
python app.py
7. Open in Browser
http://127.0.0.1:5000
🧪 Testing

The project includes automated tests for the translation service.

Run:

python -m pytest tests

The test suite covers:

Same-language translation
English-to-Hindi translation
Empty text validation
Missing language validation

Expected result:

4 passed
🔒 Input Validation

The backend validates:

Empty translation requests
Missing source language
Missing target language
Invalid translation service responses

The frontend also performs basic input validation before sending requests.

📱 Responsive Design

The interface is designed to work across:

Desktop
Laptop
Tablet
Mobile devices
📌 Project Highlights

This project demonstrates practical implementation of:

REST API integration
Flask backend development
Frontend-backend communication
External API consumption
Modular Python architecture
Error handling
Input validation
Automated testing
Responsive UI development

Future Improvements

Possible future enhancements include:

Speech-to-text input
🔊 Text-to-speech output
🤖 Automatic language detection
📚 Translation history
🌙 Light/Dark theme switching
📊 Translation usage analytics
🔐 User authentication
☁️ Cloud deployment
