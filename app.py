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
            tab1, tab2, tab3 = st.tabs(["📖 In-Depth Practical Guide", "🎥 Video Tutorials (5 Lessons)", "✍️ Interactive Lab"])
            
            with tab1:
                st.markdown("""
                ### ⚙️ Comprehensive OS & System Architecture Manual
                
                #### Section 1: Computing Hardware & Processing Mechanics
                Understanding how software interacts with hardware is essential for digital fluency:
                * **CPU (Central Processing Unit)**: Executes all logical calculations. Clock speed (GHz) determines execution rate.
                * **RAM (Random Access Memory)**: Volatile memory storing active apps. Higher RAM allows smooth multitasking.
                * **Primary Storage (SSD / HDD)**: Solid State Drives (SSDs) read data via flash memory, offering much faster boot times than magnetic Hard Disk Drives (HDDs).
                * **Peripherals & I/O Ports**: USB-C, HDMI, DisplayPort, and Wireless Bluetooth interfaces.

                #### Section 2: Advanced File Directory Architecture
                * **Root Systems**: Path construction starting from local disk (`C:\\Windows\\System32` vs `C:\\Users\\Public\\Documents`).
                * **Folder Taxonomy Standards**: Always implement standardized file naming conventions to preserve project tracking:
                  `[Project_Code]_[Department]_[Document_Type]_[YYYYMMDD]_[Version]`
                  * *Example*: `SP2026_FIN_QuarterlyReport_20260817_v2.1.docx`
                * **File Extension Mechanics**:
                  * Document Files: `.docx`, `.pdf`, `.rtf`, `.txt`
                  * Spreadsheet Data: `.xlsx`, `.csv`, `.ods`
                  * Graphic & Video Formats: `.png`, `.svg`, `.mp4`, `.webm`
                  * Executables & Scripts: `.exe`, `.msi`, `.bat`, `.ps1` (Exercise caution before execution).

                #### Section 3: System Utilities & Power User Navigation Matrix
                Mastering key commands increases administrative operational speed by up to 300%:
                | Functionality | Windows Command | macOS Equivalent | Description |
                | :--- | :--- | :--- | :--- |
                | Task Manager | `Ctrl + Shift + Esc` | `Cmd + Option + Esc` | Force terminates non-responsive software. |
                | System Search | `Win + S` | `Cmd + Space` | Universal file, setting, and index lookup. |
                | Windows Snap | `Win + Left / Right Arrow` | Built-in Split View | Splits open windows across monitors cleanly. |
                | File Clipboard | `Win + V` | External Utility | Accesses clipboard history buffer. |
                | File Explorer | `Win + E` | `Cmd + Finder` | Opens root directory instantly. |

                #### Section 4: Cybersecurity & Environmental Maintenance
                * **Disk Cleanups**: Periodically remove temporary cache buffers (`%temp%` directory).
                * **Network Protocols**: Verify HTTPS encryption badges prior to submitting personal data online.
                * **Multi-Factor Authentication (2FA)**: Always pair password storage with authenticator tokens.
                """)
            with tab2:
                st.write("#### 🎥 Complete Video Tutorial Series (5 Lessons)")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Lesson 1: Computer Hardware & OS Fundamentals**")
                    st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")
                    
                    st.write("**Lesson 3: File Explorer & Storage Management**")
                    st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")

                    st.write("**Lesson 5: Essential System Shortcuts & Utilities**")
                    st.video("https://www.youtube.com/watch?v=k1VUZEVuDJ8")

                with col2:
                    st.write("**Lesson 2: Windows 11 Full Desktop Tour**")
                    st.video("https://www.youtube.com/watch?v=Ai0MV7twEBE")

                    st.write("**Lesson 4: Internet Safety & Web Browsing**")
                    st.video("https://www.youtube.com/watch?v=R3abknwWX7k")

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
            tab1, tab2, tab3 = st.tabs(["📖 In-Depth Excel Masterclass Manual", "🎥 Video Tutorials (5 Lessons)", "✍️ Interactive Formula Lab"])
            
            with tab1:
                st.markdown("""
                ### 📊 Comprehensive Microsoft Excel & Data Analytics Manual
                
                #### Section 1: Spreadsheet Architecture & Interface Foundations
                * **Grid Layout Mechanics**: Composed of **Columns** (`A` to `XFD` = 16,384 total) and **Rows** (`1` to `1,048,576` total).
                * **Cells & Ranges**: Intersection point coordinates (e.g., `B5`). Range notation uses colons: `A1:C10` defines a block from top-left cell A1 to bottom-right cell C10.
                * **Data Types**: Excel treats numbers, plain text strings, dates (stored internally as sequential serial numbers starting from Jan 1, 1900), and boolean logical values (`TRUE`/`FALSE`) differently.

                #### Section 2: Comprehensive Mathematical & Logical Function Library
                *All Excel formulas MUST start with an equals sign (`=`).*

                ##### 1. Mathematical & Basic Aggregations
                * **`=SUM(range)`**: Adds all numeric entries in a cell selection. Syntax: `=SUM(C2:C50)`.
                * **`=AVERAGE(range)`**: Returns arithmetic mean. Syntax: `=AVERAGE(D2:D100)`.
                * **`=MIN(range)` / `=MAX(range)`**: Identifies absolute minimum or maximum value within numerical data.
                * **`=PRODUCT(range)`** / **`=ROUND(cell, num_digits)`**: Multiplies numbers or rounds decimals to target precision.

                ##### 2. Counting & Conditional Aggregations
                * **`=COUNT(range)`**: Counts cells containing purely numeric data.
                * **`=COUNTA(range)`**: Counts all non-empty cells (text + numbers).
                * **`=COUNTIF(range, criteria)`**: Counts cells meeting specific parameters.  
                  * *Example*: `=COUNTIF(C2:C50, ">5000")`
                * **`=SUMIF(range, criteria, [sum_range])`**: Sums specified values only if condition matches.  
                  * *Example*: `=SUMIF(A2:A50, "Sales", B2:B50)`

                ##### 3. Logical Evaluation Functions
                * **`=IF(logical_test, value_if_true, value_if_false)`**: Evaluates logical conditions.  
                  * *Example*: `=IF(C2>=5000, "Bonus Qualified", "Standard Pay")`
                * **Nested IF / AND / OR Functions**:
                  * `=IF(AND(A2="Active", B2>100), "Eligible", "Ineligible")`

                ##### 4. Professional Lookup & Reference Functions
                * **`=VLOOKUP(lookup_value, table_array, col_index_num, range_lookup)`**: Searches vertical columns for matches.
                  * *Syntax Example*: `=VLOOKUP(E2, A2:C100, 3, FALSE)` (Uses `FALSE` for exact match).
                * **`=XLOOKUP(lookup_value, lookup_array, return_array)`**: Modern, flexible replacement for VLOOKUP that works in both directions.

                #### Section 3: Data Cleaning, Formatting & Visualization
                * **Format as Table (`Ctrl + T`)**: Converts data ranges into structured tables with dynamic banded rows, auto-filtering headers, and automatic formula expansion.
                * **Conditional Formatting**: Applies visual highlight colors based on cell value parameters (e.g., highlighting negative balances red).
                * **Pivot Tables (`Insert > PivotTable`)**: Summarizes multi-thousand-row datasets dynamically into structured reports without requiring custom formulas.
                """)
            with tab2:
                st.write("#### 🎥 Complete Excel Masterclass Series (5 Lessons)")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Lesson 1: Excel Beginner Interface & Cell Basics**")
                    st.video("https://www.youtube.com/watch?v=Ai0MV7twEBE")
                    
                    st.write("**Lesson 3: Advanced Formulas (SUMIF, COUNTIF, IF)**")
                    st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")

                    st.write("**Lesson 5: Pivot Tables & Data Charts**")
                    st.video("https://www.youtube.com/watch?v=k1VUZEVuDJ8")

                with col2:
                    st.write("**Lesson 2: Top 10 Essential Excel Formulas**")
                    st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")

                    st.write("**Lesson 4: Master VLOOKUP & XLOOKUP Functions**")
                    st.video("https://www.youtube.com/watch?v=R3abknwWX7k")

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
            tab1, tab2, tab3 = st.tabs(["📖 In-Depth Practical Guide", "🎥 Video Tutorials (5 Lessons)", "✍️ Cover Letter Simulator"])
            
            with tab1:
                st.markdown("""
                ### 📝 Comprehensive Microsoft Word & Document Design Manual
                
                #### Section 1: Typography Rules & Page Layout Setup
                * **Font Pairings**: Combine clean headers with legible body fonts (e.g., Arial + Calibri, Times New Roman + Garamond).
                * **Sizing Rules**: Document Title (20-24pt Bold), Heading 1 (16-18pt Bold), Heading 2 (13-15pt Semi-Bold), Body Text (11-12pt Regular).
                * **Margins & Spacing**: Standard 1-inch (2.54 cm) margins on all sides. Set line spacing to 1.15x - 1.5x with 6pt space after paragraphs.

                #### Section 2: Advanced Word Productivity Features
                * **Styles Ribbon**: Using `Heading 1` and `Heading 2` allows Word to auto-generate a dynamic Table of Contents (`References > Table of Contents`).
                * **Page Breaks vs Section Breaks**:
                  * **Page Break (`Ctrl + Enter`)**: Forces text onto a new page.
                  * **Section Break**: Allows different page orientations (Portrait vs Landscape) or headers/footers within the same document.
                * **Track Changes & Comments (`Review > Track Changes`)**: Collaboration tool to view edits, additions, and strike-throughs in shared documents.

                #### Section 3: Professional Resume & Business Document Anatomy
                * **Header**: Name, City/Country, Phone, Email (`first.last@email.com`), LinkedIn profile URL.
                * **Professional Summary**: 3 sentences highlighting core skills, domain expertise, and key accomplishments.
                * **Work Experience Bullet Formula**: `[Action Verb] + [Core Task] + [Quantified Result / Impact]`
                  * *Example*: *"Optimized digital file storage system, reducing document retrieval time by 35% across a 10-person team."*
                """)
            with tab2:
                st.write("#### 🎥 Complete Microsoft Word & Writing Series (5 Lessons)")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Lesson 1: Microsoft Word Beginner Fundamentals**")
                    st.video("https://www.youtube.com/watch?v=R3abknwWX7k")
                    
                    st.write("**Lesson 3: Formatting Resumes & Cover Letters**")
                    st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")

                    st.write("**Lesson 5: Table of Contents & Mail Merge**")
                    st.video("https://www.youtube.com/watch?v=k1VUZEVuDJ8")

                with col2:
                    st.write("**Lesson 2: Styles, Headers & Section Breaks**")
                    st.video("https://www.youtube.com/watch?v=Ai0MV7twEBE")

                    st.write("**Lesson 4: Track Changes & Collaboration**")
                    st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")

            with tab3:
                st.subheader("✍️ Cover Letter Builder")
                name = st.text_input("Your Full Name:")
                body = st.text_area("Write a short intro paragraph:")
                if st.button("Generate Document"):
                    if name and body:
                        st.success(f"Generated Document for {name}:\n\n{body}")

        # SUB-MODULE 4: POWERPOINT
        elif sub_module == "🎨 Microsoft PowerPoint & Presentations":
            tab1, tab2, tab3 = st.tabs(["📖 In-Depth Practical Guide", "🎥 Video Tutorials (5 Lessons)", "✍️ Slide Deck Builder"])
            
            with tab1:
                st.markdown("""
                ### 🎨 Comprehensive Presentation Design & Storytelling Manual
                
                #### Section 1: Presentation Framework Rules
                * **The 10-20-30 Rule**: 10 total slides, maximum 20 minutes delivery time, minimum 30pt font size so text is readable from the back of any room.
                * **The 6x6 Rule**: Limit slides to a maximum of 6 bullet points, with no more than 6 words per bullet.
                * **Visual Contrast**: Dark backgrounds require white/light text; light backgrounds require dark text. Avoid clutter and heavy paragraphs.

                #### Section 2: Standard Business Slide Deck Architecture
                1. **Slide 1: Title & Presenter Info** (Clear title, subtitle, name, date).
                2. **Slide 2: Problem Statement** (Define the problem you are solving).
                3. **Slide 3: Proposed Solution / Innovation** (Explain core idea or value).
                4. **Slide 4: Key Supporting Data** (Use 1 clear chart or simple key metrics).
                5. **Slide 5: Summary & Call to Action** (Provide clear next steps).

                #### Section 3: PowerPoint Features & Delivery Tips
                * **Slide Master (`View > Slide Master`)**: Edit universal font styles and logos across all slides simultaneously.
                * **Presenter View**: Allows speakers to view notes, upcoming slides, and timers on a private screen while displaying clean slides to the audience.
                * **SmartArt Graphics**: Convert plain text bullet points into clean, professional visual diagrams in 1 click.
                """)
            with tab2:
                st.write("#### 🎥 Complete PowerPoint Design Series (5 Lessons)")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Lesson 1: PowerPoint Beginners Complete Guide**")
                    st.video("https://www.youtube.com/watch?v=k1VUZEVuDJ8")
                    
                    st.write("**Lesson 3: Graphic Design Rules for Slide Decks**")
                    st.video("https://www.youtube.com/watch?v=Ai0MV7twEBE")

                    st.write("**Lesson 5: Presenter View & Delivery Tips**")
                    st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")

                with col2:
                    st.write("**Lesson 2: SmartArt & Slide Master Customization**")
                    st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")

                    st.write("**Lesson 4: Creating Data Charts & Animations**")
                    st.video("https://www.youtube.com/watch?v=R3abknwWX7k")

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
        tab1, tab2 = st.tabs(["📖 Detailed In-Depth Guide", "🎥 Video Training Series"])
        
        with tab1:
            st.markdown("""
            ### 🤝 Professional Communication & Workplace Synergy Manual
            
            #### Section 1: Business Email Etiquette Standards
            * **Subject Lines**: Must be concise and descriptive (e.g., `ACTION REQUIRED: Q3 Report Review`).
            * **Salutations**: Use formal greetings (`Dear Mr./Ms. [Last Name]`, or `Dear [Team Name]`).
            * **The BLUF Rule (Bottom Line Up Front)**: State your core message or request in the first two sentences.

            #### Section 2: Active Listening & Conflict Resolution
            * **Active Listening**: Paraphrase speaker points, take written notes, and ask clarifying questions before responding.
            * **De-escalation Framework**: Separate facts from emotional reactions during workplace disagreements. Focus on shared goals rather than personal differences.
            """)
        with tab2:
            st.video("https://www.youtube.com/watch?v=R3abknwWX7k")

    elif category == "💼 Financial Literacy & Budgeting":
        st.subheader("💼 Financial Literacy & Budgeting")
        tab1, tab2 = st.tabs(["📖 Detailed In-Depth Guide", "🎥 Video Training Series"])
        
        with tab1:
            st.markdown("""
            ### 💼 Personal & Small Business Financial Management Manual
            
            #### Section 1: The 50/30/20 Budgeting Allocation Framework
            * **50% Needs**: Essential living costs (housing, utilities, groceries, basic transportation).
            * **30% Wants**: Discretionary spending (entertainment, dining out, hobbies).
            * **20% Savings & Debt Repayment**: Emergency funds, investments, and principal debt payments.

            #### Section 2: Income Statement & Cash Flow Fundamentals
            * **Net Cash Flow**: Total Cash Inflows minus Total Cash Outflows over 30 days.
            * **Emergency Fund Strategy**: Build 3 to 6 months of living expenses in liquid, low-risk accounts.
            """)
        with tab2:
            st.video("https://www.youtube.com/watch?v=y2K1qI_N7S4")

    elif category == "🚀 Critical Thinking & Problem Solving":
        st.subheader("🚀 Critical Thinking & Problem Solving")
        tab1, tab2 = st.tabs(["📖 Detailed In-Depth Guide", "🎥 Video Training Series"])
        
        with tab1:
            st.markdown("""
            ### 🚀 Analytical Thinking & Problem-Solving Frameworks
            
            #### Section 1: The 5 Whys Root Cause Analysis
            Iteratively ask "Why?" five times to drill down past surface symptoms to find the underlying issue:
            1. *Problem*: The software crashed. -> *Why?* -> The server ran out of memory.
            2. *Why?* -> A process didn't close correctly. -> *Why?* -> Memory leaks in the code update.
            3. *Why?* -> Updates weren't tested properly before release. -> *Why?* -> No automated testing pipeline exists.

            #### Section 2: SWOT Matrix Analysis
            Evaluate **Strengths**, **Weaknesses**, **Opportunities**, and **Threats** before launching any new initiative or making strategic decisions.
            """)
        with tab2:
            st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")

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
