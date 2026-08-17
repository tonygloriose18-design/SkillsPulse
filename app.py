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

# Sidebar Navigation
st.sidebar.title("📌 Navigation Menu")
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
    st.write("An interactive, high-impact learning suite designed for practical digital literacy, soft skills, and workforce readiness.")
    
    try:
        st.image(HERO_IMAGE_URL, caption="Practical Digital Literacy & Skills Mastery", use_container_width=True)
    except:
        st.info("Image loading...")
        
    st.divider()
    
    st.header("⚡ Platform Dashboard Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Primary Track", value="Computer Literacy")
    with col2:
        st.metric(label="Core Suite", value="Word, Excel, PPT")
    with col3:
        st.metric(label="Interactive Labs", value="Live Code & Text")
    with col4:
        st.metric(label="Access Cost", value="100% Free")

    st.write("---")
    st.subheader("💡 Launch Learning Tracks Directly")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.success("### 💻 Computer Literacy (Focus Track)\nMaster Windows OS, File Management, Microsoft Word, Excel (Deep Dive), and PowerPoint.")
        if st.button("▶ Open Computer Literacy Suite"):
            st.session_state.selected_module = "💻 Computer Literacy"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

        st.info("### 🤝 Communication & Workplace Collaboration\nMaster professional email etiquette, active listening, and conflict resolution.")
        if st.button("▶ Open Workplace Communication"):
            st.session_state.selected_module = "🤝 Communication & Workplace Collaboration"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

    with c2:
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
            "🚀 Critical Thinking & Problem Solving"
        ],
        index=[
            "💻 Computer Literacy",
            "🤝 Communication & Workplace Collaboration",
            "💼 Financial Literacy & Budgeting",
            "🚀 Critical Thinking & Problem Solving"
        ].index(st.session_state.selected_module)
    )
    
    st.session_state.selected_module = category
    st.divider()
    
    # -----------------------------------------------------
    # MAIN COURSE: COMPUTER LITERACY (WITH SUB-COURSES)
    # -----------------------------------------------------
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

        # SUB-MODULE 1: OS BASICS
        if sub_module == "⚙️ OS Basics & File System":
            tab1, tab2, tab3 = st.tabs(["📖 In-Depth Practical Guide", "🎥 Video Tutorial", "✍️ Interactive Lab"])
            
            with tab1:
                st.markdown("""
                ### System Navigation & Desktop Mechanics
                * **CPU vs RAM vs Storage**: Understanding hardware functions.
                * **Folder Management**: Building structured naming conventions (`Category / Year / File_v1`).
                * **Shortcuts**: `Ctrl+C` (Copy), `Ctrl+V` (Paste), `Ctrl+Z` (Undo), `Alt+Tab` (Switch apps).
                """)
            with tab2:
                st.write("#### Video Lesson: Computer Basics for Absolute Beginners")
                st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")
            with tab3:
                st.subheader("✍️ OS Navigation Check")
                q1 = st.text_input("Type the shortcut to UNDO an action:", placeholder="e.g. Ctrl + Z")
                if st.button("Submit Answer"):
                    if q1.strip().lower().replace(" ", "") == "ctrl+z":
                        st.success("Correct!")
                    else:
                        st.warning("Try again! (Hint: Ctrl + Z)")

        # SUB-MODULE 2: MICROSOFT EXCEL (MAIN FOCUS)
        elif sub_module == "📊 Microsoft Excel (Main Focus)":
            tab1, tab2, tab3 = st.tabs(["📖 In-Depth Excel Masterclass", "🎥 Video Tutorial", "✍️ Interactive Formula Lab"])
            
            with tab1:
                st.markdown("""
                ### 📊 Complete Microsoft Excel Masterclass
                
                #### 1. Core Spreadsheet Architecture
                * **Columns (A-XFD)** & **Rows (1-1,048,576)** intersect to form **Cells** (e.g., `B5`).
                * **Workbook**: The whole `.xlsx` file containing multiple **Worksheets**.

                #### 2. Essential Formula & Function Library
                *All Excel formulas MUST start with an equals sign (`=`).*

                * **SUM**: Adds a range of numbers.  
                  * `=SUM(B2:B20)`
                * **AVERAGE**: Calculates arithmetic mean.  
                  * `=AVERAGE(C1:C10)`
                * **COUNT / COUNTA**: Counts numbers vs. non-empty cells.  
                  * `=COUNT(A1:A50)`
                * **IF Logic**: Returns custom values based on conditions.  
                  * `=IF(C2>=5000, "Target Met", "Below Target")`
                * **VLOOKUP**: Searches for a value in the first column and returns data from another column.  
                  * `=VLOOKUP(Lookup_Value, Table_Array, Col_Index_Num, FALSE)`
                * **MAX / MIN**: Finds highest or lowest number in a dataset.  
                  * `=MAX(D1:D100)`

                #### 3. Data Cleaning & Analysis
                * **Format as Table (`Ctrl + T`)**: Adds auto-filtering and sorting.
                * **Pivot Tables**: Summarize huge datasets into meaningful reports (`Insert > PivotTable`).
                """)
            with tab2:
                st.write("#### Video Lesson: Microsoft Excel Complete Tutorial for Beginners")
                st.video("https://www.youtube.com/watch?v=Ai0MV7twEBE")
                st.caption("Video Source: Excel Beginners Step-by-Step Guide by Kevin Stratvert")
            with tab3:
                st.subheader("✍️ Interactive Formula Simulator")
                st.table({
                    "Employee": ["Sarah", "John", "David"],
                    "Sales Goal": [5000, 5000, 5000],
                    "Actual Sales": [6200, 4800, 7100]
                })
                f1 = st.text_input("1. Formula to sum all Actual Sales (Row 1 to 3 in Col C):", placeholder="e.g. =SUM(C1:C3)")
                f2 = st.text_input("2. Formula to find AVERAGE sales in Col C:", placeholder="e.g. =AVERAGE(C1:C3)")
                
                if st.button("Run Formula Engine 🧪"):
                    if f1.strip().upper().replace(" ", "") == "=SUM(C1:C3)" and f2.strip().upper().replace(" ", "") == "=AVERAGE(C1:C3)":
                        st.balloons()
                        st.success("100% Correct! Calculations verified successfully.")
                    else:
                        st.warning("Double check your formulas! Make sure to use =SUM(C1:C3) and =AVERAGE(C1:C3).")

        # SUB-MODULE 3: MICROSOFT WORD
        elif sub_module == "📝 Microsoft Word & Document Design":
            tab1, tab2, tab3 = st.tabs(["📖 Practical Guide", "🎥 Video Tutorial", "✍️ Cover Letter Simulator"])
            
            with tab1:
                st.markdown("""
                ### 📝 Microsoft Word & Document Formatting
                * **Fonts & Margins**: Standard Calibri/Arial 11-12pt, 1-inch margins.
                * **Styles Ribbon**: Use `Heading 1` and `Heading 2` for auto Table of Contents.
                * **Resume Layout**: Reverse chronological structure starting with active verbs.
                """)
            with tab2:
                st.write("#### Video Lesson: How to Write a Professional Resume")
                st.video("https://www.youtube.com/watch?v=R3abknwWX7k")
            with tab3:
                st.subheader("✍️ Cover Letter Builder")
                name = st.text_input("Your Full Name:")
                body = st.text_area("Write a short intro paragraph:")
                if st.button("Generate Document"):
                    if name and body:
                        st.success(f"Generated Document for {name}:\n\n{body}")

        # SUB-MODULE 4: POWERPOINT
        elif sub_module == "🎨 Microsoft PowerPoint & Presentations":
            tab1, tab2, tab3 = st.tabs(["📖 Practical Guide", "🎥 Video Tutorial", "✍️ Slide Deck Builder"])
            
            with tab1:
                st.markdown("""
                ### 🎨 Slide Design & Presentation Rules
                * **6x6 Rule**: Max 6 lines per slide, max 6 words per bullet.
                * **10-20-30 Rule**: 10 slides, 20 minutes, 30pt font minimum.
                * **Visual Contrast**: Dark text on light backgrounds or vice-versa.
                """)
            with tab2:
                st.write("#### Video Lesson: Presentation & Slide Design Fundamentals")
                st.video("https://www.youtube.com/watch?v=k1VUZEVuDJ8")
            with tab3:
                st.subheader("✍️ Slide Outline Builder")
                st1 = st.text_input("Slide 1 Title:")
                if st.button("Preview Slide"):
                    st.info(f"Slide Preview: {st1}")

    # -----------------------------------------------------
    # OTHER ORIGINAL COURSES PRESERVED
    # -----------------------------------------------------
    elif category == "🤝 Communication & Workplace Collaboration":
        st.subheader("🤝 Communication & Workplace Collaboration")
        st.markdown("""
        ### Professional Workplace Communication
        * **Email Etiquette**: Professional subject lines, formal greetings, concise requests.
        * **Active Listening**: Paraphrasing, avoiding interruptions, taking action items.
        * **Conflict Resolution**: Focusing on facts rather than emotions in team settings.
        """)

    elif category == "💼 Financial Literacy & Budgeting":
        st.subheader("💼 Financial Literacy & Budgeting")
        st.markdown("""
        ### Personal & Business Budgeting
        * **50/30/20 Rule**: 50% Needs, 30% Wants, 20% Savings/Debt.
        * **Income vs Expenses**: Tracking monthly cash flow using spreadsheets.
        * **Emergency Funds**: Setting aside 3–6 months of living expenses.
        """)

    elif category == "🚀 Critical Thinking & Problem Solving":
        st.subheader("🚀 Critical Thinking & Problem Solving")
        st.markdown("""
        ### Structured Decision-Making
        * **5 Whys Methodology**: Root-cause analysis by repeatedly asking 'Why?'.
        * **SWOT Analysis**: Strengths, Weaknesses, Opportunities, Threats.
        * **Data-Driven Decisions**: Evaluating facts before reaching conclusions.
        """)

