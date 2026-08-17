import streamlit as st
import requests

# 1. Page Setup & Configuration
st.set_page_config(
    page_title="SkillsPulse - Essential Skills Academy",
    page_icon="📚",
    layout="wide"
)

# 2. Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to section:",
    [
        "🏠 Home Dashboard", 
        "🤖 SkillsPulse AI Assistant", 
        "📚 Learning Modules", 
        "📝 Self-Assessment & Roadmap", 
        "ℹ️ About Platform"
    ]
)

HERO_IMAGE_URL = "https://images.unsplash.com/photo-1773332585956-2d0e8ac80cb6?q=80&w=387&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# 3. PAGE 1: HOME DASHBOARD
if page == "🏠 Home Dashboard":
    st.title("📚 SkillsPulse: Essential Skills Academy")
    st.write("Welcome to your central hub for practical, everyday digital and professional skills.")
    
    try:
        st.image(HERO_IMAGE_URL, caption="Empowering Everyday Learning", use_container_width=True)
    except:
        st.info("Image loading...")
        
    st.divider()
    
    st.header("⚡ Quick Dashboard Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Active Modules", value="7 Topics")
    with col2:
        st.metric(label="Difficulty Level", value="Beginner Friendly")
    with col3:
        st.metric(label="Estimated Time", value="2 Hours / Module")
    with col4:
        st.metric(label="Access Cost", value="100% Free")

    st.write("---")
    st.subheader("💡 Featured Learning Tracks Today")
    c1, c2 = st.columns(2)
    with c1:
        st.success("**💻 Digital Literacy**\n\nLearn essential computer navigation, internet search, and safe email practices.")
        st.info("**📄 Professional Writing**\n\nBuild job-ready resumes, cover letters, and formal communication skills.")
        st.success("**🛠️ Troubleshooting & Tech Basics**\n\nFix common software glitches, manage storage, and understand system settings.")
    with c2:
        st.warning("**📊 Essential Office Tools**\n\nMaster spreadsheets (Excel), document design (Docs), and slideshows (Slides).")
        st.error("**🔒 Digital Security**\n\nProtect your accounts, avoid online scams, and secure personal information.")
        st.info("**🌐 Remote Collaboration & AI Tools**\n\nMaster Zoom, Google Workspace, and basic AI productivity helpers.")

# 4. PAGE 2: AI CHATBOT ASSISTANT
elif page == "🤖 SkillsPulse AI Assistant":
    st.title("🤖 SkillsPulse AI Tutor")
    st.write("Ask any questions about basic digital skills, document formatting, or resume writing!")

    api_key = st.secrets.get("EJOCHAT_API_KEY", "")
    
    if not api_key:
        st.error("Please configure EJOCHAT_API_KEY in Streamlit Cloud secrets.")
        st.stop()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_prompt := st.chat_input("Ask a question (e.g., 'How do I create a table in Word?')..."):
        st.chat_message("user").markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            headers = {
                "X-API-Key": api_key,
                "Content-Type": "application/json"
            }
            payload = {
                "messages": st.session_state.messages
            }

            try:
                response = requests.post(
                    "https://api.ejolabs.com/api/v1/subiza",
                    json=payload,
                    headers=headers,
                    timeout=15
                )

                if response.status_code == 200:
                    data = response.json()
                    assistant_reply = data.get("reply") or data.get("message") or data.get("choices", [{}])[0].get("message", {}).get("content", str(data))
                    message_placeholder.markdown(assistant_reply)
                    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
                else:
                    st.error(f"API Error ({response.status_code}): {response.text}")

            except Exception as err:
                st.error(f"Connection error: {err}")

