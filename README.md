# 🏦 Loan Approval Prediction System

## 📌 Project Overview

The Loan Approval Prediction System is a Machine Learning web application developed to predict whether a loan application is likely to be approved or rejected based on applicant information.

This project uses machine learning algorithms to analyze applicant details such as income, education, employment status, credit history, and property area to assist in loan approval decision-making.

---

## 🚀 Live Demo

**Hugging Face Deployment**

https://mainuddin123-loan-approval-prediction.hf.space

---

## 📂 GitHub Repository

https://github.com/Mainuddin123/Loan-Approval-Prediction-System

---

## 🎯 Objectives

* Predict loan approval status using machine learning.
* Perform data preprocessing and feature engineering.
* Compare multiple classification algorithms.
* Deploy the trained model as an interactive web application.
* Provide real-time loan approval predictions.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit
* Matplotlib
* Seaborn

### Tools

* Git
* GitHub
* Hugging Face Spaces

---

## 📊 Dataset Features

The dataset contains the following applicant information:

* Gender
* Married
* Dependents
* Education
* Self Employed
* Applicant Income
* Coapplicant Income
* Loan Amount
* Loan Amount Term
* Credit History
* Property Area
* Loan Status

### Engineered Features

* Total Income
* EMI
* Income Per Person

---

## 🔍 Machine Learning Workflow

### 1. Data Collection

Loan approval dataset collected for model development.

### 2. Data Cleaning

* Missing value handling
* Data type corrections
* Feature preparation

### 3. Feature Engineering

Created additional features:

* TotalIncome
* EMI
* Income_Per_Person

### 4. Data Preprocessing

* Missing value imputation
* Feature scaling
* One-Hot Encoding

### 5. Model Training

Two machine learning models were trained and evaluated:

* K-Nearest Neighbors (KNN)
* Gaussian Naive Bayes

### 6. Model Evaluation

| Model                | Accuracy |
| -------------------- | -------- |
| KNN Classifier       | 85.37%   |
| Gaussian Naive Bayes | 84.55%   |

### 7. Best Model Selection

✅ K-Nearest Neighbors (KNN)

Accuracy Achieved: **85.37%**

---

## 💻 Application Features

* Interactive User Interface
* Real-Time Predictions
* Professional Dashboard Design
* Loan Approval Status Prediction
* Responsive Web Application
* Public Deployment

---

## 📈 Sample Prediction Results

### Approved Loan Example

* Applicant Income: 15000
* Coapplicant Income: 8000
* Credit History: 1
* Property Area: Semiurban

Prediction:

✅ Loan Approved

### Rejected Loan Example

* Applicant Income: 1000
* Loan Amount: 400
* Credit History: 0
* Property Area: Rural

Prediction:

❌ Loan Rejected

---

## ▶️ How to Run Locally

### Clone Repository

```bash
git clone https://github.com/Mainuddin123/Loan-Approval-Prediction-System.git
```

### Navigate to Project Folder

```bash
cd Loan-Approval-Prediction-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
Loan-Approval-Prediction-System
│
├── app.py
├── loan_pipeline.pkl
├── loan_approved.csv
├── requirements.txt
├── README.md
└── loan price prediction.ipynb
```

---

## 👨‍💻 Developer

**Shaik Khaja Mainuddin**

Artificial Intelligence & Data Science

Saveetha School of Engineering

### Connect With Me

LinkedIn:
https://www.linkedin.com/in/shaik-khajamainuddin

GitHub:
https://github.com/Mainuddin123

---

## ⭐ Project Status

✅ Machine Learning Model Developed

✅ Streamlit Application Developed

✅ GitHub Repository Created

✅ Hugging Face Deployment Completed

✅ Portfolio Ready

✅ Interview Ready

---

### Thank You for Visiting the Project Repository 🚀
