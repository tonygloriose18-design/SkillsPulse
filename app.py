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
    st.session_state.selected_module = "💻 Computer Literacy & System Navigation"

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
    st.write("An interactive, high-impact learning suite designed for practical digital literacy and workforce readiness.")
    
    try:
        st.image(HERO_IMAGE_URL, caption="Practical Digital Literacy & Skills Mastery", use_container_width=True)
    except:
        st.info("Image loading...")
        
    st.divider()
    
    st.header("⚡ Platform Dashboard Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Active Modules", value="4 Core Tracks")
    with col2:
        st.metric(label="Office Tools", value="Word, Excel, PPT")
    with col3:
        st.metric(label="Interactive Labs", value="Live Code & Text")
    with col4:
        st.metric(label="Access Cost", value="100% Free")

    st.write("---")
    st.subheader("💡 Launch Learning Tracks Directly")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.success("### 💻 Digital & Computer Literacy\nMaster OS fundamentals, file structures, shortcut mastery, and web safety.")
        if st.button("▶ Open Computer Literacy Lab"):
            st.session_state.selected_module = "💻 Computer Literacy & System Navigation"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

        st.info("### 📝 Microsoft Word & Professional Writing\nLearn document formatting, professional email structures, and resume drafting.")
        if st.button("▶ Open Microsoft Word & Writing Lab"):
            st.session_state.selected_module = "📝 Microsoft Word & Professional Writing"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

    with c2:
        st.warning("### 📊 Microsoft Excel & Data Analytics\nMaster formulas (SUM, AVERAGE, IF), formatting, tables, and pivot charts.")
        if st.button("▶ Open Microsoft Excel Lab"):
            st.session_state.selected_module = "📊 Microsoft Excel & Data Analytics"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

        st.error("### 🎨 Microsoft PowerPoint & Slide Design\nLearn visual design rules, slide layouts, presentation structures, and delivery techniques.")
        if st.button("▶ Open Microsoft PowerPoint Lab"):
            st.session_state.selected_module = "🎨 Microsoft PowerPoint & Slide Design"
            st.session_state.current_page = "📚 Learning Modules & Practical Lab"
            st.rerun()

