import pandas as pd
import streamlit as st
import pickle

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Set the title for your Streamlit app
st.title('Prediction Of CO2 Emissions')

# Create a sidebar for input features
st.sidebar.header('Input Features')

# Define a function to collect user input features
def input_features():
  cylinders=st.sidebar.selectbox('Select No of Cylinders',('3','4','5','6','8','10','12','16'))
  fuel_consumption_comb_mpg=st.sidebar.number_input('Insert The Miles Per Gallon')
  transmission_A=st.sidebar.selectbox('Automatic Transmission (A)',('0','1'))
  transmission_AM=st.sidebar.selectbox('Automated Manual Transmission (AM)',('0','1'))
  transmission_AS=st.sidebar.selectbox('Automatic with Select Shift Transmission (AS)',('0','1'))
  transmission_AV=st.sidebar.selectbox('Continuously Variable Transmission (AV)',('0','1'))
  transmission_M=st.sidebar.selectbox('Manual Transmission (M)',('0','1'))
  fuel_type_D=st.sidebar.selectbox('Fuel Type Diesel (D)',('0','1'))
  fuel_type_E=st.sidebar.selectbox('Fuel Type Ethenal (E)',('0','1'))
  fuel_type_N=st.sidebar.selectbox('Fuel Type Nitrogen (N)',('0','1'))
  fuel_type_X=st.sidebar.selectbox('Fuel Type Normal Gasoline (X)',('0','1'))
  fuel_type_Z=st.sidebar.selectbox('Fuel Type Premium Gasoline (Z)',('0','1'))

  data={'cylinders':cylinders,
              'fuel_consumption_comb(mpg)':fuel_consumption_comb_mpg,
              'transmission_A':transmission_A,
              'transmission_AM':transmission_AM,
              'transmission_AS':transmission_AS,
              'transmission_AV':transmission_AV,
              'transmission_M':transmission_M,
              'fuel_type_D':fuel_type_D,
              'fuel_type_E':fuel_type_E,
              'fuel_type_N':fuel_type_N,
              'fuel_type_X':fuel_type_X,
              'fuel_type_Z':fuel_type_Z}

  features=pd.DataFrame(data,index=[0])
  return features

# Call the input_features() function to collect user input
df=input_features()

# Display the user input features as a subheader and a DataFrame
st.subheader('User Input Features')
st.write(df)

st.subheader('Prediction Result')

if st.button("Predict"):
    if input_features:
        # Make predictions using the loaded model
        predictions = model.predict(df)
        st.write(predictions)
