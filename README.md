# Email Tone Analyzer

A simple web app that analyzes the tone of emails using **Python**, **Flask**, and **TextBlob**.

---

## 📂 Project Structure

EMAIL-TONE-ANALYZER/
│
├── app.py # Main Flask application
├── templates/ # HTML templates
│ ├── index.html # Input page for email text
│ ├── result.html # Displays tone result
├── static/
│ ├── style.css # Custom CSS styling
└── venv/ # Virtual environment (optional)

yaml
Copy code

---

## ⚡ Features
- Analyze email tone: Polite, Rude, or Neutral
- Uses **TextBlob** for sentiment analysis
- Clean and simple web interface
- Displays analyzed tone with emojis for easy understanding

---

## 🛠 Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS  
- **Libraries:** TextBlob

---

## 🚀 How to Run

1. **Clone the repository**
```bash
git clone https://github.com/surabhi-bp/email-tone-analyser.git
cd email-tone-analyser
Create and activate virtual environment

bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/Mac
Install dependencies

bash
Copy code
pip install textblob flask
Run the Flask app

bash
Copy code
python app.py
Open your browser at http://127.0.0.1:5000/ and start analyzing emails!

💡 Usage
Enter your email text on the homepage

Click Analyze

View the tone result (Polite 😊, Rude 😠, Neutral 😐) on the result page

📸 Screenshots
<img width="800" alt="Email Tone Analyzer Screenshot 1" src="https://github.com/user-attachments/assets/ff8d7415-14e6-4e52-8b2f-7930dcdf64ba" /> <img width="800" alt="Email Tone Analyzer Screenshot 2" src="https://github.com/user-attachments/assets/9ce3ea5c-b647-4e11-8efe-4a356906c669" />
