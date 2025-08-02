import streamlit as st
import numpy as np
import pandas as pd 
import joblib

# Load the trained model
with open('final_model.joblib','rb') as file:
    model = joblib.load(file)

# Prediction function
def prediction(inp_list):
    pred = model.predict([inp_list])[0]
    if pred == 0:
        return 'Sitting on bed'
    elif pred == 1:
        return 'Sitting on chair'
    elif pred == 2:
        return 'Lying on bed'
    else:
        return 'Ambulating'

# Main function to build Streamlit UI
def main():
    st.title('HUMAN ACTIVITY RECOGNITION USING WEARABLE SENSOR DATA')
    st.subheader('''Predict human activity in real time using wearable sensor inputs. Enter the required values to get the predicted activity.''')
    st.image('image.webp')

    # Dropdowns
    rfid = st.selectbox('Enter the RFID configuration settings', ['Config 1 (4 Sensors)', 'Config 2 (3 Sensors)'])
    rfid_e = 3 if rfid == 'Config 2 (3 Sensors)' else 4

    ant_ID = st.selectbox('Select the Antenna ID', [1, 2, 3, 4])

    # Input fields
    rssi = st.text_input('Enter the received signal strength indicator (RSSI)')
    accv = st.text_input('Enter the vertical acceleration data from sensor')
    accf = st.text_input('Enter the frontal acceleration data from sensor')
    accl = st.text_input('Enter the lateral acceleration data from sensor')

    # On Predict button click
    if st.button('Predict'):
        if not all([rssi, accv, accf, accl]):
            st.error("Please fill in all sensor values.")
        else:
            try:
                # Prepare input list
                inp_list = [float(accf), float(accv), float(accl), int(ant_ID), float(rssi), int(rfid_e)]
                response = prediction(inp_list)
                st.success(f"Predicted Activity: {response}")
            except ValueError:
                st.error("Please enter valid numeric values in all fields.")

# Run the app
if __name__ == '__main__':
    main()
