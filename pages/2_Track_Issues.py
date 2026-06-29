import streamlit as st
import pandas as pd

from database.database import get_all_issues, update_status

st.set_page_config(page_title="Track Issues", page_icon="📋")

st.title("📋 Track Community Issues")

issues = get_all_issues()

if not issues:
    st.warning("No issues reported yet.")
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

st.dataframe(df, use_container_width=True)

st.divider()

st.subheader("Update Issue Status")

issue_id = st.selectbox(
    "Select Issue ID",
    df["ID"].tolist()
)

new_status = st.selectbox(
    "New Status",
    ["Pending", "In Progress", "Resolved"]
)

if st.button("Update Status"):
    update_status(issue_id, new_status)
    st.success("Status updated successfully!")
    st.rerun()