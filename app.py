import pickle
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Load the pre-trained model and vectorizer
model = pickle.load(open('STREAMLIT DEPLOYMENT\model.pkl', 'rb'))
vectorizer = CountVectorizer()

# Set the page title
st.title("AIRLINE SENTIMENT ANALYSIS")

# Get user input for sentiment analysis
user_input = st.text_input("Enter a sentence to analyze the sentiment")

# Get user input for churn prediction
user_input_churn = st.text_input("Enter a sentence to predict churn")

data = pd.read_csv("STREAMLIT DEPLOYMENT/Airline-Sentiment-2-w-AA.csv", encoding='latin-1')
# Fit the vectorizer on the data
vectorizer.fit(data['text'])

# Check if user input is provided for sentiment analysis
if user_input:
    # Predict the sentiment for user input
    user_input_vec = vectorizer.transform([user_input])
    sentiment = model.predict(user_input_vec)[0]

    # Display the sentiment prediction
    st.subheader("Sentiment Prediction")
    if sentiment == "positive":
        st.write("The sentiment of the input sentence is: Positive")
    elif sentiment == "negative":
        st.write("The sentiment of the input sentence is: Negative")
    else:
        st.write("The sentiment of the input sentence is: Neutral")

# Check if user input is provided for churn prediction
if user_input_churn:
    # Predict the churn for user input
    user_input_churn_vec = vectorizer.transform([user_input_churn])
    churn_prediction = model.predict(user_input_churn_vec)[0]

    # Display the churn prediction
    st.subheader("Churn Prediction")
    if churn_prediction == 1:
        st.write("The customer is predicted to churn.")
    else:
        st.write("The customer is predicted not to churn.")

# Submit button for the predicted sentiment and churn
if st.button("Submit"):
    # Perform further actions here
    st.write("Sentiment and Churn submitted!")