import time
import streamlit as st


st.title("Olá ")

senha = ("eu te amo", "te amo", "te amo muito")
senha_user = st.chat_input("Digite sua senha aqui: ")

if senha_user:
    senha_lower = senha_user.lower()
    if senha_lower in senha:
        st.text("Senha correta! ")
        time.sleep(2)
        st.success("Pena que eu te amo mais!!!")
    else:
        st.text("Senha errada, digite novamente")


























