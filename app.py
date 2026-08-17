import streamlit as st
import requests

# 1. Page Setup & Configuration
st.set_page_config(
    page_title="SkillsPulse - Essential Skills Academy",
    page_icon="📚",
    layout="wide"
)

# 2. Session State for Page Navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 Home Dashboard"

if "selected_module" not in st.session_state:
    st.session_state.selected_module = "💻 Basic Computer Literacy & Keyboard Mastery"

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
nav_choice = st.sidebar.radio(
    "Go to section:",
    [
        "🏠 Home Dashboard", 
        "🤖 SkillsPulse AI Assistant", 
        "📚 Learning Modules & Practical Lab", 
        "📝 Self-Assessment & Roadmap", 
        "ℹ️ About Platform"
    ],
    index=[
        "🏠 Home Dashboard", 
        "🤖 SkillsPulse AI Assistant", 
        "📚 Learning Modules & Practical Lab", 
        "📝 Self-Assessment & Roadmap", 
        "ℹ️ About Platform"
    ].index(st.session_state.current_page)
)

st.session_state.current_page = nav_choice

HERO_IMAGE_URL = "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=800&auto=format&fit=crop"

# ---------------------------------------------------------
# 3. PAGE 1: HOME DASHBOARD
# ---------------------------------------------------------
if st.session_state.current_page == "🏠 Home Dashboard":
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
        st.metric(label="Active Modules", value="3 Practical Labs")
    with col2:
        st.metric(label="Difficulty Level", value="Beginner Friendly")
    with col3:
        st.metric(label="Interactive Tools", value="Hands-on Exercises")
    with col4:
        st.metric(label="Access Cost", value="100% Free")

    st.write("---")
    st.subheader("💡 Launch Learning Tracks Directly")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.success("**💻 Digital & Computer Literacy**\n\nMaster file management, operating system navigation, web search techniques, and shortcut commands.")
        if st.button("▶ Open Computer Literacy Lab"):
            st.session_state.selected_module = "💻 Basic Computer Literacy & Keyboard Mastery"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

    with c2:
        st.info("**📄 Resume & Email Writing**\n\nLearn step-by-step resume layout, professional summary drafting, and cover letter formatting.")
        if st.button("▶ Open Writing Lab"):
            st.session_state.selected_module = "📄 Professional Writing & Resume Building"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

    with c3:
        st.warning("**📊 Office Tools & Excel Math**\n\nMaster spreadsheet data entry, cell formatting, SUM/AVERAGE formulas, and basic charts.")
        if st.button("▶ Open Excel Lab"):
            st.session_state.selected_module = "📊 Excel & Spreadsheets Essentials"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

# ---------------------------------------------------------
# 4. PAGE 2: AI CHATBOT ASSISTANT
# ---------------------------------------------------------
elif st.session_state.current_page == "🤖 SkillsPulse AI Assistant":
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

