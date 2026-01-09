import pandas as pd
import pickle
import streamlit as st
st.set_page_config(page_title='House_Price_Predictor')
st.header('Welcome to Bengaluru House Price Predictor 💰💰')
df=pd.read_csv('copied.csv')
with open('RFmodel.pkl','rb') as file:
    model=pickle.load(file)
with st.container(border=True):
    col1,col2=st.columns(2)
    loc=col1.selectbox('Location',options=df['location'].unique())
    sqft=col2.number_input('total sqft',min_value=300)
    bath=col1.number_input('no of bathrooms',max_value=6,min_value=1)
    bhk=col2.number_input('no of bedrooms',min_value=1,max_value=6)
    locations=list(df['location'].unique())
    locations.sort()
    input_values=[locations.index(loc),sqft,bath,bhk]
    if st.button('Predict Price'):
        out=model.predict([input_values])
        st.subheader(f'the price is {round(out[0]*100000,2)}')
