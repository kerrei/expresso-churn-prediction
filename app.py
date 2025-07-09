import streamlit as st
import numpy as np
import pickle

# Load model
with open('../model/churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("📲 Expresso Churn Predictor")

# Input fields (numerical entries only — adapt as needed)
REGION = st.number_input("Region")
TENURE = st.number_input("Tenure (months)")
MONTANT = st.number_input("Recharge Amount")
FREQUENCE_RECH = st.number_input("Recharge Frequency")
REVENUE = st.number_input("Revenue")
ARPU_SEGMENT = st.number_input("ARPU Segment")
FREQUENCE = st.number_input("Call Frequency")
DATA_VOLUME = st.number_input("Data Volume (MB)")
ON_NET = st.number_input("On-Net Usage")
ORANGE = st.number_input("Orange Usage")
TIGO = st.number_input("Tigo Usage")
ZONE1 = st.number_input("Zone 1 Usage")
ZONE2 = st.number_input("Zone 2 Usage")
MRG = st.number_input("Monthly Recharge Group")
REGULARITY = st.number_input("Recharge Regularity")
TOP_PACK = st.number_input("Top Pack (1 = Yes, 0 = No)")  # if binary
FREQ_TOP_PACK = st.number_input("Top Pack Frequency")

# Predict
if st.button("Validate"):
    features = np.array([[
        REGION, TENURE, MONTANT, FREQUENCE_RECH, REVENUE, ARPU_SEGMENT,
        FREQUENCE, DATA_VOLUME, ON_NET, ORANGE, TIGO,
        ZONE1, ZONE2, MRG, REGULARITY, TOP_PACK, FREQ_TOP_PACK
    ]])
    
    prediction = model.predict(features)
    st.success(f"Prediction: {'Churn' if prediction[0] == 1 else 'No Churn'}")