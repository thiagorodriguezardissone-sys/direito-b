import streamlit as st

st.title("Meu programa")
st.write("Alô mundo")

nome = st.text_input("Digite o seu nome:")
if nome:
    st.write(nome.upper())
if st.checkbox("Quer ver uma mensagem especial?"):
     st.success(" Continue estudando e você vai longe em programação! ")
import random

if st.button(" Gerar meu número da sorte"):
    numero = random.randint(1, 100)
    st.success(f"Seu número da sorte é: {numero} ")
ano = st.number_input("Digite seu ano de nascimento:", 1900, 2025)
if ano:
    st.write(f"Você tem {2025 - ano} anos. ")
    st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c", caption="Programando o futuro", use_column_width=True)

