import streamlit as st

st.title("Meu programa")
st.write("Alô mundo")
st.image("images/programming-background-with-person-working-with-codes-computer-1200x800")
nome = st.text_input("Digite o seu nome:")
if nome:
    st.write(nome.upper())
