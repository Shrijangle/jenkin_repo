# set title for login form
import streamlit as st
st.title('Login Here')

st.text_input('Username')
st.text_input('Password',type='password')
st.button('Sign in')
