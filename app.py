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
        "📚 Learning Modules & Quiz Arena", 
        "📝 Self-Assessment & Roadmap", 
        "ℹ️ About Platform"
    ]
)

HERO_IMAGE_URL = "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=800&auto=format&fit=crop"

# 3. PAGE 1: HOME DASHBOARD
if page == "🏠 Home Dashboard":
    st.title("📚 SkillsPulse: Essential Skills Academy")
    st.write("Welcome to your central hub for practical, everyday digital and professional skills.")
    
    try:
        st.image(HERO_IMAGE_URL, caption="Empowering Everyday Digital Learning", use_container_width=True)
    except:
        st.info("Image loading...")
        
    st.divider()
    
    st.header("⚡ Quick Dashboard Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Active Modules", value="3 Core Tracks")
    with col2:
        st.metric(label="Difficulty Level", value="Beginner Friendly")
    with col3:
        st.metric(label="Interactive Quizzes", value="Gamified Scoring")
    with col4:
        st.metric(label="Access Cost", value="100% Free")

    st.write("---")
    st.subheader("💡 Featured Tracks")
    c1, c2 = st.columns(2)
    with c1:
        st.success("**💻 Digital & Computer Literacy**\n\nLearn essential computer navigation, file management, and internet safety.")
        st.info("**📄 Professional Resume Writing**\n\nBuild job-ready resumes, cover letters, and formal application emails.")
    with c2:
        st.warning("**📊 Office Tools & Spreadsheets**\n\nMaster basic spreadsheets, document design, and digital collaboration.")

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

