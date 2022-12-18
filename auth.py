import firebase_auth
import streamlit as st
import requests
import json

firebase_auth.load_credentials("path/to/credentials.json")


def check_credentials(login, password):
    try:
        token = firebase_auth.sign_in_with_email_and_password(login, password)
        return True
    except:
        return False


st.title("Autenticação via Firebase Auth")

login_input = st.text_input("Login")
password_input = st.text_input("Password", type="password")

if check_credentials(login_input, password_input):
    st.write("Autenticação realizada com sucesso!")
else:
    st.write("Login ou senha inválidos. Tente novamente.")
