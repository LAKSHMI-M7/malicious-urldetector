import streamlit as st
import pickle
import sklearn

# Load the model and vectorizer
model = pickle.load(open("malicious_url_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Streamlit App UI
st.title("🔐 Malicious URL Detector")
url_input = st.text_input("Enter a URL to check if it's malicious:")

if url_input:
    vector = tfidf.transform([url_input]).toarray()
    prediction = model.predict(vector)[0]
    if prediction == "malicious":
        st.error("🚨 This URL is MALICIOUS!")
    else:
        st.success("✅ This URL looks SAFE.")
