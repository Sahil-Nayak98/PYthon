import streamlit as st
import pandas as pd
import numpy as np

## title of application
st.title("HELLO Streamlit !")

## Display Simple Text
st.write("This is a simple text")

## create a simple dataframe
df=pd.DataFrame({
  'first column': [1,2,3,4],
  'second column':[10,20,30,40]
 })

## Display Dataframe
st.write("HERE IS THE DataFrame")
st.write(df)

## create a line chart
char_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(char_data)