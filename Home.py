import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊",
)

st.sidebar.markdown(
    "Made By : [Ahmed Fawzy](https://www.linkedin.com/in/ahmedfawzy-ko/)"
)

# Load data
st.title("Bank Marketing Campaign Insights")
st.write("Exploring key insights from the bank marketing campaign data.")

# Image
st.image("image2.jpeg", width=750)

data = pd.read_csv("bank-additional-full.csv", sep=";")

# About Data section
st.header("About Data")
st.write(
    "The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed. "
)

# Display the dataset
st.subheader("Dataset Overview")
st.write(data.head())


# Display skewness and outlier analysis
st.subheader("Skewness and Outlier Analysis")

# Visualize skewness in age and duration
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.histplot(data["age"], kde=True, ax=axes[0])
axes[0].set_title("Age Distribution")

sns.histplot(data["duration"], kde=True, ax=axes[1])
axes[1].set_title("Duration Distribution")

st.pyplot(fig)

# Show analysis of contact frequency
st.subheader("Contact Frequency Analysis")
st.write(
    "Most people were contacted 1 to 3 times. Below is the distribution of contact counts:"
)

call_counts = data["campaign"].value_counts()
st.bar_chart(call_counts)

# Month analysis
st.subheader("Monthly Call and Acceptance Analysis")
month_calls = data["month"].value_counts()
st.write("Number of calls by month:")
st.bar_chart(month_calls)

st.set_option("deprecation.showPyplotGlobalUse", False)


# job vs y stacked bar chart with labels
st.subheader("Job vs. Acceptance Analysis")
job_acceptance = data.groupby(["job", "y"])["y"].count()
job_acceptance = job_acceptance.unstack("y")
job_acceptance.plot(kind="bar", stacked=True)
st.pyplot()

# marital vs y Stacked bar chart with labels
st.subheader("Marital Status vs. Acceptance Analysis")
marital_acceptance = data.groupby(["marital", "y"])["y"].count()
marital_acceptance = marital_acceptance.unstack("y")
marital_acceptance.plot(kind="bar", stacked=True)
st.pyplot()

# default pie chart
st.subheader("Credit Default Analysis")
default_counts = data["default"].value_counts()
st.write("Credit default counts:")
st.bar_chart(default_counts)

# loan  pie chart with labels
st.subheader("Loan vs. Acceptance Analysis")
loan_acceptance = data.groupby(["loan", "y"])["y"].count()
loan_acceptance = loan_acceptance.unstack("y")
loan_acceptance.plot(kind="bar", stacked=True)
st.pyplot()

# contact vs y Stacked bar chart with labels
st.subheader("Contact vs. Acceptance Analysis")
contact_acceptance = data.groupby(["contact", "y"])["y"].count()
contact_acceptance = contact_acceptance.unstack("y")
contact_acceptance.plot(kind="bar", stacked=True)
st.pyplot()

# Display data insights
st.subheader("Key Insights")
insights = [
    "Duration Outliers: The maximum duration value (4918) appears to be an outlier, indicating that the column is skewed.",
    "Campaign Outliers: The 'campaign' column also shows signs of skewness, suggesting potential outliers.",
    "Client Contact History: Most clients have not been contacted before, as indicated by the 'pdays' value of 999.",
    "Previous and Pdays Relationship: The 'previous' variable aligns with the 'pdays' insights, reinforcing that many clients were not contacted previously.",
    "Emp.var.rate Skewness: The 'emp.var.rate' column is skewed, which may impact the analysis.",
    "Unknown Values: Several columns contain 'unknown' values, which might need further investigation or handling.",
    "Age Distribution: The 'age' variable is right-skewed, with the most common age being 31.",
    "Target Age Range: The target age group tends to fall between 32 and 47 years (interquartile range), representing a highly productive age bracket.",
    "Call Duration: The duration of most calls ranges from 102 to 319 seconds.",
    "Call Frequency: Most clients receive between 1 to 3 calls.",
    "Campaign Contact: Most people did not contact from this campaign, and similarly, most did not contact in previous campaigns.",
    "Call Attempts: If contacted, it was usually only 1 or 2 times.",
    "Occupation Insights: 'Admin.' and 'technician' occupations are more likely to subscribe to term deposits.",
    "Education Insights: 'University degree' holders are the most common group to take a deposit.",
    "Credit Default: Most people do not have credit in default.",
    "Month Analysis: The month with the most calls is May, which also has the highest number of accepted deposits. In October, December, March, and September, the number of 'yes' responses is roughly the same as the number of 'no' responses.",
    "Daily Trends: The percentage of people saying 'yes' is roughly equal every day, and campaign calls are only made on working days.",
    "Success Likelihood: People who have succeeded in similar situations are likely to take the deposit.",
    "Nonexistent Class Frequency: 'Nonexistent' is the most frequent class.",
    "Prior Contact Impact: People who were contacted before this campaign are more likely to make a deposit, yet most people were not contacted previously.",
    "Deposit Acceptance: A majority of people do not accept deposits, and there are no discernible trends in this data.",
    "Call Effectiveness: Making more calls in a campaign does not necessarily lead to more deposits, as most people who do make a deposit do so after a minimum number of calls.",
    "Call Strategy: Making more calls in the same campaign is generally ineffective, as people who receive more than one or two calls usually do not change their minds. When the number of calls decreases and the duration of each call increases, people are more likely to say 'yes.'",
]
for insight in insights:
    st.write(f"- {insight}")
