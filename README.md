# 🚀 Multi Agent Researcher & Report Generator

An AI-powered multi-agent system that automates the complete research workflow — from data collection to structured report generation and PDF export.

---

## 📌 Overview

This project simplifies research using an **agentic architecture**, where multiple specialized agents collaborate step-by-step to complete a task.

Instead of relying on a single AI model, the system breaks the workflow into smaller components handled by different agents — making the process modular, transparent, and efficient.

---

## 🔁 Agentic Workflow

User Input → Research Agent → Filter Agent → Summarizer Agent → Writer Agent → PDF + UI Output

---

## ⚙️ How It Works

1. **User Input**
   The user enters a topic for research.

2. **Agent Workflow**
   🔍 Research Agent → Collects data from Wikipedia & web sources
   🧹 Filter Agent → Cleans and processes raw data
   🧠 Summarizer → Extracts key insights
   📄 Writer Agent → Generates structured report
   📥 PDF Generator → Converts report into downloadable PDF

3. **Output**

   * Displays structured report
   * Provides downloadable PDF
   * Stores history of previous searches

---

## ✨ Features

* Multi-agent architecture
* Real-time agent execution visualization
* Automated research → filtering → reporting pipeline
* PDF report generation
* Memory-based history tracking
* Interactive Streamlit UI
* Deployed and accessible online

---

## 🛠 Tech Stack

* Python
* Streamlit
* APIs (Wikipedia / Web search)
* FPDF

---

## 📂 Project Structure

My_Agent_Project/
│
├── agents/
│   ├── research.py
│   ├── filter.py
│   ├── writer.py
│   ├── summarizer.py
│
├── utils/
│   └── memory.py
│
├── app.py
├── main.py
├── requirements.txt
└── outputs/

---

## 🚀 Installation & Setup

1. Clone the repository
   git clone https://github.com/udaykiran-707/Agentic-AI-project.git
   cd  Agentic-AI-project  

2. Create virtual environment
   python -m venv venv

3. Activate environment
   venv\Scripts\activate

4. Install dependencies
   pip install -r requirements.txt

5. Run the app
   streamlit run app.py

---

## 🌐 Live Demo

👉 https://agentic-multi-agents.streamlit.app/

---

## 💻 GitHub Repository

👉 https://github.com/udaykiran-707/Agentic-AI-project

---

## 🎯 What I Learned

* Designing multi-agent workflows
* Breaking complex systems into modular components
* Building real-world AI applications
* Deploying applications

---

## 🔮 Future Improvements

* Add advanced AI/LLM summarization
* Improve UI/UX with animations
* Add database for persistent storage
* Integrate more data sources

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Streamlit
* Python community
* Open-source contributors

---

## 📬 Contact

Feel free to connect for feedback or collaboration.

---

⭐ If you like this project, give it a star!
