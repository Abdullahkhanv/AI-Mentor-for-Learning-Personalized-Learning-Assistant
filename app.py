# =====================================
# AI Mentor for Learning - Streamlit App
# =====================================

import os
import streamlit as st
from groq import Groq

# -------------------------------
# PAGE CONFIG (Gen Z Style)
# -------------------------------
st.set_page_config(
    page_title="AI Mentor 🚀",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# TITLE
# -------------------------------
st.title("🚀 AI Mentor for Learning")
st.markdown("### Your Smart Study Buddy + Project Builder 😎")

# -------------------------------
# API KEY INPUT (SAFE WAY)
# -------------------------------
api_key = st.sidebar.text_input("🔑 Enter your Groq API Key", type="password")

if api_key:
    client = Groq(api_key=api_key)
else:
    st.warning("Please enter your API key to continue")
    st.stop()

MODEL = "llama-3.3-70b-versatile"

# -------------------------------
# GROQ FUNCTION
# -------------------------------
def ask_groq(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model=MODEL,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# -------------------------------
# FEATURE FUNCTIONS
# -------------------------------
def mentor_response(question):
    prompt = f"""
    You are a friendly AI mentor for undergraduate students.
    Explain the concept in a simple, clear way.

    Include:
    - Easy explanation
    - Example
    - Key points

    Question: {question}
    """
    return ask_groq(prompt)


def generate_design(requirement):
    prompt = f"""
    Generate system design for the following project:

    {requirement}

    Include:
    1. UML (Use Case Diagram in text form)
    2. Class Diagram (text)
    3. ERD (Entities + Relationships)

    Format clearly with headings.
    """
    return ask_groq(prompt)


def generate_code(requirement):
    prompt = f"""
    Generate a Python project skeleton for:

    {requirement}

    Include:
    - Folder structure
    - Main files
    - Basic classes
    - Starter functions

    Keep it simple and beginner-friendly.
    """
    return ask_groq(prompt)


# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------
option = st.sidebar.radio(
    "📌 Choose Feature",
    ["📚 Ask Mentor", "🧩 Generate Design", "💻 Generate Code"]
)

# -------------------------------
# FEATURE 1: AI MENTOR
# -------------------------------
if option == "📚 Ask Mentor":
    st.subheader("📚 Ask Your AI Mentor")

    question = st.text_area("Ask anything...", placeholder="Explain UML in simple terms")

    if st.button("Get Answer 💡"):
        if question:
            with st.spinner("Thinking... 🤔"):
                response = mentor_response(question)
                st.success("Done!")
                st.write(response)
        else:
            st.warning("Please enter a question")


# -------------------------------
# FEATURE 2: DESIGN GENERATOR
# -------------------------------
elif option == "🧩 Generate Design":
    st.subheader("🧩 System Design Generator")

    requirement = st.text_area(
        "Enter your project idea",
        placeholder="Library Management System"
    )

    if st.button("Generate Design 🛠️"):
        if requirement:
            with st.spinner("Designing... 🎨"):
                response = generate_design(requirement)
                st.success("Done!")
                st.write(response)
        else:
            st.warning("Please enter a project idea")


# -------------------------------
# FEATURE 3: CODE GENERATOR
# -------------------------------
elif option == "💻 Generate Code":
    st.subheader("💻 Code Skeleton Generator")

    requirement = st.text_area(
        "Enter project requirement",
        placeholder="Student Management System in Python"
    )

    if st.button("Generate Code ⚡"):
        if requirement:
            with st.spinner("Generating code... ⚡"):
                response = generate_code(requirement)
                st.success("Done!")
                st.write(response)
        else:
            st.warning("Please enter a requirement")


# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("✨ Built for Students | Simple • Fast • Smart")
