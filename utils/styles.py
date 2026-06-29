import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .stApp{
        background:linear-gradient(135deg,#0f172a,#111827,#0b1120);
        color:white;
    }

    section[data-testid="stSidebar"]{
        background:#0b1220;
        border-right:1px solid #1e293b;
    }

    h1,h2,h3,h4{
        color:white;
        font-weight:700;
    }

    .hero{
        background:linear-gradient(90deg,#2563eb,#06b6d4);
        padding:35px;
        border-radius:20px;
        margin-bottom:25px;
        color:white;
        box-shadow:0 8px 30px rgba(0,0,0,.35);
    }

    .card{
        background:rgba(255,255,255,.05);
        border:1px solid rgba(255,255,255,.08);
        border-radius:18px;
        padding:20px;
        backdrop-filter:blur(14px);
        margin-bottom:18px;
    }

    .metric{
        background:#111827;
        border-radius:18px;
        padding:20px;
        text-align:center;
        border:1px solid #334155;
    }

    .metric h2{
        color:#38bdf8;
        margin:0;
        font-size:36px;
    }

    .metric p{
        color:#cbd5e1;
        margin-top:8px;
    }

    .stButton>button{
        background:linear-gradient(90deg,#2563eb,#06b6d4);
        color:white;
        border:none;
        border-radius:12px;
        font-size:17px;
        font-weight:600;
        padding:12px 28px;
        transition:.3s;
    }

    .stButton>button:hover{
        transform:scale(1.03);
        box-shadow:0 8px 20px rgba(37,99,235,.45);
    }

    div[data-testid="stFileUploader"]{
        background:#111827;
        border-radius:15px;
        padding:12px;
    }

    textarea,
    input{
        border-radius:12px !important;
    }

    </style>
    """, unsafe_allow_html=True)