# ---------------------------------------------------------
# 5. PAGE 3: LEARNING MODULES & PRACTICAL LAB
# ---------------------------------------------------------
elif st.session_state.current_page == "📚 Learning Modules & Practical Lab":
    st.title("📚 Interactive Learning Modules & Practical Lab")
    st.write("Explore comprehensive guides, watch video lessons, and complete interactive practice exercises.")
    
    category = st.selectbox(
        "Select Active Track:",
        [
            "💻 Basic Computer Literacy & Keyboard Mastery",
            "📄 Professional Writing & Resume Building",
            "📊 Excel & Spreadsheets Essentials"
        ],
        index=[
            "💻 Basic Computer Literacy & Keyboard Mastery",
            "📄 Professional Writing & Resume Building",
            "📊 Excel & Spreadsheets Essentials"
        ].index(st.session_state.selected_module)
    )
    
    st.session_state.selected_module = category
    st.divider()
    
    # -----------------------------------------------------
    # TRACK 1: COMPUTER LITERACY
    # -----------------------------------------------------
    if category == "💻 Basic Computer Literacy & Keyboard Mastery":
        st.subheader("💻 Basic Computer Literacy & Keyboard Mastery")
        
        tab1, tab2, tab3 = st.tabs(["📖 In-Depth Guide", "🎥 Video Lesson", "✍️ Interactive Practical Lab"])
        
        with tab1:
            st.markdown("""
            ### Complete Computer Fundamentals Guide
            
            #### 1. Digital File System & Hierarchy
            Computers organize information like physical filing cabinets:
            * **Drives (C: / D:)**: Storage hardware holding your operating system and files.
            * **Folders (Directories)**: Containers used to group related files together.
            * **Files**: Individual documents, images, audio, or programs.
            * **Best Practice**: Create clear paths, e.g., `Documents / SkillsPulse / Module_1 / Practice.txt`.
            
            #### 2. Essential System Keyboard Shortcuts
            Using shortcuts drastically increases your productivity speed:
            * **`Ctrl + C`**: Copy selected text or file without removing original.
            * **`Ctrl + X`**: Cut selected text or file (moves it).
            * **`Ctrl + V`**: Paste copied or cut items to current location.
            * **`Ctrl + Z`**: Undo the previous action immediately.
            * **`Ctrl + S`**: Save your current document instantly.
            * **`Alt + Tab`**: Fast-switch between open applications.
            * **`Windows Key + D`**: Minimize everything and show desktop.

            #### 3. Web Navigation & Internet Safety
            * **URL Structure**: `https://` indicates a secure, encrypted connection.
            * **Downloads**: Always inspect file extensions (`.pdf`, `.docx` are standard; avoid unexpected `.exe` or `.bat` downloads).
            * **Browser Tabs**: Use `Ctrl + T` to open new tabs and `Ctrl + W` to close tabs.
            """)
            
        with tab2:
            st.write("#### Video Lesson: Windows 10/11 & Computer Basics")
            # Embed-friendly computer tutorial video
            st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")
            
        with tab3:
            st.subheader("✍️ Practical Typing Exercise: Keyboard Shortcut Simulator")
            st.write("Type the correct key combination for each prompt below:")
            
            sc1 = st.text_input("1. What keys do you press to PASTE copied text?", placeholder="e.g. Ctrl + V")
            sc2 = st.text_input("2. What keys do you press to UNDO a mistake?", placeholder="e.g. Ctrl + Z")
            sc3 = st.text_input("3. What keys do you press to SAVE a file?", placeholder="e.g. Ctrl + S")
            
            if st.button("Check Shortcut Answers 🚀"):
                score = 0
                if sc1.strip().lower().replace(" ", "") == "ctrl+v":
                    score += 33
                if sc2.strip().lower().replace(" ", "") == "ctrl+z":
                    score += 33
                if sc3.strip().lower().replace(" ", "") == "ctrl+s":
                    score += 34
                
                if score >= 90:
                    st.balloons()
                    st.success(f"🏆 Excellent! You scored {score}% on your shortcut typing lab!")
                else:
                    st.warning(f"You scored {score}%. Double check your answers (Example format: Ctrl + V) and try again.")

    # -----------------------------------------------------
    # TRACK 2: RESUME & WRITING
    # -----------------------------------------------------
    elif category == "📄 Professional Writing & Resume Building":
        st.subheader("📄 Professional Writing & Resume Building")
        
        tab1, tab2, tab3 = st.tabs(["📖 In-Depth Guide", "🎥 Video Lesson", "✍️ Interactive Practical Lab"])
        
        with tab1:
            st.markdown("""
            ### Professional Resume & Communication Blueprint
            
            #### 1. Structural Resume Anatomy
            * **Header Section**: Full name, location (City, Country), phone number, professional email address (`firstname.lastname@email.com`).
            * **Professional Summary**: A focused 2-3 sentence overview highlighting key skills, character traits, and career goals.
            * **Experience Section**: Reverse-chronological list of jobs or voluntary work using strong action verbs (*Managed*, *Developed*, *Organized*, *Coordinated*).
            * **Education & Certifications**: Name of institution, degree/certificate, and graduation year.
            
            #### 2. Professional Email Communication
            * **Subject Line**: Direct and clear (e.g., `Job Application - Software Specialist - Jane Doe`).
            * **Salutation**: Formal greeting (`Dear Hiring Manager,` or `Dear Mr./Ms. Smith,`).
            * **Body**: State purpose in paragraph 1, detail relevant qualifications in paragraph 2.
            * **Sign-off**: Professional closing (`Sincerely,` or `Best regards,`) followed by full contact details.
            """)
            
        with tab2:
            st.write("#### Video Lesson: How to Write a Resume")
            st.video("https://www.youtube.com/watch?v=ttWk4n0edgg")
            
        with tab3:
            st.subheader("✍️ Practical Workshop: Resume Summary Builder")
            st.write("Draft your professional summary below following this template formula:")
            st.info("Formula: [Adjective/Trait] [Current Role/Field] with experience in [Key Skill 1] and [Key Skill 2]. Seeking to leverage skills to achieve [Career Goal].")
            
            user_summary = st.text_area(
                "Write your 2-3 sentence Professional Summary here:",
                height=120,
                placeholder="Example: Motivated administrative assistant with 2 years of experience managing office schedules and coordinating digital files. Seeking to apply strong organizational skills to support team productivity."
            )
            
            if st.button("Analyze My Summary 📝"):
                if len(user_summary.strip()) < 40:
                    st.warning("Your summary is a bit short! Try adding more details about your skills or goals.")
                else:
                    st.balloons()
                    st.success("Great job drafting your summary! Here is your formatted preview:")
                    st.markdown(f"> **PROFESSIONAL SUMMARY**\n> {user_summary}")

    # -----------------------------------------------------
    # TRACK 3: EXCEL & SPREADSHEETS
    # -----------------------------------------------------
    elif category == "📊 Excel & Spreadsheets Essentials":
        st.subheader("📊 Excel & Spreadsheets Essentials")
        
        tab1, tab2, tab3 = st.tabs(["📖 In-Depth Guide", "🎥 Video Lesson", "✍️ Interactive Practical Lab"])
        
        with tab1:
            st.markdown("""
            ### Complete Spreadsheet Essentials
            
            #### 1. Interface Navigation
            * **Columns**: Run vertically and are labeled with Letters (`A`, `B`, `C`).
            * **Rows**: Run horizontally and are labeled with Numbers (`1`, `2`, `3`).
            * **Cells**: The intersection of a column and row (e.g., `B4`).
            
            #### 2. Core Mathematical Formulas
            All formulas in Excel **MUST start with an equals sign (`=`)**:
            * **Addition**: `=SUM(A1:A10)` — Adds all numeric values from cell A1 through A10.
            * **Average**: `=AVERAGE(B1:B20)` — Calculates the mathematical mean of B1 through B20.
            * **Counting**: `=COUNT(C1:C10)` — Counts total cells containing numbers.
            * **Subtractions & Multiplication**: `=A1 - B1` or `=A1 * B1`.
            """)
            
        with tab2:
            st.write("#### Video Lesson: Beginners Excel Course")
            st.video("https://www.youtube.com/watch?v=rwbho0CgEAE")
            
        with tab3:
            st.subheader("✍️ Practical Workshop: Excel Formula Calculator")
            st.write("Practice typing real Excel formulas based on the sample table below:")
            
            # Display sample data table
            st.table({
                "Cell": ["A1", "A2", "A3", "A4"],
                "Item Name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
                "Cost ($)": [800, 20, 50, 150]
            })
            
            f1 = st.text_input("1. Type the exact formula to ADD ALL COSTS from cell C1 to C4:", placeholder="e.g. =SUM(C1:C4)")
            f2 = st.text_input("2. Type the formula to find the AVERAGE cost from C1 to C4:", placeholder="e.g. =AVERAGE(C1:C4)")
            
            if st.button("Run Formula Check 🧪"):
                score = 0
                if f1.strip().upper().replace(" ", "") == "=SUM(C1:C4)":
                    score += 50
                if f2.strip().upper().replace(" ", "") == "=AVERAGE(C1:C4)":
                    score += 50
                    
                if score == 100:
                    st.balloons()
                    st.success("🏆 Perfect! `=SUM(C1:C4)` totals $1,020 and `=AVERAGE(C1:C4)` calculates $255 average!")
                else:
                    st.warning(f"Score: {score}/100. Make sure you start with '=' and use uppercase range parameters like =SUM(C1:C4).")

# ---------------------------------------------------------
# 6. PAGE 4: SELF-ASSESSMENT & ROADMAP
# ---------------------------------------------------------
elif st.session_state.current_page == "📝 Self-Assessment & Roadmap":
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
            1. **Week 1:** Complete Module A fundamentals and practical typing exercises.
            2. **Week 2:** Complete sample drafting in your writing/Excel practical lab.
            3. **Week 3:** Practice with the AI tutor assistant to review concepts.
            """)

# ---------------------------------------------------------
# 7. PAGE 5: ABOUT PLATFORM
# ---------------------------------------------------------
elif st.session_state.current_page == "ℹ️ About Platform":
    st.title("ℹ️ About SkillsPulse")
    st.write("SkillsPulse is designed to make practical skill learning accessible, structured, and straightforward for everyone.")
    st.write("Designed for class presentations and practical skill demonstration.")

st.divider()
st.caption("SkillsPulse Platform — All-in-One Practical Learning Dashboard")
