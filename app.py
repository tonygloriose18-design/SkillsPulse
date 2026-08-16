import streamlit as st

# Page Configuration
st.set_page_config(page_title="SkillsPulse", page_icon="⚡", layout="wide")

# Sidebar Menu Section
st.sidebar.title("⚡ SkillsPulse Menu")
st.sidebar.markdown("---")

# Sidebar Navigation Options
page = st.sidebar.radio("Navigate to:", ["Home", "My Dashboard", "Settings"])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Pro Tip:** Keep track of your daily learning goals here!")

# Main Page Content based on Sidebar Selection
if page == "Home":
    st.title("⚡ Welcome to SkillsPulse")
    st.subheader("Pulse-check your career. Build in-demand skills in minutes.")

    st.write(
        "SkillsPulse helps you analyze your current skill set, spot industry gaps, "
        "and create an actionable AI-driven roadmap to accelerate your career growth."
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🎯 Skill Gap Analysis")
        st.write("Compare your current skills against top job descriptions.")

    with col2:
        st.markdown("### 🚀 Custom Roadmaps")
        st.write("Get step-by-step learning paths tailored to your schedule.")

    with col3:
        st.markdown("### 📈 Progress Tracking")
        st.write("Monitor your growth and celebrate completed milestones.")

elif page == "My Dashboard":
    st.title("📊 My Dashboard")
    st.write("Track your active learning paths and progress here.")

elif page == "Settings":
    st.title("⚙️ Settings")
    st.write("Manage your account preferences and notifications.")