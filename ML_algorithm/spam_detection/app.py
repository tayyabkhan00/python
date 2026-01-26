import streamlit as st
import pickle
import re
import string

model = pickle.load(open("/Users/tayyabkhan/python/ML_algorithm/spam_detection/model/spam_model.pkl", "rb"))
tfidf = pickle.load(open("/Users/tayyabkhan/python/ML_algorithm/spam_detection/model/tfidf.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()

st.title("📧 Spam Detection System")

user_input = st.text_area("Enter a message")

if st.button("Predict"):
    cleaned = clean_text(user_input)
    vector = tfidf.transform([cleaned])
    prediction = model.predict(vector)

    if prediction[0] == 1:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Not Spam")
