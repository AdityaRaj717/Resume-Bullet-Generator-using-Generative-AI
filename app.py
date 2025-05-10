from transformers import pipeline, set_seed
import streamlit as st

generator = pipeline('text-generation', model='gpt2')
set_seed(42)

st.title("Resume Bullet Generator using Generative AI")
st.write("Enter your task or achievement in casual language. The AI will generate a professional resume bullet.")

input_text = st.text_input("Enter your task/achievement:")

if input_text:
    st.subheader("Generated Resume Bullet:")
    prompt = f"Rewrite the following as a professional resume bullet: {input_text}"
    outputs = generator(prompt, max_length=40, num_return_sequences=1)
    st.write(outputs[0]['generated_text'])
