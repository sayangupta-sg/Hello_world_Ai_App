import streamlit as st
import numpy as np
from model import train

#Title
st.title("Hello World AI App")
st.subheader("A simple regression model")

#Train model 
model= train()

#SIDEBAR
st.sidebar.header("Input features")
input_values=st.sidebar.slider("Select value of x ", 1, 10, 1)

#Pprediction
input_array =np.array([[input_values]])
Prediction=model.predict(input_array)

#display result
st.write(f'### Input value : {input_values}')
st.write(f'### Output value: {Prediction[0]:.2f}')