import streamlit as st
from openai import AzureOpenAI

# 1. Page Configuration
st.set_page_config(page_title="SkillsPulse - Learning Academy", page_icon="📚", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to section:",
    ["🏠 Home Dashboard", "🤖 SkillsPulse AI Assistant", "📚 Learning Modules", "ℹ️ About Platform"]
)

# 3. CHATBOT PAGE
if page == "🤖 SkillsPulse AI Assistant":
    st.title("🤖 SkillsPulse AI Tutor")
    st.write("Ask any questions about basic digital skills, document formatting, or resume writing!")

    # Initialize Azure OpenAI Client safely using secrets
    try:
        client = AzureOpenAI(
            azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"],
            api_key=st.secrets["AZURE_OPENAI_API_KEY"],
            api_version="2024-02-01"
        )
        deployment_name = st.secrets["AZURE_OPENAI_DEPLOYMENT_NAME"]
    except Exception as e:
        st.error("Please configure your secrets in Streamlit Cloud to activate the AI tutor.")
        st.stop()

    # Initialize Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful, encouraging tutor for SkillsPulse. You specialize in teaching basic digital skills, email communication, office software, and resume building in simple terms."}
        ]

    # Display Chat Messages
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Accept User Input
    if user_prompt := st.chat_input("Ask a question (e.g., 'How do I create a table in Word?')..."):
        st.chat_message("user").markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            try:
                response = client.chat.completions.create(
                    model=deployment_name,
                    messages=st.session_state.messages,
                    temperature=0.7
                )
                assistant_reply = response.choices[0].message.content
                message_placeholder.markdown(assistant_reply)
                st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
            except Exception as err:
                st.error(f"Error connecting to AI service: {err}")

# 4. HOME DASHBOARD PAGE
elif page == "🏠 Home Dashboard":
    st.title("📚 SkillsPulse: Essential Skills Academy")
    st.write("Welcome! Use the sidebar menu to navigate through learning modules or chat with our AI Assistant.")

# 5. OTHER PAGES
elif page == "📚 Learning Modules":
    st.title("📚 Learning Modules")
    st.write("Explore step-by-step practical guides for essential everyday tools.")

elif page == "ℹ️ About Platform":
    st.title("ℹ️ About SkillsPulse")
    st.write("An intuitive learning portal for essential digital and workplace skills.")