# 5. PAGE 3: LEARNING MODULES & GAMIFIED QUIZ ARENA
elif page == "📚 Learning Modules & Quiz Arena":
    st.title("📚 Interactive Learning Modules & Quiz Arena")
    st.write("Select a topic to read real guides, watch tutorial media, and challenge yourself in the interactive quiz arena!")
    
    category = st.selectbox(
        "Choose a module track:",
        [
            "💻 Basic Computer Literacy & Shortcut Mastery",
            "📄 Professional Writing & Resume Building",
            "📊 Excel & Spreadsheets Essentials"
        ]
    )
    
    st.divider()
    
    # TRACK 1
    if category == "💻 Basic Computer Literacy & Shortcut Mastery":
        st.subheader("💻 Basic Computer Literacy & Shortcut Mastery")
        
        tab1, tab2, tab3 = st.tabs(["📖 Real Guide & Steps", "🎥 Video Tutorial", "🎮 Interactive Quiz Challenge"])
        
        with tab1:
            st.markdown("""
            ### Key Concepts to Master:
            1. **File Management:** Keep your desktop clean. Create folder hierarchies like `Documents/Work/2026/`.
            2. **Essential System Shortcuts:**
               * `Ctrl + C` (Copy) & `Ctrl + V` (Paste)
               * `Ctrl + Z` (Undo accidental actions)
               * `Alt + Tab` (Switch between open windows)
            3. **Browser Basics:** Use bookmarks (`Ctrl + D`) to save important websites.
            """)
            
        with tab2:
            st.write("#### Demonstration Video")
            # Reliable fallback MP4 stream
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")
            st.caption("Note: Interactive video player streams directly within Streamlit.")
            
        with tab3:
            st.subheader("🎮 Skill Challenge: Computer Basics")
            st.write("Test your memory to earn your digital badge!")
            
            q1 = st.radio(
                "Question 1: Which keyboard shortcut allows you to undo an accidental mistake?",
                ["Ctrl + P", "Ctrl + Z", "Ctrl + S", "Alt + F4"],
                key="c_q1"
            )
            
            q2 = st.radio(
                "Question 2: What is the best practice for organizing digital files?",
                ["Leave everything on the desktop", "Create named folders and subfolders", "Delete files after 1 day", "Save all files as images"],
                key="c_q2"
            )
            
            if st.button("Submit Computer Literacy Quiz 🚀"):
                score = 0
                if q1 == "Ctrl + Z":
                    score += 50
                if q2 == "Create named folders and subfolders":
                    score += 50
                
                if score == 100:
                    st.balloons()
                    st.success(f"🏆 Perfect Score: {score}/100! You mastered Computer Basics!")
                else:
                    st.warning(f" You scored {score}/100. Review the reading tab and try again!")

    # TRACK 2
    elif category == "📄 Professional Writing & Resume Building":
        st.subheader("📄 Professional Writing & Resume Building")
        
        tab1, tab2, tab3 = st.tabs(["📖 Real Guide & Steps", "🎥 Video Tutorial", "🎮 Interactive Quiz Challenge"])
        
        with tab1:
            st.markdown("""
            ### Anatomy of a Great Resume:
            * **Contact Header:** Full name, clean professional email, mobile phone number.
            * **Professional Summary:** 2–3 sentences highlighting your strong work ethic and goal.
            * **Work / Practical Experience:** Action-oriented bullet points starting with verbs like *Managed*, *Created*, *Supported*.
            * **Education & Skills:** Technical certifications, languages, and core soft skills.
            """)
            
        with tab2:
            st.write("#### Demonstration Video")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")
            
        with tab3:
            st.subheader("🎮 Skill Challenge: Resume Mastery")
            
            rq1 = st.radio(
                "Question 1: Which of the following is the most professional email address format?",
                ["cool_gamer99@gmail.com", "first.last@email.com", "unknown_user_123@yahoo.com"],
                key="r_q1"
            )
            
            rq2 = st.radio(
                "Question 2: Bullet points in your experience section should start with...",
                ["Strong action verbs", "The word 'I'", "Random adjectives", "Dates only"],
                key="r_q2"
            )
            
            if st.button("Submit Resume Quiz 🚀"):
                r_score = 0
                if rq1 == "first.last@email.com":
                    r_score += 50
                if rq2 == "Strong action verbs":
                    r_score += 50
                
                if r_score == 100:
                    st.balloons()
                    st.success(f"🏆 Perfect Score: {r_score}/100! You are ready to build top resumes!")
                else:
                    st.warning(f" Score: {r_score}/100. Check the guide tab to review!")

    # TRACK 3
    elif category == "📊 Excel & Spreadsheets Essentials":
        st.subheader("📊 Excel & Spreadsheets Essentials")
        
        tab1, tab2, tab3 = st.tabs(["📖 Real Guide & Steps", "🎥 Video Tutorial", "🎮 Interactive Quiz Challenge"])
        
        with tab1:
            st.markdown("""
            ### Essential Formulas & Functions:
            * `=SUM(A1:A10)` — Adds all numbers in cells A1 through A10.
            * `=AVERAGE(B1:B5)` — Calculates the mean value of cells B1 through B5.
            * **Columns** run vertically (A, B, C) while **Rows** run horizontally (1, 2, 3).
            """)
            
        with tab2:
            st.write("#### Demonstration Video")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")
            
        with tab3:
            st.subheader("🎮 Skill Challenge: Spreadsheet Math")
            
            eq1 = st.radio(
                "Question 1: Which formula adds values together in cells A1 through A5?",
                ["=TOTAL(A1:A5)", "=SUM(A1:A5)", "=ADD(A1:A5)"],
                key="e_q1"
            )
            
            if st.button("Submit Excel Quiz 🚀"):
                if eq1 == "=SUM(A1:A5)":
                    st.balloons()
                    st.success("🏆 Correct! `=SUM(A1:A5)` is the standard addition function!")
                else:
                    st.error("Incorrect formula. Remember all math operations in Excel use =SUM()!")

# 6. PAGE 4: SELF-ASSESSMENT & ROADMAP
elif page == "📝 Self-Assessment & Roadmap":
    st.title("📝 Self-Assessment & Roadmap Generator")
    st.write("Test your readiness and generate a custom step-by-step learning path.")
    
    st.subheader("Step 1: Your Info")
    user_name = st.text_input("Enter your name:", placeholder="e.g., Student")
    selected_track = st.selectbox(
        "Select target learning area:", 
        ["Digital Literacy", "Resume & Writing", "Office Tools"]
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
