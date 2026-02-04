🚀 Gemini RAG Chatbot
Team: Team-Kernel
An intelligent chatbot using Google's Gemini API and ChromaDB for Retrieval-Augmented Generation.

## 👥 Team Details
| Name | Role | Email |
|------|------|-------|
| Sandeep | Team Lead | sandeepprajapati1202@gmail.com |

## 🎯 Problem Statement
Users need quick access to knowledge bases (Operating Systems, History, etc.) without manually searching through documentation.

**Context:** Traditional chatbots lack context-aware responses and require frequent retraining with new information. Students and learners struggle to get accurate, sourced answers.

**Impact:** Students, professionals, and researchers who need reliable, context-aware information from specific domains.

## 💡 Solution
A Retrieval-Augmented Generation (RAG) chatbot that combines Google's Gemini API with ChromaDB vector database to deliver accurate, context-based responses.

- **RAG Architecture:** Retrieves relevant documents before generating responses for accuracy
- **Gemini Integration:** Leverages advanced language models for natural, coherent answers
- **Multi-Domain Support:** Easily extensible to different knowledge bases

## 🛠 Tech Stack
| Category | Technologies Used |
|----------|-------------------|
| Frontend | HTML5, CSS, JavaScript (Vanilla) |
| Backend | Python, Flask |
| AI/ML | Google Gemini API, ChromaDB |
| Database | ChromaDB (Vector Database) |
| Tools/APIs | Google Generative AI |

## 📊 MVP Features
- ✅ OS Bot: RAG-based chatbot for Operating Systems questions
- ✅ Web Interface: Flask-based UI with real-time chat
- 🔄 WW2 History Bot: Domain-specific knowledge base (In Progress)

## 🔗 Links & Demo
- 📂 **GitHub Repo:** https://github.com/GDGoC-GalgotiasUniversity/techsprint-2026-team-team-kernel

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/simplysandeepp/try-gemini.git
   cd try-gemini
   ```

2. **Create a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API Key:**
   - Get your Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Open `os_bot.py` and replace `GOOGLE_API_KEY` with your actual key

### Running the Application

**Web Interface (Flask):**
```bash
python app.py
```
Then open your browser and navigate to: `http://127.0.0.1:5000`

**Console Mode - OS Bot:**
```bash
python os_bot.py
```

**Console Mode - WW2 History Bot:**
```bash
python main.py
```

## 📁 Project Structure
```
Team-Kernel/
├── app.py              # Flask web application
├── os_bot.py           # Operating Systems RAG bot
├── main.py             # WW2 History bot
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Web interface
└── README.md           # Project documentation
```

### Testing Credentials
```
User: user@demo.com
Pass: hack2026
```

## 🏆 Acknowledgements
This project was developed during TechSprint Hackathon 2026, organized by GDG on Campus Galgotias University.
