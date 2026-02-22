import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# PAGE CONFIG
st.set_page_config(page_title="Job Acceptance Dashboard", layout="wide")
st.title("📊 Job Acceptance Prediction Dashboard")

# LOAD DATASET 
df = pd.read_csv("job_prediction_cleaned_data.csv")

# KPI DASHBOARD
st.header("📌 Key Performance Indicators")

total_candidates = len(df)
placement_rate = df["status_placed"].mean() * 100
job_acceptance_rate = placement_rate
avg_interview_score = df["interview_total"].mean()
avg_skills_match = df["skills_match_percentage"].mean()
offer_dropout_rate = (df["status_placed"] == 0).mean() * 100
high_risk_percentage = (df["placement_probability_score"] < 0.4).mean() * 100

col1, col2, col3 = st.columns(3)
col1.metric("Total Candidates", total_candidates)
col2.metric("Placement Rate (%)", round(placement_rate, 2))
col3.metric("Job Acceptance Rate (%)", round(job_acceptance_rate, 2))

col4, col5, col6 = st.columns(3)
col4.metric("Avg Interview Score", round(avg_interview_score, 2))
col5.metric("Skills Match (%)", round(avg_skills_match, 2))
col6.metric("Offer Dropout (%)", round(offer_dropout_rate, 2))

st.metric("High Risk Candidate (%)", round(high_risk_percentage, 2))


# VISUALIZATION
st.header("📈 Data Visualization")

# Placement distribution
fig, ax = plt.subplots(figsize=(6,3))
df["status_placed"].value_counts().plot(kind="bar", ax=ax)
ax.set_title("Placement Distribution")
st.pyplot(fig)

# Interview score distribution
fig2, ax2 = plt.subplots(figsize=(6,3))
df["interview_total"].hist(ax=ax2)
ax2.set_title("Interview Score Distribution")
st.pyplot(fig2)


# PREDICTION SECTION 
st.header("🎯 Predict Candidate Placement")

import zipfile
import os


if not os.path.exists("placement_model.pkl"):
    with zipfile.ZipFile("placement_model.zip", "r") as zip_ref:
        zip_ref.extractall()

model = pickle.load(open("placement_model.pkl", "rb"))

interview_score = st.number_input("Interview Score", 0, 100, 60)
skills_match = st.number_input("Skills Match %", 0, 100, 70)
academic_avg = st.number_input("Academic Average", 0, 100, 65)
experience = st.number_input("Years Experience", 0, 20, 1)
aptitude = st.number_input("Aptitude Score", 0, 100, 60)
communication = st.number_input("Communication Score", 0, 100, 60)

if st.button("Predict Placement"):

    input_data = pd.DataFrame({
        "interview_total": [interview_score],
        "skills_match_percentage": [skills_match],
        "academic_average": [academic_avg],
        "years_of_experience": [experience],
        "aptitude_score": [aptitude],
        "communication_score": [communication]
    })
    input_data=input_data.astype(float)
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Candidate Likely Placed")
    else:
        st.error("❌ Candidate Not Likely Placed")
