# Bank Deposit Campaign: Predicting Term Deposit Subscriptions

## Project Overview
This project aims to build a predictive machine learning pipeline to determine whether a client will subscribe to a term deposit, using the [Bank Marketing dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing) from the UCI Machine Learning Repository. By accurately forecasting client responses, the model assists in refining marketing strategies, prioritizing leads, and increasing campaign efficiency.

The entire project, including the model and exploratory data analysis (EDA), is deployed on a Streamlit web application, allowing stakeholders to access model predictions and insights interactively. Each stage has been documented to provide a comprehensive guide to the project’s methodology, decisions, and outcomes.

---

## Table of Contents
1. [Project Scope](#project-scope)
2. [Data Collection and Exploration](#data-collection-and-exploration)
3. [Data Preprocessing and Feature Engineering](#data-preprocessing-and-feature-engineering)
4. [Model Selection and Training](#model-selection-and-training)
5. [Model Evaluation and Validation](#model-evaluation-and-validation)
6. [Model Deployment and Monitoring](#model-deployment-and-monitoring)
7. [Resources and Links](#resources-and-links)
8. [Expected Outcome](#expected-outcome)

---

### Project Scope
The primary goal of this project is to predict whether a client will subscribe to a term deposit in response to a direct marketing campaign. By identifying high-potential leads, the model optimizes targeting for future campaigns. Key evaluation metrics include precision, recall, F1 score, ROC-AUC, and the confusion matrix.

### Data Collection and Exploration
The Bank Marketing dataset contains customer demographic data, call outcomes, and past campaign information. Exploratory data analysis (EDA) helped identify trends, correlations, and significant features that influence term deposit subscription rates. Data quality checks addressed missing values, outliers, and inconsistencies.

### Data Preprocessing and Feature Engineering
The data preprocessing steps include encoding categorical variables, scaling numerical features, and splitting the data into training, validation, and test sets. Feature engineering based on historical campaign data and customer interactions further enhances model accuracy.

### Model Selection and Training
Several classification models were trained and tested, including logistic regression, SVC, decision trees, random forests, gradient boosting, Adaboost, and XGBoost. Hyperparameter tuning (grid search and random search) was used to optimize the selected model.

### Model Evaluation and Validation
The model was evaluated on the validation and test sets using metrics such as precision, recall, F1 score, ROC-AUC, and a confusion matrix to gauge accuracy and class balance. Error analysis identified areas for improvement, ensuring the model accurately predicts positive and negative outcomes.

### Model Deployment
The final model, along with EDA, is deployed on a Streamlit web app, providing an interactive platform for real-time predictions and data exploration.

---

## Resources and Links
- **Interactive Streamlit App:**: [Streamlit App](https://bank-deposite-campain.streamlit.app/)
- **EDA and Feature Importance Notebook**: [Link to notebook](https://www.kaggle.com/code/ahmedfawzy2/eda-feature-importance)
- **Preprocessing, Modeling, and Deployment Notebook**: [Link to notebook](https://www.kaggle.com/code/ahmedfawzy2/eda-preprocessing-modeling-and-deployment)
- **GitHub Repository**: [Project Repository](https://github.com/Ahmed-Mohamed-Fawzy/bank_deposite_campain)
- **Source of the Data**: [UCI Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/bank+marketing)
- **Dataset Description**: [Kaggle Dataset Description](https://www.kaggle.com/datasets/volodymyrgavrysh/bank-marketing-campaigns-dataset)


---

## Expected Outcome
The final model, accessible through the Streamlit app, predicts the likelihood of a client subscribing to a term deposit, allowing the marketing team to prioritize high-potential leads, improve conversion rates, and reduce campaign costs. The interactive app offers stakeholders real-time insights into model predictions and EDA, while the documentation serves as a reference for each phase of the project, ensuring reproducibility and transparency.
