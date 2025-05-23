# 🤖 AI Interview Coach – Your Personal Job Interview Simulator

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green)](https://openai.com/)
[![Gemini](https://img.shields.io/badge/Gemini-API-yellow)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🎯 Overview

**AI Interview Coach** is a smart, interactive mock interview application that lets you practice technical, behavioral, and personality-based interviews powered by LLMs (OpenAI + Gemini).

💼 Target Audience: Developers, job seekers, career switchers  
🎓 Powered by GPT-4 / GPT-3.5 and Gemini for dual evaluation  
🧠 Judge LLM feedback on generated interview questions  
📋 Session summaries with question, answers, scoring and cost  
▶️ Demo: https://interviewpreparation-cncegpb8hua6bjg3.germanywestcentral-01.azurewebsites.net/  
or  
▶️ https://interviewpreparationcoach.streamlit.app/  

---

## 🚀 Features

### 🧪 Interview Modes
- **Mock Interview** – One-by-one interactive questioning
- **Q&A Mode** – Question + freeform answering
- **Personality Check** – Explore character, values, and motivation

### 🎛️ Configurable Interview Settings
- Role/Job Title (e.g. "Frontend Developer")
- Difficulty: Easy / Medium / Hard
- Topic focus: General / Tech / Soft Skills / Behavioral / Custom
- LLM Prompting style:
  - Few-shot learning
  - Chain-of-thought
  - Role-based persona
  - Self-reflection
  - Zero-shot baseline

### ⚙️ OpenAI Settings
- Choose model: GPT-4 / GPT-3.5
- Temperature
- Top-p
- Max Tokens
- Frequency & Presence Penalties

### 🧠 LLM-as-a-Judge
- Gemini (LLM 2) evaluates questions from GPT (LLM 1)
- JSON-structured scoring with:
  - Score (1–10)
  - Explanation
  - Improvement suggestion
- Criteria sets for Technical, Behavioral, and Personality modes

### 📊 Progress Tracking
- Visual “Question x of y” progress indicator
- Session token + cost tracking per response
- Display cost and total budget in footer

### 📋 End-of-Session Summary
- All questions + user answers
- Judge feedback per question
- Tokens used + cost breakdown
- Total session cost
- Optional: PDF or export (planned)

### 🖼️ Visual Interview Scene Generator (via DALL·E)
- Auto-generates interview scenes based on role + tone
- Friendly/strict tone visual immersion

---

## 🛡️ Security & Abuse Protection

- ✅ Input validation and prompt injection blocking
- ✅ Session token limits
- ✅ Cost thresholding (max tokens per session)
- 🔒 Optional: moderation layer via OpenAI

---

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourname/ai-interview-coach.git
cd ai-interview-coach
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup `.env` with API Keys
Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

> 💡 Get OpenAI key at: https://platform.openai.com/account/api-keys  
> 💡 Get Gemini key at: https://makersuite.google.com/app/apikey

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```bash
.
├── app.py                          # Main Streamlit App
├── prompts/                        # Prompt builders for different techniques
├── config/                             
│   └── settings.py                 # OpenAI API settings
├── logic/                          # LLM calling logic
│   ├── openai_client.py
│   ├── security.py                 # Validation checks
│   └── question_evaluator.py       # LLM as a judge, Question scoring
├── ui/                             # Streamlit UI components
│   ├── sidebar.py
│   ├── chat.py
│   ├── settings.py
│   ├── feedback.py
│   └── summary.py
├── utils/                          # Token tracking, validation
├── .env                            # API keys
├── requirements.txt
├── README.md
└── streamlit.sh                    # Start environment for Azure
```

---

## 📄 License

MIT License – free to use, modify, and share.

---

## 🙌 Credits

Built with ❤️ using Streamlit, OpenAI, Google Gemini, and a lot of good prompting.
