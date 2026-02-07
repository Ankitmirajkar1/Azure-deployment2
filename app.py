import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

st.set_page_config(page_title="Groq streamlit App", page_icon=":guardsman:", layout="wide")
st.title("LLM App")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

user_input = st.text_input("Enter your query:")

if user_input:
    with st.spinner("Generating response..."):
        try:
            response = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=[
                            {"role": "user", "content": user_input}
                        ]
                    )
            st.success("Response generated successfully!")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error generating response: {e}")