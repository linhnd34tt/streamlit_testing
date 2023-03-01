import streamlit as st
import pandas as pd

# Takes in a username and prints out a greeting text
st.title('A Simple Streamlit Web App')
name = st.text_input('Enter your name', '')
st.write(f'Hello {name}!')

# Takes in two slider inputs of integers ranging from 0 to 10
x = st.slider('Select an integer x', 0, 10, 1)
y = st.slider('Select an integer y', 0, 10, 1)
df = pd.DataFrame(
    {'x': [x], 'y': [y] , 'x + y': [x + y]}, 
    index = ['addition row'],
)
# Prints out the variables and their sums
st.write(df)