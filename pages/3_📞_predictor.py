# import libraries
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
from streamlit_lottie import st_lottie
import json

st.set_page_config(
    page_title="Term Deposit Success Predictor",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊",
)

st.title("Term Deposit Success Predictor")

# Body

# Animation upload and open
with open("images_animations\prediction.json") as source:
    animation = json.load(source)
st_lottie(animation)

# sidebar

st.sidebar.header("Term Deposit Success Predictor")
st.sidebar.image("images_animations\prediction.jpeg")
st.sidebar.subheader("Choose Your Favorite Predictor")

# Filters
model = st.sidebar.selectbox(
    "predictors", ["Random Forest", "Gradient Boost", "XGBoost"]
)

# Load Cleaned Data
df = pd.read_csv("datasets\cleaned_data.csv")

# Load preprocessor
preprocessor = pkl.load(open("saved_models\preprocessor.pkl", "rb"))

# Load models
rf = pkl.load(open(r"saved_models\rf.pkl", "rb"))
gb = pkl.load(open("saved_models\gb.pkl", "rb"))
xgb = pkl.load(open(r"saved_models\xgb.pkl", "rb"))

# model selection
if model == "Random Forest":
    model = rf
elif model == "Gradient Boost":
    model = gb
elif model == "XGBoost":
    model = xgb

# Input Data

# Create two columns
col1, col2 = st.columns(2)

# First column inputs
with col1:
    job = st.selectbox("job", df["job"].unique())
    marital = st.selectbox("marital", df["marital"].unique())
    education = st.selectbox("education", df["education"].unique())
    housing = st.selectbox("housing", df["housing"].unique())
    loan = st.selectbox("loan", df["loan"].unique())
    contact = st.selectbox("contact", df["contact"].unique())
    month = st.selectbox("month", df["month"].unique())
    day_of_week = st.selectbox("day_of_week", df["day_of_week"].unique())
    contacted_before = st.selectbox("contacted_before", df["contacted_before"].unique())
    poutcome = st.selectbox("poutcome", df["poutcome"].unique())


# Second column inputs
with col2:
    age = st.number_input("age", df.age.min(), df.age.max())
    duration = st.number_input("duration", df.duration.min(), df.duration.max())
    campaign = st.number_input("campaign", df.campaign.min(), df.campaign.max())
    previous = st.number_input("previous", df.previous.min(), df.previous.max())
    emp_var_rate = st.number_input(
        "emp_var_rate", df["emp_var_rate"].min(), df["emp_var_rate"].max()
    )
    cons_price_idx = st.number_input(
        "cons_price_idx", df["cons_price_idx"].min(), df["cons_price_idx"].max()
    )
    cons_conf_idx = st.number_input(
        "cons_conf_idx", df["cons_conf_idx"].min(), df["cons_conf_idx"].max()
    )
    euribor3m = st.number_input(
        "euribor3m", df["euribor3m"].min(), df["euribor3m"].max()
    )
    nr_employed = st.number_input(
        "nr_employed", df["nr_employed"].min(), df["nr_employed"].max()
    )

# Preprocessing
new_data = {
    "job": job,
    "marital": marital,
    "education": education,
    "housing": housing,
    "loan": loan,
    "contact": contact,
    "month": month,
    "day_of_week": day_of_week,
    "contacted_before": contacted_before,
    "age": age,
    "duration": duration,
    "campaign": campaign,
    "previous": previous,
    "poutcome": poutcome,
    "emp_var_rate": emp_var_rate,
    "cons_price_idx": cons_price_idx,
    "cons_conf_idx": cons_conf_idx,
    "euribor3m": euribor3m,
    "nr_employed": nr_employed,
}

new_data = pd.DataFrame(new_data, index=[0])

# Preprocessing
new_data = preprocessor.transform(new_data)

# Prediction
predection = model.predict(new_data)

if predection == 0:
    predection = "NO"
else:
    predection = "YES"

# Output
if st.button("Predict"):
    st.markdown("# Deposit Prediction")
    st.markdown(predection)

f1_scores = [60.0, 60.0, 59.0]
recall_scores = [95.0, 94.0, 94.0]
precision_scores = [44.0, 44.0, 43.0]

fig = go.Figure(
    data=[
        go.Table(
            header=dict(
                values=[
                    "<b>Model<b>",
                    "<b>F1 Score<b>",
                    "<b>Recall<b>",
                    "<b>Precision<b>",
                ],
                line_color="darkslategray",
                fill_color="whitesmoke",
                align=["center", "center"],
                font=dict(color="black", size=18),
                height=40,
            ),
            cells=dict(
                values=[
                    ["<b>Random Forest<b>", "<b>Gradient Boost<b>", "<b>XG Boost<b>"],
                    [f1_scores[0], f1_scores[1], f1_scores[2]],
                    [recall_scores[0], recall_scores[1], recall_scores[2]],
                    [precision_scores[0], precision_scores[1], precision_scores[2]],
                ]
            ),
        )
    ]
)

fig.update_layout(title="Model Results On Test Data")
st.plotly_chart(fig, use_container_width=True)