# 5. PAGE 3: LEARNING MODULES
elif page == "📚 Learning Modules":
    st.title("📚 Interactive Learning Modules")
    st.write("Select a topic below to access structured guides, video tutorials, and practical exercises.")
    
    category = st.selectbox(
        "Choose a module to explore:",
        [
            "💻 Basic Computer & Internet Literacy",
            "📄 Professional Writing & Resume Building",
            "📊 Essential Tools (Excel, Docs & Slides)",
            "🗣️ Communication & Workplace Soft Skills",
            "🔒 Online Safety & Digital Security",
            "🛠️ Tech Troubleshooting & System Maintenance",
            "🌐 Remote Work & Digital Collaboration Tools"
        ]
    )
    
    st.divider()
    
    if category == "💻 Basic Computer & Internet Literacy":
        st.subheader("💻 Computer & Internet Basics")
        
        tab1, tab2, tab3 = st.tabs(["🎥 Video Lesson", "📖 Reading & Steps", "📥 Resources"])
        
        with tab1:
            st.write("#### Watch: Master Computer Navigation")
            st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")
            
        with tab2:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info("**Module A: Navigation**\n\n• OS basics & desktop management\n• Organizing folders & files\n• Web browser navigation")
            with col2:
                st.info("**Module B: Email Setup**\n\n• Creating professional emails\n• Structuring clear messages\n• Sending attachments safely")
            with col3:
                st.info("**Module C: Web Search**\n\n• Google search strategies\n• Identifying trusted websites\n• Downloading documents")
                
        with tab3:
            st.write("#### Download Practice Cheat Sheet")
            sample_guide = "Keyboard Shortcuts Cheat Sheet:\n- Ctrl+C: Copy\n- Ctrl+V: Paste\n- Ctrl+Z: Undo\n- Ctrl+S: Save"
            st.download_button(
                label="📄 Download Shortcuts Guide (TXT)",
                data=sample_guide,
                file_name="computer_basics_cheat_sheet.txt",
                mime="text/plain"
            )

    elif category == "📄 Professional Writing & Resume Building":
        st.subheader("📄 Resume & Professional Writing")
        
        tab1, tab2, tab3 = st.tabs(["🎥 Video Lesson", "📖 Reading & Steps", "📥 Resources"])
        
        with tab1:
            st.write("#### Watch: How to Write a Winning Resume")
            st.video("https://www.youtube.com/watch?v=ttWk4n0edgg")
            
        with tab2:
            col1, col2 = st.columns(2)
            with col1:
                st.success("**Resume Builder Guide**\n\n• Summary writing\n• Listing practical experience\n• Clean formatting templates")
            with col2:
                st.success("**Cover Letters & Emails**\n\n• Application letter layouts\n• Tailoring experience to jobs\n• Professional follow-ups")
                
        with tab3:
            st.write("#### Download Sample Templates")
            resume_template = "FIRST NAME LAST NAME\nEmail: example@email.com\n\nPROFESSIONAL SUMMARY\nDedicated professional with background in..."
            st.download_button(
                label="📄 Download Starter Resume Template (TXT)",
                data=resume_template,
                file_name="resume_template.txt",
                mime="text/plain"
            )

    elif category == "📊 Essential Tools (Excel, Docs & Slides)":
        st.subheader("📊 Essential Office Applications")
        tab1, tab2 = st.tabs(["🎥 Video Lesson", "📖 Reading & Steps"])
        with tab1:
            st.write("#### Watch: Excel Basics for Beginners")
            st.video("https://www.youtube.com/watch?v=rwbho0CgEAE")
        with tab2:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.warning("**Word Docs**\n\n• Document formatting\n• Tables & headers\n• Exporting to PDF")
            with col2:
                st.warning("**Spreadsheets**\n\n• Data entry basics\n• SUM & AVERAGE formulas\n• Simple visual charts")
            with col3:
                st.warning("**Presentations**\n\n• Creating clean slides\n• Content structure\n• Visual design tips")

    elif category == "🗣️ Communication & Workplace Soft Skills":
        st.subheader("🗣️ Soft Skills & Workplace Habits")
        col1, col2 = st.columns(2)
        with col1:
            st.info("**Interpersonal Skills**\n\n• Active listening\n• Teamwork basics\n• Clear verbal communication")
        with col2:
            st.info("**Time Management**\n\n• Prioritizing tasks\n• Setting daily goals\n• Meeting deadlines")

    elif category == "🔒 Online Safety & Digital Security":
        st.subheader("🔒 Online Safety & Privacy")
        col1, col2 = st.columns(2)
        with col1:
            st.error("**Account Protection**\n\n• Creating strong passwords\n• Setting up 2FA\n• Spotting phishing emails")
        with col2:
            st.error("**Privacy Rules**\n\n• Social media privacy\n• Safe public Wi-Fi habits\n• Avoiding fake website scams")

    elif category == "🛠️ Tech Troubleshooting & System Maintenance":
        st.subheader("🛠️ Tech Troubleshooting Basics")
        col1, col2 = st.columns(2)
        with col1:
            st.success("**Device Maintenance**\n\n• Clearing cache & temporary files\n• Managing storage space\n• Restarting frozen applications")
        with col2:
            st.success("**Connectivity Issues**\n\n• Resetting Wi-Fi routers\n• Checking network adapter settings\n• Managing browser extensions")

    elif category == "🌐 Remote Work & Digital Collaboration Tools":
        st.subheader("🌐 Remote Collaboration Tools")
        col1, col2 = st.columns(2)
        with col1:
            st.warning("**Virtual Meetings**\n\n• Zoom & Google Meet etiquette\n• Screen sharing controls\n• Mic & camera configuration")
        with col2:
            st.warning("**Cloud Storage**\n\n• Google Drive & OneDrive basics\n• Sharing permissions\n• Real-time collaborative editing")

# 6. PAGE 4: SELF-ASSESSMENT & ROADMAP
elif page == "📝 Self-Assessment & Roadmap":
    st.title("📝 Self-Assessment & Roadmap Generator")
    st.write("Test your readiness and generate a custom step-by-step learning path.")
    
    st.subheader("Step 1: Your Info")
    user_name = st.text_input("Enter your name:", placeholder="e.g., Student")
    selected_track = st.selectbox(
        "Select target learning area:", 
        ["Digital Literacy", "Resume & Writing", "Office Tools", "Soft Skills", "Cyber Safety", "Tech Troubleshooting", "Remote Tools"]
    )
    
    st.subheader("Step 2: Current Experience Level")
    level = st.radio("How comfortable are you with this topic?", ["Beginner (Just starting)", "Intermediate (Know basics)", "Advanced (Need polish)"])
    
    st.divider()
    
    if st.button("Generate My Roadmap 🚀"):
        if user_name.strip() == "":
            st.warning("Please enter your name above to generate your plan!")
        else:
            st.balloons()
            st.success(f"### Custom Plan Generated for {user_name}!")
            st.write(f"**Selected Track:** {selected_track} | **Starting Level:** {level}")
            
            st.markdown("""
            #### 📌 Recommended Next Steps:
            1. **Week 1:** Complete Module A fundamentals and practical exercises.
            2. **Week 2:** Complete sample assignments in your target skill area.
            3. **Week 3:** Take the interactive review quiz on the dashboard.
            """)

# 7. PAGE 5: ABOUT PLATFORM
elif page == "ℹ️ About Platform":
    st.title("ℹ️ About SkillsPulse")
    st.write("SkillsPulse is designed to make practical skill learning accessible, structured, and straightforward for everyone.")
    st.write("Designed for class presentations and practical skill demonstration.")

st.divider()
st.caption("SkillsPulse Platform — All-in-One Practical Learning Dashboard")
