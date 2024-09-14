# import libraries
import streamlit as st
from streamlit_lottie import st_lottie
import json
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="💹",
)

st.title("Deposit Decision Predictor")

# Load data
df = pd.read_csv(r"datasets\cleaned_data.csv")


# sidebar
st.sidebar.header("Deposit Decision Predictor")
st.sidebar.image("images_animations\home.jpeg")
st.sidebar.markdown(
    "Made By : [Ahmed Fawzy](https://www.linkedin.com/in/ahmedfawzy-ko/)"
)

# Body

# Animation upload and open
with open(r"images_animations\animation.json") as source:
    animation = json.load(source)
st_lottie(animation)

# About Data section
st.title("Bank Marketing Dataset Overview")

# Dataset Overview
st.header("Dataset Overview")
st.write(
    """
- The dataset comes from the UCI Machine Learning Repository and contains information on direct marketing campaigns by a Portuguese banking institution.
"""
)

# Main Objective
st.header("Main Objective")
st.write(
    """
- Predict the outcome (yes or no) of whether a customer will subscribe to a term deposit.
"""
)

# Features
st.header("Features")

st.subheader("Client Information")
st.write(
    """
- **age**: Age of the client (numeric).
- **job**: Type of job (categorical: admin., blue-collar, entrepreneur, etc.).
- **marital**: Marital status (categorical: single, married, divorced).
- **education**: Education level (categorical: primary, secondary, tertiary, unknown).
- **default**: Has credit in default? (categorical: yes, no).
- **housing**: Has a housing loan? (categorical: yes, no).
- **loan**: Has a personal loan? (categorical: yes, no).
"""
)

st.subheader("Contact Information")
st.write(
    """
- **contact**: Contact communication type (categorical: cellular, telephone).
- **month**: Last contact month of year (categorical: jan, feb, mar, ..., dec).
- **day_of_week**: Last contact day of the week (categorical: mon, tue, wed, thu, fri).
- **duration**: Last contact duration in seconds (numeric).
"""
)

st.subheader("Campaign Information")
st.write(
    """
- **campaign**: Number of contacts performed during this campaign (numeric).
- **pdays**: Days since the client was last contacted from a previous campaign (numeric; 999 indicates not previously contacted).
- **previous**: Number of contacts performed before this campaign (numeric).
- **poutcome**: Outcome of the previous marketing campaign (categorical: failure, nonexistent, success).
"""
)

st.subheader("Economic Context")
st.write(
    """
- **emp.var.rate**: Employment variation rate (numeric).
- **cons.price.idx**: Consumer price index (numeric).
- **cons.conf.idx**: Consumer confidence index (numeric).
- **euribor3m**: Euribor 3-month rate (numeric).
- **nr.employed**: Number of employees (numeric).
"""
)

# Target Variable
st.header("Target Variable")
st.write(
    """
- **y**: Indicates if the client subscribed to a term deposit (binary: yes or no).
"""
)


btn = st.button("Show a random sample from the final dataset")
if btn:
    st.write(df.sample(5))
