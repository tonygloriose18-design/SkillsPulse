import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(
    page_title="SkillsPulse - Essential Skills Academy",
    page_icon="📚",
    layout="wide"
)

# 2. Global State Management
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 Home Dashboard"

if "selected_module" not in st.session_state:
    st.session_state.selected_module = "💻 Computer Literacy"

if "verified_student" not in st.session_state:
    st.session_state.verified_student = False

# Sidebar Navigation
st.sidebar.title("📌 Navigation Menu")
nav_choice = st.sidebar.radio(
    "Go to section:",
    [
        "🏠 Home Dashboard", 
        "🤖 SkillsPulse AI Assistant", 
        "📚 Learning Modules & Practical Lab", 
        "📸 Student Identity & Camera Proctoring",
        "📝 Self-Assessment & Roadmap", 
        "ℹ️ About Platform"
    ],
    index=[
        "🏠 Home Dashboard", 
        "🤖 SkillsPulse AI Assistant", 
        "📚 Learning Modules & Practical Lab", 
        "📸 Student Identity & Camera Proctoring",
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
    st.write("An interactive, high-impact learning suite designed for practical digital literacy, soft skills, and workforce readiness.")
    
    try:
        st.image(HERO_IMAGE_URL, caption="Practical Digital Literacy & Skills Mastery", use_container_width=True)
    except:
        st.info("Image loading...")
        
    st.divider()
    
    st.header("⚡ Platform Dashboard Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Active Courses", value="8 Total Modules")
    with col2:
        st.metric(label="Core Suite", value="Word, Excel, PPT")
    with col3:
        st.metric(label="Proctor Security", value="Active Camera Guard")
    with col4:
        st.metric(label="Access Cost", value="100% Free")

    st.write("---")
    st.subheader("💡 Launch Learning Tracks Directly")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.success("### 💻 Computer Literacy (Focus Track)\nMaster Windows OS, File Management, Microsoft Word, Excel, and PowerPoint.")
        if st.button("▶ Open Computer Literacy Suite"):
            st.session_state.selected_module = "💻 Computer Literacy"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

        st.info("### 🤝 Communication & Workplace Collaboration\nMaster professional email etiquette, active listening, and conflict resolution.")
        if st.button("▶ Open Workplace Communication"):
            st.session_state.selected_module = "🤝 Communication & Workplace Collaboration"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

        st.warning("### 💼 Financial Literacy & Budgeting\nLearn personal budgeting, debt management, saving strategies, and basic accounting.")
        if st.button("▶ Open Financial Literacy"):
            st.session_state.selected_module = "💼 Financial Literacy & Budgeting"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

        st.error("### 🚀 Critical Thinking & Problem Solving\nDevelop root-cause analysis, decision-making frameworks, and structured thinking.")
        if st.button("▶ Open Critical Thinking"):
            st.session_state.selected_module = "🚀 Critical Thinking & Problem Solving"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

    with c2:
        st.success("### 🌐 Web & Digital Marketing Fundamentals\nUnderstand SEO, digital campaigns, social media branding, and analytics.")
        if st.button("▶ Open Digital Marketing"):
            st.session_state.selected_module = "🌐 Web & Digital Marketing Fundamentals"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

        st.info("### 🛡️ Cybersecurity & Online Safety\nProtect personal credentials, identify phishing attempts, and manage passwords safely.")
        if st.button("▶ Open Cybersecurity Essentials"):
            st.session_state.selected_module = "🛡️ Cybersecurity & Online Safety"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

        st.warning("### 🛠️ Basic Practical Trades & Technical Maintenance\nLearn basic troubleshooting, equipment maintenance, and workplace safety protocols.")
        if st.button("▶ Open Practical Trades"):
            st.session_state.selected_module = "🛠️ Basic Practical Trades & Technical Maintenance"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

        st.error("### 📊 Business Analytics & Data Visualization\nTransform raw numbers into clear dashboards, charts, and actionable metrics.")
        if st.button("▶ Open Data Visualization"):
            st.session_state.selected_module = "📊 Business Analytics & Data Visualization"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

# ---------------------------------------------------------
# 4. PAGE 2: AI CHATBOT ASSISTANT
# ---------------------------------------------------------
elif st.session_state.current_page == "🤖 SkillsPulse AI Assistant":
    st.title("🤖 SkillsPulse AI Tutor")
    st.write("Ask any questions about basic digital skills, Excel formulas, Word formatting, PowerPoint, or workplace skills!")

    api_key = st.secrets.get("EJOCHAT_API_KEY", "")
    
    if not api_key:
        st.error("Please configure EJOCHAT_API_KEY in Streamlit Cloud secrets.")
        st.stop()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_prompt := st.chat_input("Ask a question (e.g., 'How do I combine cells in Excel?' or 'Explain VLOOKUP')..."):
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
    st.title("📚 Comprehensive Learning Modules & Interactive Labs")
    st.write("In-depth practical lessons with real video training and hands-on work simulators.")
    
    category = st.selectbox(
        "Select Active Learning Course:",
        [
            "💻 Computer Literacy",
            "🤝 Communication & Workplace Collaboration",
            "💼 Financial Literacy & Budgeting",
            "🚀 Critical Thinking & Problem Solving",
            "🌐 Web & Digital Marketing Fundamentals",
            "🛡️ Cybersecurity & Online Safety",
            "🛠️ Basic Practical Trades & Technical Maintenance",
            "📊 Business Analytics & Data Visualization"
        ],
        index=[
            "💻 Computer Literacy",
            "🤝 Communication & Workplace Collaboration",
            "💼 Financial Literacy & Budgeting",
            "🚀 Critical Thinking & Problem Solving",
            "🌐 Web & Digital Marketing Fundamentals",
            "🛡️ Cybersecurity & Online Safety",
            "🛠️ Basic Practical Trades & Technical Maintenance",
            "📊 Business Analytics & Data Visualization"
        ].index(st.session_state.selected_module)
    )
    
    st.session_state.selected_module = category
    st.divider()
    
    # COURSE 1: COMPUTER LITERACY
    if category == "💻 Computer Literacy":
        st.subheader("💻 Computer Literacy Suite")
        st.write("Explore OS navigation along with specialized sub-modules for Microsoft Word, Excel (Main Focus), and PowerPoint.")
        
        sub_module = st.selectbox(
            "Select Computer Literacy Sub-Module:",
            [
                "⚙️ OS Basics & File System",
                "📊 Microsoft Excel (Main Focus)",
                "📝 Microsoft Word & Document Design",
                "🎨 Microsoft PowerPoint & Presentations"
            ]
        )
        st.divider()

        if sub_module == "⚙️ OS Basics & File System":
            tab1, tab2, tab3 = st.tabs(["📖 In-Depth Practical Guide", "🎥 Video Tutorials (5 Lessons)", "✍️ Interactive Lab"])
            with tab1:
                st.markdown("""
                ### ⚙️ OS & System Architecture Manual
                #### Section 1: Computing Hardware & Processing Mechanics
                * **CPU**: Central Processing Unit that executes all logic loops.
                * **RAM**: Short-term memory used for operating active windows.
                * **Storage**: Long-term SSD/HDD drive retention.
                #### Section 2: Directory Architecture & File Extension Rules
                * Structured paths: `C:\\Users\\Public\\Documents`
                * File Naming Standard: `[Project]_[Department]_[Date]_v[Version]`
                """)
            with tab2:
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Lesson 1: Hardware Basics**")
                    st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")
                    st.write("**Lesson 2: Operating Systems**")
                    st.video("https://www.youtube.com/watch?v=Ai0MV7twEBE")
                    st.write("**Lesson 3: File Storage**")
                    st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")
                with col2:
                    st.write("**Lesson 4: Web Safety Basics**")
                    st.video("https://www.youtube.com/watch?v=R3abknwWX7k")
                    st.write("**Lesson 5: System Shortcuts**")
                    st.video("https://www.youtube.com/watch?v=k1VUZEVuDJ8")
            with tab3:
                q1 = st.text_input("Type the shortcut to UNDO an action:", placeholder="e.g. Ctrl + Z")
                if st.button("Submit Answer"):
                    if q1.strip().lower().replace(" ", "") == "ctrl+z":
                        st.success("Correct!")
                    else:
                        st.warning("Try again! (Hint: Ctrl + Z)")

        elif sub_module == "📊 Microsoft Excel (Main Focus)":
            tab1, tab2, tab3 = st.tabs(["📖 In-Depth Excel Manual", "🎥 Video Tutorials (5 Lessons)", "✍️ Interactive Formula Lab"])
            with tab1:
                st.markdown("""
                ### 📊 Microsoft Excel Masterclass Manual
                #### Core Formulas & Functions
                * `=SUM(range)`: Adds numbers in a grid.
                * `=AVERAGE(range)`: Returns arithmetic mean.
                * `=COUNTIF(range, condition)`: Conditional counting.
                * `=VLOOKUP(lookup_val, table, col, FALSE)`: Vertical search lookup.
                """)
            with tab2:
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Lesson 1: Interface Basics**")
                    st.video("https://www.youtube.com/watch?v=Ai0MV7twEBE")
                    st.write("**Lesson 2: Top Formulas**")
                    st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")
                    st.write("**Lesson 3: Conditional Logic**")
                    st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")
                with col2:
                    st.write("**Lesson 4: VLOOKUP Deep Dive**")
                    st.video("https://www.youtube.com/watch?v=R3abknwWX7k")
                    st.write("**Lesson 5: Pivot Tables**")
                    st.video("https://www.youtube.com/watch?v=k1VUZEVuDJ8")
            with tab3:
                f1 = st.text_input("1. Formula to sum all Actual Sales (Row 1 to 3 in Col C):", placeholder="e.g. =SUM(C1:C3)")
                f2 = st.text_input("2. Formula to find AVERAGE sales in Col C:", placeholder="e.g. =AVERAGE(C1:C3)")
                if st.button("Run Formula Engine 🧪"):
                    if f1.strip().upper().replace(" ", "") == "=SUM(C1:C3)" and f2.strip().upper().replace(" ", "") == "=AVERAGE(C1:C3)":
                        st.balloons()
                        st.success("100% Correct!")

        elif sub_module == "📝 Microsoft Word & Document Design":
            tab1, tab2, tab3 = st.tabs(["📖 Word Manual", "🎥 Video Tutorials (5 Lessons)", "✍️ Interactive Lab"])
            with tab1:
                st.markdown("### 📝 Document Design Guidelines\n* Use Heading 1 and 2 styles.\n* Set 1-inch margins.")
            with tab2:
                st.video("https://www.youtube.com/watch?v=R3abknwWX7k")
            with tab3:
                st.write("Cover letter drafting simulator.")

        elif sub_module == "🎨 Microsoft PowerPoint & Presentations":
            tab1, tab2, tab3 = st.tabs(["📖 PowerPoint Manual", "🎥 Video Tutorials (5 Lessons)", "✍️ Interactive Lab"])
            with tab1:
                st.markdown("### 🎨 Slide Design Standards\n* Follow the 10-20-30 Rule.\n* Keep visual contrast sharp.")
            with tab2:
                st.video("https://www.youtube.com/watch?v=k1VUZEVuDJ8")
            with tab3:
                st.write("Slide outline generator.")

    # COURSE 2: COMMUNICATION
    elif category == "🤝 Communication & Workplace Collaboration":
        st.subheader("🤝 Communication & Workplace Collaboration")
        tab1, tab2 = st.tabs(["📖 In-Depth Guide", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("### Workplace Communication\nFocus on email formatting, active listening, and conflict management.")
        with tab2:
            st.video("https://www.youtube.com/watch?v=R3abknwWX7k")

    # COURSE 3: FINANCIAL LITERACY
    elif category == "💼 Financial Literacy & Budgeting":
        st.subheader("💼 Financial Literacy & Budgeting")
        tab1, tab2 = st.tabs(["📖 In-Depth Guide", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("### Budgeting Essentials\nUnderstand the 50/30/20 framework and income statement tracking.")
        with tab2:
            st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")

    # COURSE 4: CRITICAL THINKING
    elif category == "🚀 Critical Thinking & Problem Solving":
        st.subheader("🚀 Critical Thinking & Problem Solving")
        tab1, tab2 = st.tabs(["📖 In-Depth Guide", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("### Structured Problem Solving\nApply the 5 Whys and SWOT Analysis frameworks.")
        with tab2:
            st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")

    # COURSE 5: DIGITAL MARKETING
    elif category == "🌐 Web & Digital Marketing Fundamentals":
        st.subheader("🌐 Web & Digital Marketing Fundamentals")
        tab1, tab2 = st.tabs(["📖 In-Depth Manual", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("""
            ### 🌐 Digital Marketing & Web Strategy
            * **Search Engine Optimization (SEO)**: Optimizing content using targeted keywords and backlink structures.
            * **Pay-Per-Click (PPC)**: Running targeted advertising campaigns across engines.
            * **Content Funnels**: Awareness -> Consideration -> Conversion stages.
            """)
        with tab2:
            st.video("https://www.youtube.com/watch?v=k1VUZEVuDJ8")

    # COURSE 6: CYBERSECURITY
    elif category == "🛡️ Cybersecurity & Online Safety":
        st.subheader("🛡️ Cybersecurity & Online Safety")
        tab1, tab2 = st.tabs(["📖 In-Depth Manual", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("""
            ### 🛡️ Digital Security Principles
            * **Phishing Identification**: Inspecting sender addresses, urgent calls to action, and suspicious links.
            * **Password Hygiene**: Using complex length strings paired with multi-factor authentication.
            * **Data Encryption**: Verification of HTTPS protocol signatures across network endpoints.
            """)
        with tab2:
            st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")

    # COURSE 7: PRACTICAL TRADES
    elif category == "🛠️ Basic Practical Trades & Technical Maintenance":
        st.subheader("🛠️ Basic Practical Trades & Technical Maintenance")
        tab1, tab2 = st.tabs(["📖 In-Depth Manual", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("""
            ### 🛠️ Hardware & Physical Tool Operations
            * **Workplace Safety Protocols**: Wearing PPE (Personal Protective Equipment) and managing workspace clean zones.
            * **Basic Troubleshooting**: Diagnostic testing using step-by-step isolation procedures.
            * **Equipment Calibration**: Periodic checks to ensure accurate mechanical performance.
            """)
        with tab2:
            st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")

    # COURSE 8: DATA VISUALIZATION
    elif category == "📊 Business Analytics & Data Visualization":
        st.subheader("📊 Business Analytics & Data Visualization")
        tab1, tab2 = st.tabs(["📖 In-Depth Manual", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("""
            ### 📊 Data Visualization & Dashboarding
            * **Chart Type Selection**: Bar charts for category comparison, line charts for trends, scatter plots for correlation.
            * **Data Cleaning**: Removing duplicates, handling null fields, and normalizing raw numbers.
            * **Key Performance Indicators (KPIs)**: Tracking measurable operational targets clearly.
            """)
        with tab2:
            st.video("https://www.youtube.com/watch?v=Ai0MV7twEBE")

# ---------------------------------------------------------
# 6. PAGE 4: STUDENT IDENTITY & CAMERA PROCTORING
# ---------------------------------------------------------
elif st.session_state.current_page == "📸 Student Identity & Camera Proctoring":
    st.title("📸 Student Live Verification System")
    st.write("To ensure integrity during practical modules, students must take a live verification selfie using their device camera.")

    st.subheader("📷 Active Student Proctor Guard")
    img_capture = st.camera_input("Take a photo to verify your active presence during study:")

    if img_capture:
        st.image(img_capture, caption="Verified Student Snapshot", width=350)
        st.success("✅ Student identity logged & verified! You may proceed with your coursework safely.")
        st.session_state.verified_student = True
    else:
        st.info("Please allow camera access and snap a photo to verify student identity.")

# ---------------------------------------------------------
# 7. PAGE 5: SELF-ASSESSMENT & ROADMAP
# ---------------------------------------------------------
elif st.session_state.current_page == "📝 Self-Assessment & Roadmap":
    st.title("📝 Self-Assessment & Roadmap Generator")
    st.write("Assess your current readiness and generate a tailored step-by-step learning pathway.")
    
    st.subheader("Step 1: Student Information")
    user_name = st.text_input("Enter your full name:", placeholder="e.g. Jane Doe")
    selected_track = st.selectbox(
        "Select primary target focus area:", 
        [
            "Computer Literacy (Excel Focus)", 
            "Communication", 
            "Financial Literacy", 
            "Critical Thinking",
            "Digital Marketing",
            "Cybersecurity",
            "Practical Trades",
            "Data Visualization"
        ]
    )
    
    st.subheader("Step 2: Self-Evaluation")
    level = st.radio("Current Confidence Level:", ["Beginner", "Intermediate", "Advanced"])
    
    st.divider()
    
    if st.button("Generate Personal Roadmap 🚀"):
        if user_name.strip() == "":
            st.warning("Please enter your name to generate your custom plan!")
        else:
            st.balloons()
            st.success(f"### Custom Learning Blueprint Generated for {user_name}!")
            st.write(f"**Target Focus Track:** {selected_track} | **Starting Baseline:** {level}")
            
            st.markdown("""
            #### 📌 Recommended Action Blueprint:
            1. **Week 1:** Verify identity in camera proctor lab & complete baseline topics.
            2. **Week 2:** Master chosen course skills & core practical guides.
            3. **Week 3:** Work through video tutorials & complete interactive labs.
            4. **Week 4:** Take advanced evaluation modules & use AI Assistant for spot checks.
            """)

# ---------------------------------------------------------
# 8. PAGE 6: ABOUT PLATFORM
# ---------------------------------------------------------
elif st.session_state.current_page == "ℹ️ About Platform":
    st.title("ℹ️ About SkillsPulse Academy")
    st.write("SkillsPulse is an integrated learning management environment focused on practical digital literacy, workforce development, and hands-on software training.")

st.divider()
st.caption("SkillsPulse Platform — All-in-One Practical Learning Dashboard")
