import streamlit as st
from LLMs import get_response_from_llm

st.title("LLM Arena")

llm_options = ["Llama3-70B", "Llama3-8B", "Mistral", "Gemini", "Claude"]
model_name = st.selectbox("Choose an LLM:", llm_options)
prompt = st.text_area("Enter your prompt:")

if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        response = get_response_from_llm(model_name, prompt)
    st.text_area("Response:", response, height=200)
