import streamlit as st

from faq_data import faq_data
from semantic_engine import SemanticEngine

from styles import load_css
from ui import sidebar
from ui import example_questions
from ui import footer


# ---------------- Page Config ----------------

st.set_page_config(
    page_title="AI-Powered FAQ Assistant",
    page_icon="🤖",
    layout="wide"
)


# ---------------- Load CSS ----------------

load_css()
# ---------------- Theme ----------------

dark_mode = st.sidebar.toggle("🌙 Dark Mode")
if dark_mode:
    st.markdown("""
    <style>
    .stApp{
        background:#0f172a;
        color:white;
    }

    div[data-testid="stMetric"]{
        background:#1e293b;
        border-radius:15px;
        padding:15px;
    }

    .stTextInput input{
        background:#1e293b;
        color:white;
    }

    .stButton button{
        background:#2563eb;
        color:white;
        border-radius:12px;
    }
    </style>
    """, unsafe_allow_html=True)


# ---------------- Sidebar ----------------

sidebar()


# ---------------- Session ----------------

if "history" not in st.session_state:
    st.session_state.history = []


if "questions_asked" not in st.session_state:
    st.session_state.questions_asked = 0


# ---------------- Main Title ----------------

# ---------------- Main Header ----------------

st.markdown("""
<div style="
background:linear-gradient(90deg,#2563EB,#3B82F6);
padding:30px;
border-radius:18px;
color:white;
box-shadow:0 8px 20px rgba(37,99,235,.25);
margin-bottom:25px;
">

<h1 style="margin:0;color:white;">
🤖 AI-Powered FAQ Assistant
</h1>

<p style="font-size:18px;margin-top:10px;color:white;">
Ask questions in natural language and receive intelligent answers using Semantic Search.
</p>

</div>
""", unsafe_allow_html=True)


# ---------------- Statistics ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div style="
  background:linear-gradient(135deg,#2563EB,#3B82F6);
color:white;cx
    padding:20px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
    ">
    <h3>📚 FAQs</h3>
    <h1 style="color:white;">{len(faq_data)}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
   background:linear-gradient(135deg,#7C3AED,#9333EA);
color:white;
    padding:20px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
    ">
    <h3>🤖 AI Model</h3>
   <h1 style="color:white;">
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="
   background:linear-gradient(135deg,#059669,#10B981);
color:white;
    padding:20px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
    ">
    <h3>💬 Questions</h3>
   <h1 style="color:white;">
    </div>
    """, unsafe_allow_html=True)

# ---------------- Example Questions ----------------

example_questions()


st.divider()


# ---------------- Category ----------------

categories = sorted(
    list(
        set(
            item["category"]
            for item in faq_data
        )
    )
)

selected_category = st.selectbox(
    "📂 Select Category",
    ["All"] + categories
)


# ---------------- Filter ----------------

if selected_category == "All":

    filtered_data = faq_data

else:

    filtered_data = [

        item

        for item in faq_data

        if item["category"] == selected_category

    ]


engine = SemanticEngine(filtered_data)
# ---------------- Search Box ----------------

user_question = st.text_input(
    "💬 Ask your question",
    placeholder="Example: Explain Machine Learning"
)

# ---------------- Search Suggestions ----------------

if user_question:

    suggestions = [

        item["question"]

        for item in filtered_data

        if user_question.lower()

        in item["question"].lower()

    ]

    if suggestions:

        with st.expander("🔍 Suggestions"):

            for s in suggestions:

                st.write("•", s)

# ---------------- Ask Button ----------------

if st.button("🚀 Get Answer"):

    if user_question.strip() == "":

        st.warning("Please enter a question.")

    else:

        result = engine.search(user_question)

        confidence = result["confidence"]

        st.markdown("### 📊 AI Confidence")

        st.progress(min(confidence, 1.0))

        st.write(f"Confidence Score : **{confidence:.2f}**")

        if confidence >= 0.80:

            st.success("🟢 High Confidence")

        elif confidence >= 0.60:

            st.warning("🟡 Medium Confidence")

        else:

            st.error("🔴 Low Confidence")

        if confidence >= 0.50:

            

            st.session_state.questions_asked += 1

            st.session_state.history.append({

                "question": user_question,

                "answer": result["answer"],

                "confidence": round(confidence,2),

                "category": selected_category

            })

        else:

            st.error("Sorry! No suitable answer found.")
            # ---------------- Conversation History ----------------

# ---------------- Conversation ----------------

# ---------------- Conversation ----------------

if st.session_state.history:

    st.markdown("""
    <div style="
    background:linear-gradient(90deg,#1E3A8A,#3B82F6);
    color:white;
    padding:25px;
    border-radius:20px;
    margin-top:25px;
    margin-bottom:20px;
    box-shadow:0 10px 25px rgba(0,0,0,.15);
    ">
    <h1 style="margin:0;">💬 AI Conversation</h1>
    <p style="margin-top:8px;font-size:18px;">
    Your recent conversation with the AI Assistant
    </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.history = []
        st.rerun()

    st.write("")

    for chat in reversed(st.session_state.history):

        # USER MESSAGE
        st.markdown(f"""
        <div style="
        background:#2563EB;
        color:white;
        padding:18px;
        border-radius:18px;
        margin-bottom:12px;
        box-shadow:0 6px 15px rgba(0,0,0,.12);
        ">
        <b>👤 You</b><br><br>
        {chat['question']}
        </div>
        """, unsafe_allow_html=True)

        # AI MESSAGE
        st.markdown(f"""
        <div style="
        background:white;
        color:#111827;
        padding:20px;
        border-radius:18px;
        border-left:6px solid #2563EB;
        margin-bottom:25px;
        box-shadow:0 8px 20px rgba(0,0,0,.08);
        ">
        <b>🤖 AI Assistant</b><br><br>
        {chat['answer']}

        <hr>

        📁 <b>Category:</b> {chat['category']}<br>
        📊 <b>Confidence:</b> {chat['confidence']}
        </div>
        """, unsafe_allow_html=True)

footer()

# ---------------- Footer ----------------

st.divider()

st.markdown("""
<div style="
text-align:center;
padding:20px;
color:#808080;
font-size:15px;
">
🚀 <b>AI-Powered FAQ Assistant</b><br>
Developed by <b>Prasad Jella</b> ❤️
</div>
""", unsafe_allow_html=True)