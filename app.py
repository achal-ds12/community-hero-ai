import streamlit as st
from database.database import create_table
from utils.styles import load_css

# Create database
create_table()

st.set_page_config(
    page_title="Community Hero AI",
    page_icon="🤖",
    layout="wide"
)

# Load custom CSS
load_css()

# Hero Section
st.markdown("""
<div class="hero">
    <h1>🤖 Community Hero AI</h1>
    <h3>AI-Powered Hyperlocal Problem Solver</h3>
    <p>
    Empowering citizens with Google Gemini AI to report, analyze and resolve
    community issues faster and smarter.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 🚀 Welcome to Community Hero AI")

st.write(
    "A smart civic issue reporting platform that combines Artificial Intelligence "
    "with community participation to improve public services."
)

st.markdown("")

# Feature Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📷 AI Issue Reporting</h3>
        <p>
        Upload an image with a description. Gemini AI automatically identifies
        the issue category, severity, priority and responsible department.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📋 Track Issues</h3>
        <p>
        Monitor reported issues, update their status and manage the complete
        issue lifecycle from one dashboard.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>📊 Smart Dashboard</h3>
        <p>
        View analytics, issue statistics and AI-powered insights to help
        authorities make better decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("✨ Key Features")

c1, c2 = st.columns(2)

with c1:
    st.success("📷 Image-based Issue Reporting")
    st.success("🤖 Google Gemini AI Analysis")
    st.success("🏷️ Automatic Issue Categorization")
    st.success("⚡ Severity & Priority Detection")

with c2:
    st.success("🏢 Department Recommendation")
    st.success("📋 Issue Tracking")
    st.success("📊 Analytics Dashboard")
    st.success("💡 AI Recommended Actions")

st.markdown("---")

st.info("👈 Use the sidebar to navigate through the application.")