# ---------------------------------------------------------
# 6. PAGE 4: SELF-ASSESSMENT & ROADMAP
# ---------------------------------------------------------
elif st.session_state.current_page == "📝 Self-Assessment & Roadmap":
    st.title("📝 Self-Assessment & Roadmap Generator")
    st.write("Assess your current readiness and generate a tailored step-by-step learning pathway.")
    
    st.subheader("Step 1: Student Information")
    user_name = st.text_input("Enter your full name:", placeholder="e.g. Jane Doe")
    selected_track = st.selectbox(
        "Select primary target focus area:", 
        ["Computer Literacy (Excel Focus)", "Communication", "Financial Literacy", "Critical Thinking"]
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
            1. **Week 1:** Complete OS Basics & Keyboard Shortcuts.
            2. **Week 2:** Master Excel formulas (`SUM`, `AVERAGE`, `IF`, `VLOOKUP`).
            3. **Week 3:** Complete Microsoft Word & PowerPoint sub-modules.
            4. **Week 4:** Take soft skill modules & use AI Assistant for spot checks.
            """)

# ---------------------------------------------------------
# 7. PAGE 5: ABOUT PLATFORM
# ---------------------------------------------------------
elif st.session_state.current_page == "ℹ️ About Platform":
    st.title("ℹ️ About SkillsPulse Academy")
    st.write("SkillsPulse is an integrated learning management environment focused on practical digital literacy, workforce development, and hands-on software training.")

st.divider()
st.caption("SkillsPulse Platform — All-in-One Practical Learning Dashboard")
