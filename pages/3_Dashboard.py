import streamlit as st
import pandas as pd
import plotly.express as px

from database.database import get_all_issues

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊"
)

st.title("📊 Community Hero Dashboard")

issues = get_all_issues()

if not issues:
    st.warning("No data available.")
    st.stop()

columns = [
    "ID",
    "Title",
    "Description",
    "Location",
    "Image",
    "Category",
    "Severity",
    "Priority",
    "Department",
    "Summary",
    "Status",
    "Reported At"
]

df = pd.DataFrame(issues, columns=columns)

st.divider()

# =====================
# Statistics
# =====================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Issues", len(df))

with col2:
    st.metric(
        "Pending",
        len(df[df["Status"] == "Pending"])
    )

with col3:
    st.metric(
        "High Priority",
        len(df[df["Priority"] == "High"])
    )

with col4:
    st.metric(
        "Resolved",
        len(df[df["Status"] == "Resolved"])
    )

st.divider()

# =====================
# Category Chart
# =====================

category_counts = (
    df["Category"]
    .value_counts()
    .reset_index()
)

category_counts.columns = ["Category", "Count"]

fig1 = px.bar(
    category_counts,
    x="Category",
    y="Count",
    title="Issues by Category"
)

st.plotly_chart(fig1, use_container_width=True)

# =====================
# Status Chart
# =====================

status_counts = (
    df["Status"]
    .value_counts()
    .reset_index()
)

status_counts.columns = ["Status", "Count"]

fig2 = px.pie(
    status_counts,
    names="Status",
    values="Count",
    title="Issue Status Distribution"
)

st.plotly_chart(fig2, use_container_width=True)