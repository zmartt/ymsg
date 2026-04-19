import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Gemini App", page_icon="🚀")
st.title("🤖 My Custom AI App")
st.markdown("Enter your request below to get started.")

# --- API SETUP ---
# On Streamlit Cloud, we store the key in "Secrets". 
# For local testing, it looks for a key in your environment.
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # --- MODEL CONFIGURATION ---
    # Replace the text below with your "System Instructions" from AI Studio
    system_prompt = """
    YOU ARE A [Insert your App Role here, e.g., YouTube Coach].
    YOUR GOAL IS TO [Insert your specific goal from AI Studio].
    STRICT RULES: [Insert any rules you wrote in AI Studio].
    """
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash", # Or gemini-1.5-pro
        system_instruction=system_prompt
    )

    # --- USER INTERFACE ---
    user_input = st.text_area("Your Question:", placeholder="Type here...")

    if st.button("Generate Response"):
        if user_input:
            with st.spinner("Thinking..."):
                try:
                    response = model.generate_content(user_input)
                    st.subheader("Result:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter some text first!")
else:
    st.info("Please add your Google API Key to continue.")