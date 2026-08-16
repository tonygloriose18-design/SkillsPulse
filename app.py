import streamlit as st

# Page Title
st.title("SkillsPulse AI 🚀")
st.subheader("Welcome to our Career & Skills Analysis Tool")

# Put your copied image link between the quotes below:
image_url = "PASTE_YOUR_COPIED_IMAGE_LINK_HERE"

# Display the image safely
try:
    st.image(image_url, caption="SkillsPulse AI Platform", use_container_width=True)
except:
    st.info("Paste a valid image link above to display your hero image!")

# Interactive Section
st.write("---")
st.header("Get Started")
job_role = st.selectbox("Select your target role:", ["Data Analyst", "Software Engineer", "AI Specialist"])
st.success(f"You selected: {job_role}")
