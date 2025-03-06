import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("❌ Gemini API key not found. Please add it to the `.env` file.")
    st.stop()
genai.configure(api_key=API_KEY)

# Chatbot Function
def chatbot_response(user_input):
    model = genai.GenerativeModel("gemini-1.5-pro")  # Use the best available Gemini model
    response = model.generate_content(user_input)
    return response.text

# Streamlit UI for Chatbot
st.set_page_config(
    page_title="Smart Chatbot Assistant",
    page_icon="👩‍💻🤖",  # Updated to a female AI-themed chatbot icon
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling (DeepSeek-like UI)
st.markdown("""
    <style>
    /* Main background and text color */
    body {
        background-color: black;
        color: white;
    }
    /* Input field styling */
    .stTextInput input {
        background-color: #1e1e1e;
        color: white;
        border: 1px solid #444;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        width: 100%;
    }
    /* Button styling */
    .stButton button {
        background-color: #ffcc00;
        color: black;
        border-radius: 10px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        cursor: pointer;
        width: 100%;
        transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton button:hover {
        background-color: #e6b800;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
    }
    .stButton button:active {
        transform: translateY(0);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    /* User message styling */
    .user-message {
        background-color: #2e2e2e;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        font-size: 16px;
        color: white;
        border-left: 5px solid #ffcc00;
    }
    /* Assistant message styling */
    .assistant-message {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        font-size: 16px;
        color: white;
        border-left: 5px solid #00b3b3;
    }
    /* Warning message styling */
    .stWarning {
        color: #ff3333;
        font-size: 14px;
        margin-top: 10px;
    }
    /* Subheading styling */
    .subheading {
        font-size: 18px;
        text-align: center;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    .subheading-1 {
        color: #ffcc00; /* Yellow */
    }
    .subheading-2 {
        color: #00b3b3; /* Cyan */
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Header
st.markdown("<h1 style='text-align:center; color:#ffcc00;'>👩‍💻🤖 Smart Chatbot Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheading subheading-1'>Your AI-powered assistant for quick and accurate answers!</p>", unsafe_allow_html=True)
st.markdown("<p class='subheading subheading-2'>Ask me anything, and I'll help you out in seconds.</p>", unsafe_allow_html=True)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"<div class='user-message'>👤 <strong>You:</strong> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='assistant-message'>👩‍💻🤖 <strong>Assistant:</strong> {message['content']}</div>", unsafe_allow_html=True)

# Use st.form to handle input and clear it after submission
with st.form("chat_form", clear_on_submit=True):
    user_query = st.text_input("💬 Ask me anything:", placeholder="Type your question here...", key="user_input")
    submit_button = st.form_submit_button("🚀 Send")

# Handle form submission
if submit_button:
    if user_query.strip():
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_query})
        # Generate bot response
        with st.spinner("🤔 Thinking..."):
            bot_reply = chatbot_response(user_query)
        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        # Rerun to update the chat history
        st.rerun()
    else:
        st.markdown("<div class='stWarning'>⚠️ Please enter a question!</div>", unsafe_allow_html=True)



# import streamlit as st
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Set up Gemini API key
# API_KEY = os.getenv("GEMINI_API_KEY")
# if not API_KEY:
#     st.error("❌ Gemini API key not found. Please add it to the `.env` file.")
#     st.stop()
# genai.configure(api_key=API_KEY)

# # Chatbot Function
# def chatbot_response(user_input):
#     model = genai.GenerativeModel("gemini-1.5-pro")  # Use the best available Gemini model
#     response = model.generate_content(user_input)
#     return response.text

# # Streamlit UI for Chatbot
# st.set_page_config(
#     page_title="Smart Chatbot Assistant",
#     page_icon="🤖",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Custom CSS for styling (DeepSeek-like UI)
# st.markdown("""
#     <style>
#     /* Main background and text color */
#     body {
#         background-color: black;
#         color: white;
#     }
#     /* Input field styling */
#     .stTextInput input {
#         background-color: #1e1e1e;
#         color: white;
#         border: 1px solid #444;
#         border-radius: 10px;
#         padding: 10px;
#         font-size: 16px;
#         width: 100%;
#     }
#     /* Button styling */
#     .stButton button {
#         background-color: #ffcc00;
#         color: black;
#         border-radius: 10px;
#         padding: 10px 20px;
#         font-size: 16px;
#         font-weight: bold;
#         border: none;
#         cursor: pointer;
#         width: 100%;
#         transition: background-color 0.3s ease;
#     }
#     .stButton button:hover {
#         background-color: #e6b800;
#     }
#     /* User message styling */
#     .user-message {
#         background-color: #2e2e2e;
#         padding: 15px;
#         border-radius: 10px;
#         margin: 10px 0;
#         font-size: 16px;
#         color: white;
#         border-left: 5px solid #ffcc00;
#     }
#     /* Assistant message styling */
#     .assistant-message {
#         background-color: #1e1e1e;
#         padding: 15px;
#         border-radius: 10px;
#         margin: 10px 0;
#         font-size: 16px;
#         color: white;
#         border-left: 5px solid #00b3b3;
#     }
#     /* Warning message styling */
#     .stWarning {
#         color: #ff3333;
#         font-size: 14px;
#         margin-top: 10px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Title and Header
# st.markdown("<h1 style='text-align:center; color:#ffcc00;'>🤖 Smart Chatbot Assistant</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center; font-size:18px; color:#666;'>Ask me anything, and I'll help you out!</p>", unsafe_allow_html=True)

# # Initialize session state for chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat history
# for message in st.session_state.messages:
#     if message["role"] == "user":
#         st.markdown(f"<div class='user-message'>👤 <strong>You:</strong> {message['content']}</div>", unsafe_allow_html=True)
#     else:
#         st.markdown(f"<div class='assistant-message'>🤖 <strong>Assistant:</strong> {message['content']}</div>", unsafe_allow_html=True)

# # Use st.form to handle input and clear it after submission
# with st.form("chat_form", clear_on_submit=True):
#     user_query = st.text_input("💬 Ask me anything:", placeholder="Type your question here...", key="user_input")
#     submit_button = st.form_submit_button("🚀 Send")

# # Handle form submission
# if submit_button:
#     if user_query.strip():
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": user_query})
#         # Generate bot response
#         with st.spinner("🤔 Thinking..."):
#             bot_reply = chatbot_response(user_query)
#         # Add bot response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": bot_reply})
#         # Rerun to update the chat history
#         st.rerun()
#     else:
#         st.markdown("<div class='stWarning'>⚠️ Please enter a question!</div>", unsafe_allow_html=True)






# import streamlit as st
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Set up Gemini API key
# API_KEY = os.getenv("GEMINI_API_KEY")
# if not API_KEY:
#     st.error("❌ Gemini API key not found. Please add it to the `.env` file.")
#     st.stop()
# genai.configure(api_key=API_KEY)

# # Chatbot Function
# def chatbot_response(user_input):
#     model = genai.GenerativeModel("gemini-1.5-pro")  # Use the best available Gemini model
#     response = model.generate_content(user_input)
#     return response.text

# # Streamlit UI for Chatbot
# st.set_page_config(
#     page_title="Smart Chatbot Assistant",
#     page_icon="🤖",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Custom CSS for styling
# st.markdown("""
#     <style>
#     .stTextInput input {
#         border-radius: 10px;
#         padding: 10px;
#         font-size: 16px;
#         width: 100%;
#     }
#     .stButton button {
#         background-color: #ffcc00;
#         color: black;
#         border-radius: 10px;
#         padding: 10px 20px;
#         font-size: 16px;
#         font-weight: bold;
#         border: none;
#         cursor: pointer;
#         width: 100%;
#         transition: background-color 0.3s ease;
#     }
#     .stButton button:hover {
#         background-color: #e6b800;
#     }
#     .user-message {
#         background-color: #f0f2f6;
#         padding: 15px;
#         border-radius: 10px;
#         margin: 10px 0;
#         font-size: 16px;
#         color: #333;
#         border-left: 5px solid #ffcc00;
#     }
#     .assistant-message {
#         background-color: #e6f7ff;
#         padding: 15px;
#         border-radius: 10px;
#         margin: 10px 0;
#         font-size: 16px;
#         color: #333;
#         border-left: 5px solid #00b3b3;
#     }
#     .stWarning {
#         color: #ff3333;
#         font-size: 14px;
#         margin-top: 10px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Title and Header
# st.markdown("<h1 style='text-align:center; color:#ffcc00;'>🤖 Smart Chatbot Assistant</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center; font-size:18px; color:#666;'>Ask me anything, and I'll help you out!</p>", unsafe_allow_html=True)

# # Initialize session state for chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat history
# for message in st.session_state.messages:
#     if message["role"] == "user":
#         st.markdown(f"<div class='user-message'>👤 <strong>You:</strong> {message['content']}</div>", unsafe_allow_html=True)
#     else:
#         st.markdown(f"<div class='assistant-message'>🤖 <strong>Assistant:</strong> {message['content']}</div>", unsafe_allow_html=True)

# # Use st.form to handle input and clear it after submission
# with st.form("chat_form", clear_on_submit=True):
#     user_query = st.text_input("💬 Ask me anything:", placeholder="Type your question here...", key="user_input")
#     submit_button = st.form_submit_button("🚀 Send")

# # Handle form submission
# if submit_button:
#     if user_query.strip():
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": user_query})
#         # Generate bot response
#         with st.spinner("🤔 Thinking..."):
#             bot_reply = chatbot_response(user_query)
#         # Add bot response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": bot_reply})
#         # Rerun to update the chat history
#         st.rerun()
#     else:
#         st.markdown("<div class='stWarning'>⚠️ Please enter a question!</div>", unsafe_allow_html=True)



# import streamlit as st
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# load_dotenv()

# # Set up Gemini API key
# API_KEY= os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=API_KEY)

# # Chatbot Function
# def chatbot_response(user_input):
#     model = genai.GenerativeModel("gemini-1.5-pro")  # Use the best available Gemini model
#     response = model.generate_content(user_input)
#     return response.text

# # Streamlit UI for Chatbot
# st.markdown("<h2 style='color:#ffcc00; text-align:center;'>🤖 Smart Chatbot Assistant</h2>", unsafe_allow_html=True)

# user_query = st.text_input("💬 Ask me anything:", "")

# if st.button("Send"):
#     if user_query.strip():
#         with st.spinner("Thinking... 💭"):
#             bot_reply = chatbot_response(user_query)
#         st.markdown(f"<div class='stSuccess'>{bot_reply}</div>", unsafe_allow_html=True)
#     else:
#         st.warning("Please enter a question!")