# ---------------------------------------------------------
# 4. PAGE 2: AI CHATBOT ASSISTANT
# ---------------------------------------------------------
elif st.session_state.current_page == "🤖 SkillsPulse AI Assistant":
    st.title("🤖 SkillsPulse AI Tutor")
    st.write("Ask any questions about basic digital skills, Word formatting, Excel formulas, or PowerPoint design!")

    api_key = st.secrets.get("EJOCHAT_API_KEY", "")
    
    if not api_key:
        st.error("Please configure EJOCHAT_API_KEY in Streamlit Cloud secrets.")
        st.stop()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_prompt := st.chat_input("Ask a question (e.g., 'How do I combine cells in Excel?' or 'How do I cite in Word?')..."):
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
        "Select Active Learning Track:",
        [
            "💻 Computer Literacy & System Navigation",
            "📝 Microsoft Word & Professional Writing",
            "📊 Microsoft Excel & Data Analytics",
            "🎨 Microsoft PowerPoint & Slide Design"
        ],
        index=[
            "💻 Computer Literacy & System Navigation",
            "📝 Microsoft Word & Professional Writing",
            "📊 Microsoft Excel & Data Analytics",
            "🎨 Microsoft PowerPoint & Slide Design"
        ].index(st.session_state.selected_module)
    )
    
    st.session_state.selected_module = category
    st.divider()
    
    # -----------------------------------------------------
    # TRACK 1: COMPUTER LITERACY
    # -----------------------------------------------------
    if category == "💻 Computer Literacy & System Navigation":
        st.subheader("💻 Computer Literacy & System Navigation")
        
        tab1, tab2, tab3 = st.tabs(["📖 In-Depth Practical Guide", "🎥 Video Tutorial", "✍️ Interactive Practical Simulator"])
        
        with tab1:
            st.markdown("""
            ### Complete Operating System & Navigation Architecture
            
            #### 1. Operating Systems & Hardware Infrastructure
            * **CPU (Central Processing Unit)**: The brain of the computer executing software calculations.
            * **RAM (Random Access Memory)**: High-speed temporary memory used when applications are actively running.
            * **Storage (SSD / HDD)**: Permanent storage holding your Operating System (Windows / macOS / Linux), software programs, and personal files.
            
            #### 2. Directory Hierarchy & File Systems
            A proper folder structure prevents lost work and boosts efficiency:
            * **Root Directory**: The primary starting point (e.g., `C:\\`).
            * **User Directories**: Pre-built folders (`Documents`, `Downloads`, `Pictures`, `Desktop`).
            * **Best Practice Folder Formula**: `Main_Category / Year / Project_Name / File_v1.ext`
              * *Example*: `Work_Projects / 2026 / Quarter_1_Report / Final_Draft.docx`
            * **File Extensions to Know**:
              * `.docx` (Microsoft Word Document)
              * `.xlsx` (Microsoft Excel Spreadsheet)
              * `.pptx` (Microsoft PowerPoint Presentation)
              * `.pdf` (Portable Document Format - read-only layout standard)
              * `.exe` / `.msi` (Executable Installation Programs — handle with care)

            #### 3. Master Keyboard Shortcut Reference Matrix
            | Shortcut Command | Function / Action Performed |
            | :--- | :--- |
            | `Ctrl + C` | Copy selected item to clipboard |
            | `Ctrl + X` | Cut selected item (removes from origin) |
            | `Ctrl + V` | Paste copied or cut item |
            | `Ctrl + Z` | Undo last operation |
            | `Ctrl + Y` | Redo last undone operation |
            | `Ctrl + S` | Save current file instantly |
            | `Alt + Tab` | Switch actively running application windows |
            | `Win + D` | Minimize all open windows and show Desktop |
            | `Ctrl + Shift + Esc` | Direct launch Task Manager |
            """)
            
        with tab2:
            st.write("#### Video Lesson: Computer Basics for Absolute Beginners")
            st.video("https://www.youtube.com/watch?v=lxk2VaTaXgM")
            st.caption("Video Source: Complete Computer Fundamentals & OS Navigation Lesson")
            
        with tab3:
            st.subheader("✍️ Interactive Lab: Operating System Operations Simulator")
            st.write("Solve the system navigation prompts below:")
            
            q1 = st.text_input("1. Type the precise shortcut key combination to UNDO an accidental deletion:", placeholder="e.g. Ctrl + Z")
            q2 = st.selectbox("2. Which file extension represents a read-only document that preserves exact formatting across all devices?", ["-- Select --", ".docx", ".exe", ".pdf", ".xlsx"])
            q3 = st.text_input("3. Type the shortcut to instantly switch between active windows on your computer:", placeholder="e.g. Alt + Tab")
            
            if st.button("Submit Computer Science Lab 🚀"):
                score = 0
                if q1.strip().lower().replace(" ", "") == "ctrl+z":
                    score += 33
                if q2 == ".pdf":
                    score += 33
                if q3.strip().lower().replace(" ", "") == "alt+tab":
                    score += 34
                
                if score >= 90:
                    st.balloons()
                    st.success(f"🏆 Score: {score}%! Perfect mastery of OS shortcuts and file extensions!")
                else:
                    st.warning(f"Score: {score}%. Review the shortcut matrix in Tab 1 and try again.")

    # -----------------------------------------------------
    # TRACK 2: MICROSOFT WORD & WRITING
    # -----------------------------------------------------
    elif category == "📝 Microsoft Word & Professional Writing":
        st.subheader("📝 Microsoft Word & Professional Writing")
        
        tab1, tab2, tab3 = st.tabs(["📖 In-Depth Practical Guide", "🎥 Video Tutorial", "✍️ Interactive Drafting Workshop"])
        
        with tab1:
            st.markdown("""
            ### Complete Document Formatting & Business Communication Blueprint
            
            #### 1. Microsoft Word Document Setup Rules
            * **Typography**: Standard professional fonts are **Calibri, Arial, Times New Roman, or Garamond** (11pt - 12pt for body, 14pt - 18pt for headings).
            * **Margins**: Use **Normal Margins** (1 inch / 2.54 cm on all sides) for professional documents and resumes.
            * **Line Spacing**: Set to **1.15x or 1.5x** with 6pt space after paragraphs for clean readability.
            * **Styles Ribbon**: Always use Word's built-in `Heading 1`, `Heading 2`, and `Title` styles to create automatic Tables of Contents.

            #### 2. Structural Resume Blueprint
            * **Header**: Full Name, Location (City/Country), Phone, Professional Email (`first.last@email.com`), LinkedIn URL.
            * **Professional Summary**: 3 strong lines detailing current title, key technical skills, and value brought to a role.
            * **Work Experience**: Reverse-chronological order. Bullet points MUST start with active verbs (*Spearheaded, Formatted, Orchestrated, Optimized*).
            * **Education & Skills**: Degree/Diploma details and hard skills (e.g., MS Office Suite, Data Entry, Digital Security).

            #### 3. Formal Email / Cover Letter Structure
            ```text
            SUBJECT: Application for [Job Title] - [Your Full Name]

            Dear [Hiring Manager / Recruiter Name],

            [PARAGRAPH 1: Statement of intent, position targeted, and source of job listing.]
            [PARAGRAPH 2: 2-3 specific accomplishments with quantified results.]
            [PARAGRAPH 3: Closing call to action expressing enthusiasm for an interview.]

            Sincerely,
            [Your Full Name]
            ```
            """)
            
        with tab2:
            st.write("#### Video Lesson: How to Write a Winning Resume")
            st.video("https://www.youtube.com/watch?v=R3abknwWX7k")
            st.caption("Video Source: Professional Resume Writing Guide by Bryan Creely")
            
        with tab3:
            st.subheader("✍️ Practical Workshop: Write a Professional Email Application")
            st.write("Draft a formal application email using the lesson rules:")
            
            job_title = st.text_input("1. Target Job Position:", placeholder="e.g. Administrative Officer")
            applicant_name = st.text_input("2. Your Full Name:", placeholder="e.g. Alex Morgan")
            email_body = st.text_area(
                "3. Write your Email Body (include statement of intent and key skills):",
                height=150,
                placeholder="Dear Hiring Manager,\n\nI am writing to express my strong interest in the Administrative Officer position..."
            )
            
            if st.button("Analyze & Render Formal Document 📄"):
                if len(email_body.strip()) < 50 or applicant_name.strip() == "":
                    st.error("Please fill in all fields with complete detailed sentences.")
                else:
                    st.balloons()
                    st.success("Your Formal Application Draft Has Been Generated!")
                    st.markdown(f"""
                    ---
                    **SUBJECT:** Application for {job_title} - {applicant_name}  
                    
                    {email_body}  
                    
                    **Sincerely,**  
                    **{applicant_name}**
                    ---
                    """)

    # -----------------------------------------------------
    # TRACK 3: MICROSOFT EXCEL
    # -----------------------------------------------------
    elif category == "📊 Microsoft Excel & Data Analytics":
        st.subheader("📊 Microsoft Excel & Data Analytics")
        
        tab1, tab2, tab3 = st.tabs(["📖 In-Depth Practical Guide", "🎥 Video Tutorial", "✍️ Interactive Formula Lab"])
        
        with tab1:
            st.markdown("""
            ### Complete Spreadsheet Analytics & Formula Masterclass
            
            #### 1. Excel Grid Terminology & Navigation
            * **Workbook vs Worksheet**: A workbook is the overall file (`.xlsx`); worksheets are individual tabbed sheets inside it.
            * **Columns**: Identified by Letters (`A` through `XFD` — total 16,384 columns).
            * **Rows**: Identified by Numbers (`1` through `1,048,576` rows).
            * **Cell Reference**: The precise coordinate where a column and row intersect (e.g., `C15`).

            #### 2. Essential Formula & Function Dictionary
            *All formulas MUST begin with an equals sign (`=`).*
            
            | Function Name | Syntax Example | Description / Purpose |
            | :--- | :--- | :--- |
            | **SUM** | `=SUM(B2:B10)` | Adds all numerical values within the cell range B2 to B10. |
            | **AVERAGE** | `=AVERAGE(C1:C20)` | Computes the arithmetic mean of specified cells. |
            | **COUNT** | `=COUNT(A1:A50)` | Counts how many cells contain numbers. |
            | **COUNTA** | `=COUNTA(A1:A50)` | Counts all non-empty cells (numbers + text). |
            | **IF** | `=IF(D2>=50, "Pass", "Fail")` | Evaluates a logical condition and returns custom outputs. |
            | **MAX / MIN** | `=MAX(E1:E10)` / `=MIN(E1:E10)` | Finds the absolute highest or lowest value in a range. |

            #### 3. Data Visualization & Tables
            * **Format as Table (`Ctrl + T`)**: Converts raw data into an interactive database with automatic sorting and filtering arrows.
            * **Charts (`Alt + F1`)**: Highlight data and press shortcut to instantly generate a column chart visualization.
            """)
            
        with tab2:
            st.write("#### Video Lesson: Microsoft Excel Tutorial for Beginners")
            st.video("https://www.youtube.com/watch?v=Ai0MV7twEBE")
            st.caption("Video Source: Excel Beginners Step-by-Step Guide by Kevin Stratvert")
            
        with tab3:
            st.subheader("✍️ Interactive Formula Lab: Live Spreadsheet Solver")
            st.write("Analyze the employee sales database below and enter the correct Excel formulas:")
            
            st.table({
                "Cell Row": ["Row 1", "Row 2", "Row 3", "Row 4", "Row 5"],
                "Employee (Column A)": ["Sarah", "John", "David", "Grace", "Target Goal"],
                "Sales Target (Column B)": [5000, 5000, 5000, 5000, "N/A"],
                "Actual Sales (Column C)": [6200, 4800, 7100, 5500, "Calculate Below"]
            })
            
            f1 = st.text_input("1. Type the exact Excel formula to calculate TOTAL Sales for C1 to C4:", placeholder="e.g. =SUM(C1:C4)")
            f2 = st.text_input("2. Type the formula to find the AVERAGE sales made from C1 to C4:", placeholder="e.g. =AVERAGE(C1:C4)")
            f3 = st.text_input("3. Write an IF formula for Sarah (Cell C1) returning 'Bonus' if Sales >= 5000 else 'No Bonus':", placeholder='e.g. =IF(C1>=5000, "Bonus", "No Bonus")')
            
            if st.button("Run Spreadsheet Calculation Engine 🧪"):
                score = 0
                clean_f1 = f1.strip().upper().replace(" ", "")
                clean_f2 = f2.strip().upper().replace(" ", "")
                clean_f3 = f3.strip().upper().replace(" ", "")
                
                if clean_f1 == "=SUM(C1:C4)":
                    score += 33
                if clean_f2 == "=AVERAGE(C1:C4)":
                    score += 33
                if 'IF(C1>=5000,"BONUS","NOBONUS")' in clean_f3:
                    score += 34
                
                if score >= 90:
                    st.balloons()
                    st.success(f"🏆 100% Score! Calculated Total: $23,600 | Calculated Average: $5,900 | Logic Check: PASS!")
                else:
                    st.warning(f"Score: {score}%. Ensure your formulas start with '=' and use proper cell ranges like C1:C4.")

    # -----------------------------------------------------
    # TRACK 4: MICROSOFT POWERPOINT
    # -----------------------------------------------------
    elif category == "🎨 Microsoft PowerPoint & Slide Design":
        st.subheader("🎨 Microsoft PowerPoint & Slide Design")
        
        tab1, tab2, tab3 = st.tabs(["📖 In-Depth Practical Guide", "🎥 Video Tutorial", "✍️ Interactive Deck Designer"])
        
        with tab1:
            st.markdown("""
            ### Complete Presentation Design & Storytelling Masterclass
            
            #### 1. The 6x6 Rule of Professional Slide Design
            * **Maximum 6 Lines**: Never exceed 6 bullet points per slide.
            * **Maximum 6 Words**: Keep individual bullet points under 6 words where possible.
            * **Contrast Principle**: Use high-contrast colors (Dark text on light background or Light text on dark background).
            * **Visual Hierarchy**: Titles should be 32pt - 40pt bold; body text should be 18pt - 24pt.

            #### 2. The 10-20-30 Rule of Public Presentations
            * **10 Slides**: The ideal length for a business or class presentation.
            * **20 Minutes**: Maximum time to deliver the talk to keep audience engagement high.
            * **30 Point Font**: Minimum font size used so everyone in the back of the room can read easily.

            #### 3. Master Slide Deck Structure Framework
            1. **Slide 1: Title Slide** (Topic, Presenter Name, Date).
            2. **Slide 2: Problem Statement** (What real challenge are you solving?).
            3. **Slide 3: Proposed Solution** (Your key takeaway or idea).
            4. **Slide 4: Key Supporting Evidence / Data Chart**.
            5. **Slide 5: Action Plan & Conclusion**.
            """)
            
        with tab2:
            st.write("#### Video Lesson: Fundamentals of Great Presentations")
            st.video("https://www.youtube.com/watch?v=k1VUZEVuDJ8")
            st.caption("Video Source: Beginner Interface and Layout Masterclass")
            
        with tab3:
            st.subheader("✍️ Interactive Deck Builder Lab")
            st.write("Design a 3-slide pitch outline using slide design rules:")
            
            slide1_title = st.text_input("Slide 1 Main Title:", placeholder="e.g. Digital Literacy in 2026")
            slide2_bullet = st.text_input("Slide 2 Key Bullet Point (Apply 6-Word Rule):", placeholder="e.g. Digital skills increase workplace productivity dramatically")
            slide3_callout = st.text_input("Slide 3 Call to Action:", placeholder="e.g. Join the SkillsPulse Academy Today")
            
            if st.button("Generate & Validate Slide Structure 🎨"):
                word_count = len(slide2_bullet.strip().split())
                if slide1_title == "" or slide3_callout == "":
                    st.error("Please fill in all slide prompts.")
                elif word_count > 8:
                    st.warning(f"Your Slide 2 bullet has {word_count} words! Remember the 6x6 rule: keep bullet points concise.")
                else:
                    st.balloons()
                    st.success("Slide Deck Outline Successfully Generated and Validated!")
                    st.markdown(f"""
                    ---
                    ### 🖼️ Slide 1: Cover
                    # {slide1_title}
                    
                    ---
                    ### 🖼️ Slide 2: Core Concept
                    * {slide2_bullet} *(Word Count: {word_count} - Concise!)*
                    
                    ---
                    ### 🖼️ Slide 3: Action & Takeaway
                    > **{slide3_callout}**
                    ---
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
        ["Computer Literacy", "Microsoft Word & Writing", "Microsoft Excel Data", "PowerPoint Presentation"]
    )
    
    st.subheader("Step 2: Self-Evaluation")
    level = st.radio("Current Confidence Level:", ["Beginner (Starting from scratch)", "Intermediate (Know simple usage)", "Advanced (Seeking mastery)"])
    
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
            1. **Week 1 (Theory & Shortcuts):** Read the in-depth guides and memorize key shortcut matrices.
            2. **Week 2 (Practical Application):** Complete all practical simulator labs in your chosen track.
            3. **Week 3 (Project Build):** Produce a real Word document, Excel spreadsheet calculation, or PowerPoint deck.
            4. **Week 4 (AI Review):** Use the SkillsPulse AI Tutor to test your knowledge with spot questions.
            """)

# ---------------------------------------------------------
# 7. PAGE 5: ABOUT PLATFORM
# ---------------------------------------------------------
elif st.session_state.current_page == "ℹ️ About Platform":
    st.title("ℹ️ About SkillsPulse Academy")
    st.write("SkillsPulse is an integrated learning management environment focused on practical digital literacy, workforce development, and hands-on software training.")
    st.write("Built for interactive educational demonstrations, class presentations, and practical skills evaluation.")

st.divider()
st.caption("SkillsPulse Platform — All-in-One Practical Learning Dashboard")
