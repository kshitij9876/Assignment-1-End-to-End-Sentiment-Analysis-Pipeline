from flask import Flask, request, jsonify
import pickle
import re
from bs4 import BeautifulSoup

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and TF-IDF vectorizer
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)
with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = BeautifulSoup(text, "html.parser").get_text()  # Remove HTML tags
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

# Endpoint for predicting sentiment
@app.route("/predict", methods=["POST"])
def predict_sentiment():
    data = request.get_json()
    if "review_text" not in data:
        return jsonify({"error": "Field 'review_text' is missing."}), 400
    
    review_text = data["review_text"]
    cleaned_text = clean_text(review_text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)[0]
    sentiment = "positive" if prediction == 1 else "negative"
    
    return jsonify({"sentiment_prediction": sentiment})

# Run the app
app.run(debug=True)