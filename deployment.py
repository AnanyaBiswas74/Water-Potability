import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome To Water Portability Prediction')


st.sidebar.header('User Input Parameters')

def user_input_features():
    
    
    ph = st.sidebar.number_input("ph ",min_value=0,max_value=15,value=0)
    ha = st.sidebar.number_input("Hardness",min_value=0,max_value=15,value=0)
    so = st.sidebar.number_input("Solids",min_value=0,max_value=57000,value=0)
    ch = st.sidebar.number_input("Chloramines",min_value=0,max_value=15,value=0)
    su = st.sidebar.number_input("Sulfate",min_value=0,max_value=485,value=0)
    oc = st.sidebar.number_input("Organic_carbon",min_value=0,max_value=30,value=0)
   
    tri = st.sidebar.number_input("Trihalomethanes",min_value=0,max_value=124,value=0)
    
    new = {
         'ph': ph,
         'Hardness': ha,
         'Solids': so,
         'Chloramines': ch,
         'Sulfate': su,
         'Organic_carbon': oc,
         
         'Trihalomethanes': tri
            }
    features = pd.DataFrame(new,index = [0])
    return features 


df = user_input_features()
st.write(df)



import pickle

with open(file="Final_model.pkl",mode="rb") as f:
    model = pickle.load(f)
    
st.write("Model loaded")



result = model.predict(df)
st.subheader('Predicted Result')

if result[0]==0:
    st.write("Water is not Portable")
    
else:
    st.write("Water is Portable")