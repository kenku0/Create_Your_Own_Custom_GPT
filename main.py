import streamlit as st
import openai

openai.api_key = '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'

st.title("Happy Dog GPT (Example)")

user_prompt = st.text_input("Input here")

system_message = "Answer like a happy dog."

if user_prompt:
    messages = [
        {"role": "system", "content":system_message},
        {"role": "user", "content": user_prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    output = response ['choiuces'][0]['message']['content']

    st.write(output)