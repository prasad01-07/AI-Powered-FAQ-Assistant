import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* ---------- Main Background ---------- */

    .stApp{
        background:linear-gradient(135deg,#EEF5FF,#F8FBFF,#FFFFFF);
        color:#1F2937;
    }

    .block-container{
        max-width:1200px;
        padding-top:2rem;
        padding-bottom:2rem;
    }

    /* ---------- Headings ---------- */

    h1{
        color:#1E3A8A;
        font-size:52px;
        font-weight:800;
        letter-spacing:-1px;
    }

    h2{
        color:#1F2937;
        font-size:34px;
        font-weight:700;
    }

    h3{
        color:#374151;
        font-size:24px;
        font-weight:700;
    }

    /* ---------- Buttons ---------- */

    div.stButton > button{
        width:100%;
        background:linear-gradient(90deg,#2563EB,#3B82F6);
        color:white;
        border:none;
        border-radius:14px;
        padding:14px;
        font-size:18px;
        font-weight:700;
        transition:0.3s;
        box-shadow:0 8px 20px rgba(37,99,235,.30);
    }

    div.stButton > button:hover{
        background:linear-gradient(90deg,#1D4ED8,#2563EB);
        transform:translateY(-2px);
        box-shadow:0 12px 25px rgba(37,99,235,.40);
    }

    /* ---------- Text Input ---------- */

    div[data-testid="stTextInput"] input{

        background:white;
        border:2px solid #D6E4FF;
        border-radius:14px;
        padding:14px;
        font-size:17px;
        box-shadow:0 4px 12px rgba(0,0,0,.05);

    }

    div[data-testid="stTextInput"] input:focus{

        border:2px solid #2563EB;

    }

    /* ---------- Select Box ---------- */

    div[data-baseweb="select"]{

        background:white;
        border-radius:14px;

    }

    /* ---------- Cards ---------- */

    div[data-testid="stMetric"]{

        background:white;

        border-radius:20px;

        padding:20px;

        box-shadow:0 8px 20px rgba(0,0,0,.08);

        border:1px solid #E5E7EB;

    }

    /* ---------- Progress ---------- */

    div[data-testid="stProgressBar"]{

        border-radius:10px;

    }

    /* ---------- Expander ---------- */

    details{

        background:white;

        border-radius:15px;

        padding:10px;

        border:1px solid #E5E7EB;

        box-shadow:0 5px 15px rgba(0,0,0,.05);

    }

    /* ---------- Sidebar ---------- */

    section[data-testid="stSidebar"]{

        background:linear-gradient(180deg,#1E3A8A,#2563EB);

    }

    section[data-testid="stSidebar"] *{

        color:white;

    }

    /* ---------- Horizontal Line ---------- */

    hr{

        border:1px solid #E5E7EB;

    }

    /* ---------- Scrollbar ---------- */

    ::-webkit-scrollbar{

        width:10px;

    }

    ::-webkit-scrollbar-thumb{

        background:#3B82F6;

        border-radius:10px;

    }

    ::-webkit-scrollbar-track{

        background:#E5E7EB;

    }

    </style>
    """, unsafe_allow_html=True)