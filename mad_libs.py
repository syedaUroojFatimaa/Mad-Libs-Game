import streamlit as st

# Page Configurations
st.set_page_config(page_title="Mad Libs Fun 🎭", page_icon="🎨", layout="centered")

# Custom CSS for Modern Styling
st.markdown(
    """
    <style>
    body {
        background-color: #F5F7FA;
    }
    .stApp {
        background: url('https://source.unsplash.com/1600x900/?nature,landscape') no-repeat center center fixed;
        background-size: cover;
    }
    .title {
        font-size: 42px;
        font-weight: 600;
        text-align: center;
        color: #333;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.1);
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #555;
        margin-bottom: 30px;
    }
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 1px solid #ddd;
        padding: 12px;
        font-size: 16px;
        width: 100%;
        background-color: #f9f9f9;
    }
    .stButton > button {
        border-radius: 8px;
        background: linear-gradient(135deg, #007BFF, #0056b3);
        color: white;
        font-size: 18px;
        padding: 12px;
        border: none;
        transition: 0.3s ease-in-out;
        box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.2);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #0056b3, #004085);
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
    }
    .story-box {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        font-size: 18px;
        line-height: 1.6;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Content
st.markdown('<h1 class="title">🎭 Mad Libs Game</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Fill in the blanks and create a fun story! 🚀</p>', unsafe_allow_html=True)

# User Inputs with Icons
name = st.text_input("👤 Name")
place = st.text_input("📍 Place")
animal = st.text_input("🐾 Animal")
verb = st.text_input("⚡ Action Verb")
adjective = st.text_input("🎨 Adjective")

# Generate Story Button
if st.button("Generate Story ✨"):
    if name and place and animal and verb and adjective:
        story = f"""
        Once upon a time, **{name}** traveled to **{place}**.  
        There, they saw a **{adjective} {animal}** trying to **{verb}**.  
        It was the funniest thing ever! 😂  
        """
        st.markdown('<div class="story-box">', unsafe_allow_html=True)
        st.subheader("📖 Your Mad Libs Story:")
        st.write(story)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please fill out all the fields to generate a story!")

