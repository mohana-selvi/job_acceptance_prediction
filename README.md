# 📊 Job Acceptance Prediction System

This project predicts whether a candidate is likely to get placed based on interview performance, skills match, academic performance, and experience. It also includes a KPI dashboard built using Streamlit.



## 🚀 Project Overview
The Job Acceptance Prediction System is a Machine Learning-based project designed to predict whether a candidate is likely to be placed based on key performance metrics such as interview score, skills match percentage, academic performance, aptitude, communication skills, and work experience.
The system also includes a Streamlit interactive dashboard to visualize hiring trends and key performance indicators (KPIs).
- Machine Learning model: Random Forest Classifier
- Dashboard: Streamlit
- Goal: Predict candidate placement probability and visualize key hiring insights.


## ❓Problem Statement
Hiring teams often struggle to identify which candidates are most likely to accept job offers and successfully get placed.

Traditional screening methods:
- Lack predictive intelligence
- Do not quantify placement probability
- Provide limited analytical insights
  
This project solves that problem by:
- Using Machine Learning to predict placement likelihood
- Analyzing performance metrics
- Providing actionable hiring insights

## 🎯Project Objective
- Build a predictive model to classify candidate placement status.
- Identify key factors influencing job acceptance.
- Provide business insights through KPI visualization.
- Enable HR teams to make data-driven hiring decisions.



## 📌 Key Features
📊 Interactive KPI Dashboard showing placement trends and candidate statistics

🤖 Machine Learning Prediction Model to estimate candidate placement likelihood

📈 Data Visualization including placement distribution and interview score trends

🎯 Real-time Prediction Interface using Streamlit inputs

🧹 Data Cleaning & Feature Engineering Pipeline for improved model performance

📉 Risk Candidate Identification based on probability scoring

💼 Business-Oriented Insights derived from data analysis

This project integrates analytics, prediction, and visualization into a single unified dashboard.


## 📂Dataset Overview
The dataset used in this project contains candidate information related to job placement and acceptance prediction.

Key Dataset Details:
- Includes candidate academic performance, skills, interview scores, and experience
- Contains both numerical and categorical features
- Cleaned dataset used after preprocessing and feature engineering
- Total records: ~50,000+ candidates (approximate)
- Target variable: Placement Status (Placed / Not Placed)
This dataset helps analyze factors influencing job placement success and candidate acceptance probability.

## 🔎Exploratory Data Analysis (EDA)
The dataset was analyzed to understand:

- Distribution of interview scores
- Placement vs non-placement ratio
- Skills match percentage trends
- Correlation between academic performance and placement
- Impact of experience on hiring outcomes

Key EDA Observations:
- Majority of placed candidates had interview scores above 65.
- Skills match percentage showed strong correlation with placement.
- Candidates with 1+ years experience had higher placement probability.


## 🛠Feature Engineering
The following features were engineered or refined:

- interview_total
- skills_match_percentage
- academic_average
- years_of_experience
- aptitude_score
- communication_score
- placement_probability_score (risk evaluation metric)
  
Data cleaning included:

- Handling missing values
- Feature normalization
- Outlier checks
- Encoding categorical variables 




## 📌Key Performance Indicators (KPI)
The Streamlit dashboard displays:

Total Candidates

Placement Rate (%)

Job Acceptance Rate (%)

Average Interview Score

Skills Match Percentage

Offer Dropout Rate (%)

High-Risk Candidate Percentage (%)



## 🤖Machine Learning Model
Algorithm Used: Random Forest Classifier

Problem Type: Binary Classification

Target Variable: status_placed

Model trained to predict:

- 1 → Likely Placed
- 0 → Not Likely Placed




## 💻Technologies Used

This project combines data analytics, machine learning, and web application development tools to build an end-to-end job acceptance prediction system.

Python – Core programming language for data processing and model development

Pandas & NumPy – Data manipulation and numerical analysis

Matplotlib – Data visualization and graphical analysis

Scikit-learn – Machine learning model development (Random Forest Classifier)

Streamlit – Interactive dashboard creation and deployment

Pickle – Model serialization for deployment

Jupyter Notebook – Data analysis, experimentation, and model training

These technologies together enable efficient data analysis, predictive modeling, and interactive visualization.



## 💡Project Insights
Key findings derived from data analysis and modeling:

- Candidates with higher skills match percentage have significantly better placement probability.
- Interview performance strongly influences job acceptance outcomes.
- Academic consistency contributes positively to placement success.
- Candidates with relevant experience show higher acceptance rates.
- Low placement probability scores help identify high-risk candidates early.
- Communication and aptitude scores play a supporting role in final placement decisions.
  
These insights can help recruiters and training teams improve candidate readiness.




## ▶️How to Run Project

To run this project locally, follow the steps below:

1. Install Required Dependencies

Make sure Python is installed, then install all required libraries:

Copy code

pip install -r requirements.txt

2. Extract Model Files
   
Due to GitHub file size limitations, trained machine learning models are uploaded as ZIP files.

Extract the following files before running the application:

Copy code

- placement_model.zip
- random_forest_model.zip

Ensure the extracted .pkl model files are placed in the project root directory alongside:

Copy code

streamlit_app.py

3. Launch the Streamlit Dashboard
Run the following command in your terminal:

Copy code

streamlit run streamlit_app.py

The application will automatically open in your default web browser.




## 🌐Deployment Link







## ✅Conclusion 

This project successfully demonstrates how data analytics and machine learning can be applied to predict job acceptance outcomes.
By combining data preprocessing, feature engineering, predictive modeling, and dashboard visualization, the system provides actionable insights for candidate evaluation.
The Streamlit dashboard makes predictions accessible in real-time, enabling better decision-making for recruitment and training processes.









