import streamlit as st

st.title("Meu programa")
st.write("Alô mundo")

nome = st.text_input("Digite o seu nome:")
if nome:
    st.write(nome.upper())
 if st.checkbox("Quer ver uma mensagem especial?"):
     st.success("✨ Continue estudando e você vai longe em programação! 🚀")
