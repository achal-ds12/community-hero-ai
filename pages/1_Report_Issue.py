import os
import streamlit as st
from PIL import Image

from ai.gemini import analyze_issue
from database.database import add_issue

st.set_page_config(page_title="Report Issue", page_icon="📷")

st.title("📷 Report Community Issue")
st.write("Fill in the details below to report a community issue.")

st.divider()

title = st.text_input("Issue Title")

description = st.text_area("Issue Description")

location = st.text_input("Location")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

if st.button("Analyze & Submit"):

    if not title or not description or not location:
        st.error("Please fill in all the fields.")

    elif uploaded_file is None:
        st.error("Please upload an image.")

    else:
        # Create folder if it doesn't exist
        os.makedirs("uploaded_images", exist_ok=True)

        # Save uploaded image
        image_path = os.path.join(
            "uploaded_images",
            uploaded_file.name
        )

        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Analyze image + description using Gemini
        analysis = analyze_issue(description, image_path)

        # Save to database
        add_issue(
            title,
            description,
            location,
            image_path,
            analysis["category"],
            analysis["severity"],
            analysis["priority"],
            analysis["department"],
            analysis["summary"]
        )

        st.success("🎉 Issue submitted successfully!")

        st.markdown("---")
        st.markdown("## 🤖 AI Analysis Report")

        col1, col2 = st.columns(2)

        with col1:
            st.info(f"**🏷️ Category**\n\n{analysis['category']}")
            st.warning(f"**🚨 Severity**\n\n{analysis['severity']}")
            st.error(f"**⚡ Priority**\n\n{analysis['priority']}")

        with col2:
            st.success(f"**🏢 Department**\n\n{analysis['department']}")
            st.info(f"**📝 Summary**\n\n{analysis['summary']}")

        st.markdown("### 💡 AI Recommended Action")

        st.success(analysis["recommended_action"])