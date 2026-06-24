import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("loan_pipeline.pkl")

# Page Config
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.main-title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#38bdf8;
}

.sub-title{
    text-align:center;
    color:white;
    font-size:18px;
}

.stButton>button{
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    background:linear-gradient(90deg,#2563eb,#06b6d4);
    color:white;
    font-size:20px;
    font-weight:bold;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#1d4ed8,#0891b2);
}

label{
    color:white !important;
    font-weight:bold;
}

[data-testid="stMetricValue"]{
    color:white !important;
}

[data-testid="stMetricLabel"]{
    color:#38bdf8 !important;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class='main-title'>🏦 Loan Approval Prediction System</div>
<div class='sub-title'>
Predict Loan Approval using Machine Learning
</div>
<br>
""", unsafe_allow_html=True)

# Metrics
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("🤖 Model", "KNN")

with c2:
    st.metric("🎯 Accuracy", "85.37%")

with c3:
    st.metric("🟢 Status", "Active")

st.markdown("---")

# Input Columns
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    property_area = st.selectbox(
        "Property Area",
        ["Urban", "Semiurban", "Rural"]
    )

with col2:
    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0,
        value=5000
    )

    coapplicant_income = st.number_input(
        "Coapplicant Income",
        min_value=0,
        value=0
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0,
        value=150.0
    )

    loan_amount_term = st.number_input(
        "Loan Amount Term",
        min_value=1.0,
        value=360.0
    )

    credit_history = st.selectbox(
        "Credit History",
        [1.0, 0.0]
    )

# Prediction Button
if st.button("🔍 Predict Loan Status"):

    total_income = applicant_income + coapplicant_income

    emi = loan_amount / loan_amount_term

    income_per_person = total_income / (int(dependents) + 1)

    input_df = pd.DataFrame({
        "Gender":[gender],
        "Married":[married],
        "Dependents":[int(dependents)],
        "Education":[education],
        "Self_Employed":[self_employed],
        "ApplicantIncome":[applicant_income],
        "CoapplicantIncome":[coapplicant_income],
        "LoanAmount":[loan_amount],
        "Loan_Amount_Term":[loan_amount_term],
        "Credit_History":[credit_history],
        "Property_Area":[property_area],
        "TotalIncome":[total_income],
        "EMI":[emi],
        "Income_Per_Person":[income_per_person]
    })

    prediction = model.predict(input_df)

    if str(prediction[0]).upper() == "Y":

        st.balloons()

        st.success("🎉 Loan Approved")

        st.markdown("""
        <div style="
        background:linear-gradient(90deg,#16a34a,#22c55e);
        padding:18px;
        border-radius:12px;
        text-align:center;
        color:white;
        font-size:22px;
        font-weight:bold;">
        ✅ Congratulations! Loan is likely to be Approved
        </div>
        """, unsafe_allow_html=True)

    else:

        st.error("❌ Loan Rejected")

        st.markdown("""
        <div style="
        background:linear-gradient(90deg,#dc2626,#ef4444);
        padding:18px;
        border-radius:12px;
        text-align:center;
        color:white;
        font-size:22px;
        font-weight:bold;">
        ⚠️ Loan is likely to be Rejected
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<h2 style='text-align:center;color:#38bdf8;'>
🏦 Thank You for Using Loan Approval Prediction System
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center;color:white;'>
Developed by Shaik Khaja Mainuddin
</h4>
""", unsafe_allow_html=True)
