import numpy as np
import sns as sns
import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
st.title("Transaction Fraud Detection")


data = pd.read_csv('PS_20174392719_1491204439457_log.csv')
# Convert the 'step' column to a datetime format if it represents time
# This step may vary depending on the dataset's structure
# data['step'] = pd.to_datetime(data['step'])

# Set the title of the Streamlit app
st.title('Step per hour vs amount')

# Create a line chart to show trends in fraud incidents over time
# You may need to adapt the column names based on your dataset
fraud_trends = data.groupby('step')['amount'].sum()
st.line_chart(fraud_trends)
st.title('Percentage of Detected vs. Undetected Fraud Transactions')

# Calculate the number of detected and undetected fraud transactions
fraud_counts = data['isFraud'].value_counts()
detected_fraud = fraud_counts[1] if 1 in fraud_counts else 0
undetected_fraud = fraud_counts[0] if 0 in fraud_counts else 0


fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title('Percentage of Detected vs. Undetected Fraud Transactions')
labels = ['Detected', 'Not Detected']
fraud_data = [detected_fraud, undetected_fraud]
colors = ['lightcoral', 'lightskyblue']
ax.pie(fraud_data, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
ax.axis('equal')
st.pyplot(fig)


fraud = data.loc[data.isFraud == 1]
nonfraud = data.loc[data.isFraud == 0]

# Set the title of the Streamlit app
st.title('Scatter Plot of Fraud Data')

# Create a Streamlit scatter plot for fraud data
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Scatter Plot of oldbalance Data')
ax.scatter(fraud['step'], fraud['oldbalanceOrg'], label='oldbalanceOrg', c='r')
ax.scatter(fraud['step'], fraud['oldbalanceDest'], label='oldbalanceDest', c='b')
ax.set_xlabel('Step')
ax.set_ylabel('Amount')
ax.legend()

# Display the scatter plot in Streamlit
st.pyplot(fig)

# Set the title of the Streamlit app


# Create a Streamlit scatter plot for fraud data
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Scatter Plot of newbalalnced Data')
ax.scatter(fraud['step'], fraud['newbalanceOrig'], label='newbalanceOrig', c='r')
ax.scatter(fraud['step'], fraud['newbalanceDest'], label='newbalanceDest', c='b')
ax.set_xlabel('Step')
ax.set_ylabel('Amount')
ax.legend()

# Display the scatter plot in Streamlit
st.pyplot(fig)

# Set the title of the Streamlit app
st.title('Scatter Plot of Fraud Transactions Flagged Correctly')

# Create a Streamlit scatter plot for fraud transactions
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Scatter Plot of Fraud Transactions Flagged Correctly')
ax.scatter(nonfraud['amount'], nonfraud['isFlaggedFraud'], c='g', label='Not Flagged')
ax.scatter(fraud['amount'], fraud['isFlaggedFraud'], c='r', label='Flagged')
ax.set_xlabel('Amount')
ax.set_ylabel('isFlaggedFraud')
ax.legend(loc='upper right', labels=['Not Flagged', 'Flagged'])

# Display the scatter plot in Streamlit
st.pyplot(fig)

