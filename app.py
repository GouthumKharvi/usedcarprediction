import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load(r'C:\Users\Gouthum\Downloads\ALL-Ml-Dl-PROJECTS\xgb_model.pkl')

st.title("🚗 Used Car Price Prediction")

# Create two columns to reduce scrolling
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox("Company", ['Maruti Suzuki', 'Hyundai', 'Honda', 'BMW', 'Mercedes Benz', 'Other'])
    colour = st.selectbox("Colour", ['White', 'Grey', 'Black', 'Silver', 'Other'])
    age = st.number_input("Age (years)", 0, 30, 3)
    dealer_state = st.selectbox("DealerState", ['Delhi', 'Maharashtra', 'Rajasthan', 'Other'])
    city = st.selectbox("City", ['Delhi', 'Mumbai', 'Bangalore', 'Other'])
    warranty = st.selectbox("Warranty", ['Yes', 'No'])
    quality_score = st.number_input("QualityScore", 0, 10, 7)

with col2:
    fuel_type = st.selectbox("FuelType", ['Petrol', 'Diesel', 'CNG', 'Electric'])
    kilometer = st.number_input("Kilometer", 0, 500000, 50000)
    bodystyle = st.selectbox("BodyStyle", ['SUV', 'Sedan', 'HatchBack', 'MPV', 'Coupe', 'Convertible'])
    owner = st.selectbox("Owner", ['1st Owner', '2nd Owner', '3rd Owner', '4th & Above Owner'])
    dealer_name = st.selectbox("DealerName", ['Car Estate', 'Star Auto India', 'Car Choice', 'Other'])

# Encoding dictionaries
company_map = {'Maruti Suzuki':0, 'Hyundai':1, 'Honda':2, 'BMW':3, 'Mercedes Benz':4, 'Other':5}
fuel_type_map = {'Petrol':0, 'Diesel':1, 'CNG':2, 'Electric':3}
colour_map = {'White':0, 'Grey':1, 'Black':2, 'Silver':3, 'Other':4}
bodystyle_map = {'SUV':0, 'Sedan':1, 'HatchBack':2, 'MPV':3, 'Coupe':4, 'Convertible':5}
owner_map = {'1st Owner':0, '2nd Owner':1, '3rd Owner':2, '4th & Above Owner':3}
dealer_state_map = {'Delhi':0, 'Maharashtra':1, 'Rajasthan':2, 'Other':3}
dealer_name_map = {'Car Estate':0, 'Star Auto India':1, 'Car Choice':2, 'Other':3}
city_map = {'Delhi':0, 'Mumbai':1, 'Bangalore':2, 'Other':3}
warranty_map = {'Yes':1, 'No':0}

# Prepare input data
input_dict = {
    'Company': company_map[company],
    'FuelType': fuel_type_map[fuel_type],
    'Colour': colour_map[colour],
    'Kilometer': kilometer,
    'BodyStyle': bodystyle_map[bodystyle],
    'Age': age,
    'Owner': owner_map[owner],
    'DealerState': dealer_state_map[dealer_state],
    'DealerName': dealer_name_map[dealer_name],
    'City': city_map[city],
    'Warranty': warranty_map[warranty],
    'QualityScore': quality_score
}

input_df = pd.DataFrame([input_dict])

# Predict button with animation
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Used Car Price: ₹{prediction[0]:,.2f}")
    st.balloons()
