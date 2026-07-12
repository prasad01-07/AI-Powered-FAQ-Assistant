import streamlit as st

# ---------------- Sidebar ----------------

def sidebar():

    st.sidebar.title("📌 Project Information")

    st.sidebar.markdown("""
### 🤖 AI-Powered FAQ Assistant

This application uses Semantic Search to understand user questions and retrieve the most relevant FAQ answer.

### 🚀 Technologies

- Python
- Streamlit
- Sentence Transformers
- Scikit-learn
- PyTorch

### 👨‍💻 Developed By

Prasad Jella
""")

    if st.sidebar.button("🗑 Clear Conversation"):
        st.session_state.history = []
        st.rerun()


# ---------------- Example Questions ----------------

def example_questions():

    st.subheader("💡 Example Questions")

    st.info("""
• What is AI?

• Explain Python

• What is Machine Learning?

• Explain Deep Learning

• What is OpenCV?

• What is Streamlit?
""")


# ---------------- Footer ----------------

def footer():

    st.markdown("---")

    st.caption(
        "🚀 AI-Powered FAQ Assistant | Developed by Prasad Jella"
    )