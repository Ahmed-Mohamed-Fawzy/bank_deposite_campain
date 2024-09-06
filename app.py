
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Title
st.title('Deposit Prediction\n')

# Image
st.image('images.jpeg', width=500)

# Load Cleaned Data
df = pd.read_csv('cleaned_data.csv')

# Load preprocessor
preprocessor_full = pickle.load(open('preprocessor.pkl', 'rb'))

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Input Data
job = st.selectbox('job', df['job'].unique())
marital = st.selectbox('marital', df['marital'].unique())
education = st.selectbox('education', df['education'].unique())
housing = st.selectbox('housing', df['housing'].unique())
loan = st.selectbox('loan', df['loan'].unique())
contact = st.selectbox('contact', df['contact'].unique())
month = st.selectbox('month', df['month'].unique())
day_of_week = st.selectbox('day_of_week', df['day_of_week'].unique())
contacted_before = st.selectbox('contacted_before', df['contacted_before'].unique())


age = st.number_input('age', df.age.min(), df.age.max())
campaign = st.number_input('campaign', df.campaign.min(), df.campaign.max())
previous = st.number_input('previous', df.previous.min(), df.previous.max())
poutcome = st.number_input('poutcome', df.poutcome.min(), df.poutcome.max())
emp_var_rate = st.number_input('emp.var.rate', df['emp.var.rate'].min(), df['emp.var.rate'].max())
cons_price_idx = st.number_input('cons.price.idx', df['cons.price.idx'].min(), df['cons.price.idx'].max())
cons_conf_idx = st.number_input('cons.conf.idx', df['cons.conf.idx'].min(), df['cons.conf.idx'].max())
euribor3m = st.number_input('euribor3m', df['euribor3m'].min(), df['euribor3m'].max())
nr_employed = st.number_input('nr.employed', df['nr.employed'].min(), df['nr.employed'].max())

# Preprocessing
new_data = {'job':job,
            'marital':marital,
            'education':education,
            'housing':housing,
            'loan':loan,
            'contact':contact,
            'month':month,
            'day_of_week':day_of_week,
            'contacted_before':contacted_before,
            'age':age,
            'campaign':campaign,
            'previous':previous,
            'poutcome':poutcome,
            'emp.var.rate':emp_var_rate,
            'cons.price.idx':cons_price_idx,
            'cons.conf.idx':cons_conf_idx,
            'euribor3m':euribor3m,
            'nr.employed':nr_employed}

new_data = pd.DataFrame(new_data, index=[0])

# Preprocessing
new_data = preprocessor_full.transform(new_data)

# Prediction
predection = model.predict(new_data) 

if predection == 0:
    predection = 'No Deposit'
else:
    predection = 'Deposit'

# Output
if st.button('Predict'):
    st.markdown('# Deposit Prediction')
    st.markdown(predection)
