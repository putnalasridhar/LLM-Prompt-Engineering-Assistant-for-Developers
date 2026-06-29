import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #000000;
    color: white;
}

/* Main content */
.main {
    background-color: #000000;
}

/* Text area */
.stTextArea textarea {
    background-color: #111111;
    color: white;
    border: 1px solid #444444;
}

/* Buttons */
.stButton > button {
    background-color: #222222;
    color: white;
    border: 1px solid white;
    border-radius: 8px;
}

.stButton > button:hover {
    background-color: #444444;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read System Prompt
with open("prompt_engineering_assistant.txt", "r", encoding="utf-8") as file:
    system_prompt = file.read()

st.set_page_config(
    page_title="Prompt Engineering Assistant"
)

st.image("image.png", width=800)

st.title("Prompt Engineering Assistant")

user_prompt = st.text_area(
    "Enter your Prompt:",
    height=200
)

if st.button("Generate"):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
    ]
    )

    st.subheader("Response")
    st.write(response.choices[0].message.content)