import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(
    page_title="SkillsPulse - Essential Skills Academy",
    page_icon="📚",
    layout="wide"
)

# Custom High-End Styling
st.markdown("""
    <style>
    /* Main Theme Styling */
    .stApp {
        background-color: #0e1117;
    }
    .main-header {
        background: linear-gradient(90deg, #1f2937 0%, #111827 100%);
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #374151;
        margin-bottom: 2rem;
        text-align: center;
    }
    .talent-card {
        background-color: #1f2937;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
        margin-bottom: 1rem;
    }
    .metric-container {
        background-color: #111827;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #374151;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Global State Management
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 Home Dashboard"

if "selected_module" not in st.session_state:
    st.session_state.selected_module = "💻 Computer Literacy"

if "verified_student" not in st.session_state:
    st.session_state.verified_student = False

# Sample Talent Database
if "talent_pool" not in st.session_state:
    st.session_state.talent_pool = [
        {"name": "Alex Morgan", "track": "Computer Literacy (Excel Focus)", "score": "98%", "skills": ["Excel Formulas", "VLOOKUP", "Pivot Tables", "Word Drafting"], "status": "Verified"},
        {"name": "David Chen", "track": "Business Analytics & Data Visualization", "score": "95%", "skills": ["Data Visualization", "Dashboards", "Excel", "KPI Tracking"], "status": "Verified"},
        {"name": "Sarah Jenkins", "track": "Cybersecurity & Online Safety", "score": "92%", "skills": ["Phishing Defense", "Password Hygiene", "Encryption Protocols"], "status": "Verified"},
        {"name": "Grace Uwase", "track": "Web & Digital Marketing Fundamentals", "score": "96%", "skills": ["SEO", "Content Strategy", "PPC Campaigns"], "status": "Verified"}
    ]

# Sidebar Navigation
st.sidebar.title("📌 SkillsPulse Menu")
nav_choice = st.sidebar.radio(
    "Go to section:",
    [
        "🏠 Home Dashboard", 
        "🤖 SkillsPulse AI Assistant", 
        "📚 Learning Modules & Practical Lab", 
        "📸 Student Identity & Camera Proctoring",
        "🏢 Investor & Business Talent Portal",
        "📝 Self-Assessment & Roadmap", 
        "ℹ️ About Platform"
    ],
    index=[
        "🏠 Home Dashboard", 
        "🤖 SkillsPulse AI Assistant", 
        "📚 Learning Modules & Practical Lab", 
        "📸 Student Identity & Camera Proctoring",
        "🏢 Investor & Business Talent Portal",
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
    st.markdown("""
        <div class="main-header">
            <h1 style="color: #f3f4f6; margin-bottom: 0.5rem;">📚 SkillsPulse: Essential Skills Academy</h1>
            <p style="color: #9ca3af; font-size: 1.1rem;">An interactive, high-impact learning suite and talent ecosystem built for workforce readiness.</p>
        </div>
    """, unsafe_allow_html=True)
    
    try:
        st.image(HERO_IMAGE_URL, caption="Practical Digital Literacy & Talent Ecosystem", use_container_width=True)
    except:
        st.info("Image loading...")
        
    st.divider()
    
    st.header("⚡ Platform Metrics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Active Courses", value="8 Modules")
    with col2:
        st.metric(label="Core Focus", value="Word, Excel, PPT")
    with col3:
        st.metric(label="Proctor Security", value="Active Camera Guard")
    with col4:
        st.metric(label="Talent Portal", value="Investor Ready")

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

    elif category == "🤝 Communication & Workplace Collaboration":
        st.subheader("🤝 Communication & Workplace Collaboration")
        tab1, tab2 = st.tabs(["📖 In-Depth Guide", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("### Workplace Communication\nFocus on email formatting, active listening, and conflict management.")
        with tab2:
            st.video("https://www.youtube.com/watch?v=R3abknwWX7k")

    elif category == "💼 Financial Literacy & Budgeting":
        st.subheader("💼 Financial Literacy & Budgeting")
        tab1, tab2 = st.tabs(["📖 In-Depth Guide", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("### Budgeting Essentials\nUnderstand the 50/30/20 framework and income statement tracking.")
        with tab2:
            st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")

    elif category == "🚀 Critical Thinking & Problem Solving":
        st.subheader("🚀 Critical Thinking & Problem Solving")
        tab1, tab2 = st.tabs(["📖 In-Depth Guide", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("### Structured Problem Solving\nApply the 5 Whys and SWOT Analysis frameworks.")
        with tab2:
            st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")

    elif category == "🌐 Web & Digital Marketing Fundamentals":
        st.subheader("🌐 Web & Digital Marketing Fundamentals")
        tab1, tab2 = st.tabs(["📖 In-Depth Manual", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("### Digital Marketing Strategy\nFocus on SEO, PPC, and content conversion funnels.")
        with tab2:
            st.video("https://www.youtube.com/watch?v=k1VUZEVuDJ8")

    elif category == "🛡️ Cybersecurity & Online Safety":
        st.subheader("🛡️ Cybersecurity & Online Safety")
        tab1, tab2 = st.tabs(["📖 In-Depth Manual", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("### Digital Security Principles\nPhishing defense, password security, and SSL encryption.")
        with tab2:
            st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")

    elif category == "🛠️ Basic Practical Trades & Technical Maintenance":
        st.subheader("🛠️ Basic Practical Trades & Technical Maintenance")
        tab1, tab2 = st.tabs(["📖 In-Depth Manual", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("### Technical Maintenance\nWorkplace safety protocols, PPE compliance, and tool diagnostics.")
        with tab2:
            st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")

    elif category == "📊 Business Analytics & Data Visualization":
        st.subheader("📊 Business Analytics & Data Visualization")
        tab1, tab2 = st.tabs(["📖 In-Depth Manual", "🎥 Video Tutorials"])
        with tab1:
            st.markdown("### Data Visualization Fundamentals\nSelecting chart types, data cleaning, and tracking KPIs.")
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
# 7. NEW PAGE 5: INVESTOR & BUSINESS TALENT PORTAL
# ---------------------------------------------------------
elif st.session_state.current_page == "🏢 Investor & Business Talent Portal":
    st.title("🏢 Investor & Business Talent Matching Portal")
    st.write("Connecting verified SkillsPulse graduates with businesses and investors seeking skilled talent.")

    tab_search, tab_post = st.tabs(["🔍 Search Verified Talent", "📋 Post a Business Job Requirement"])

    with tab_search:
        st.subheader("Match Skills to Verified Graduates")
        col_a, col_b = st.columns(2)
        with col_a:
            search_track = st.selectbox(
                "Filter by Primary Competency Track:",
                [
                    "All Tracks",
                    "Computer Literacy (Excel Focus)",
                    "Business Analytics & Data Visualization",
                    "Cybersecurity & Online Safety",
                    "Web & Digital Marketing Fundamentals"
                ]
            )
        with col_b:
            search_skill = st.text_input("Filter by Specific Skill Keyword:", placeholder="e.g. Excel Formulas, SEO, Phishing")

        st.divider()
        st.subheader("Available Qualified Candidates")

        for person in st.session_state.talent_pool:
            if search_track == "All Tracks" or search_track in person["track"]:
                if not search_skill or any(search_skill.lower() in s.lower() for s in person["skills"]):
                    st.markdown(f"""
                        <div class="talent-card">
                            <h3 style="color: #60a5fa; margin-bottom: 0.2rem;">👤 {person['name']} <span style="color: #34d399; font-size: 0.9rem;">({person['status']})</span></h3>
                            <p style="color: #d1d5db; margin-bottom: 0.5rem;"><strong>Primary Specialization:</strong> {person['track']} | <strong>Course Score:</strong> {person['score']}</p>
                            <p style="color: #9ca3af; margin-bottom: 0.5rem;"><strong>Verified Skills:</strong> {', '.join(person['skills'])}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"📩 Request Contact Info for {person['name']}", key=person['name']):
                        st.success(f"Contact request logged for {person['name']}. An automated connection email will be sent to your registered business address.")

    with tab_post:
        st.subheader("Post a Role & Find Automated Matches")
        st.write("Businesses and investors can define specific role requirements to auto-match with our talent pool.")

        company_name = st.text_input("Company / Investor Name:", placeholder="e.g. Horizon Capital")
        role_title = st.text_input("Job / Internship Title:", placeholder="e.g. Junior Data Analyst")
        required_track = st.selectbox(
            "Required Primary Skills Track:",
            [
                "Computer Literacy (Excel Focus)",
                "Business Analytics & Data Visualization",
                "Cybersecurity & Online Safety",
                "Web & Digital Marketing Fundamentals"
            ]
        )
        required_skills = st.text_area("List Required Skills (separated by commas):", placeholder="e.g. Excel, VLOOKUP, Data Visualization")

        if st.button("Submit Role & Run Talent Match 🚀"):
            if company_name and role_title:
                st.balloons()
                st.success(f"Job posting for '{role_title}' at {company_name} submitted successfully!")
                
                # Match Logic
                matches = [p for p in st.session_state.talent_pool if p["track"] == required_track]
                st.write(f"### 🎯 Found {len(matches)} High-Match Candidates:")
                for m in matches:
                    st.info(f"**Candidate:** {m['name']} | **Assessment Score:** {m['score']} | **Skills:** {', '.join(m['skills'])}")
            else:
                st.error("Please fill in company name and role title.")

# ---------------------------------------------------------
# 8. PAGE 6: SELF-ASSESSMENT & ROADMAP
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
            4. **Week 4:** Publish profile to the Investor & Business Talent Portal.
            """)

# ---------------------------------------------------------
# 9. PAGE 7: ABOUT PLATFORM
# ---------------------------------------------------------
elif st.session_state.current_page == "ℹ️ About Platform":
    st.title("ℹ️ About SkillsPulse Academy")
    st.write("SkillsPulse is an integrated learning management environment focused on practical digital literacy, workforce development, and direct talent placement for businesses and investors.")

st.divider()
st.caption("SkillsPulse Platform — All-in-One Practical Learning & Talent Ecosystem")
