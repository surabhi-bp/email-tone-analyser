from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    email_text = request.form['email']
    blob = TextBlob(email_text)
    polarity = blob.sentiment.polarity

    if polarity > 0.3:
        tone = "Polite 😊"
    elif polarity < -0.3:
        tone = "Rude 😠"
    else:
        tone = "Neutral 😐"

    return render_template('result.html', tone=tone, email=email_text)

if __name__ == '__main__':
    app.run(debug=True)
