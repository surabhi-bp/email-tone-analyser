# Email Tone Analyzer

A simple web app that analyzes the tone of emails using **Python**, **Flask**, and **TextBlob**.

---

## 📂 Project Structure

```
EMAIL-TONE-ANALYZER/
│
├── app.py # Main Flask application
├── templates/ # HTML templates
│ ├── index.html # Input page for email text
│ ├── result.html # Displays tone result
├── static/
│ ├── style.css # Custom CSS styling
└── venv/ # Virtual environment (optional)
```


## ⚡ Features
- Analyze email tone: Polite, Rude, or Neutral
- Uses **TextBlob** for sentiment analysis
- Clean and simple web interface
- Displays analyzed tone with emojis for easy understanding


## 🛠 Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS  
- **Libraries:** TextBlob



## 🚀 How to Run

1. **Clone the repository**

git clone https://github.com/surabhi-bp/email-tone-analyser.git
cd email-tone-analyser
Create and activate virtual environment

2. **Create and activate virtual environment**
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/Mac
Install dependencies

3. **Install dependencies**
pip install textblob flask
Run the Flask app

4. **Run the Flask app**
python app.py

5. **Open your browser at http://127.0.0.1:5000/ and start analyzing emails!**

**💡 Usage**
Enter your email text on the homepage
Click Analyze
View the tone result (Polite 😊, Rude 😠, Neutral 😐) on the result page

📸 Screenshots
![Screenshot 2025-10-08 195048](https://github.com/user-attachments/assets/d24a797b-7068-4238-a460-121ff999062f)
![Email Tone Analyzer Screenshot 2](https://github.com/user-attachments/assets/9ce3ea5c-b647-4e11-8efe-4a356906c669)


