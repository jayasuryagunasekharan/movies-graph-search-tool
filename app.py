import streamlit as st
import utils

# Page configuration
st.set_page_config(page_title="Movie Graph Search", page_icon="🎬", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-image: url("https://www.digitaltrends.com/wp-content/uploads/2023/06/netflix-home-screen-on-roku-tv.jpg?fit=1920%2C1280&p=1");
        background-size: cover;
    }
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.6);  /* Semi-transparent black overlay */
        z-index: -1;
    }
    .big-font {
        font-size: 48px !important;
        font-weight: bold;
        color: #FFD700;
        text-shadow: 2px 2px 4px #000000;
    }
    .subheader {
        color: #E0E0E0;
        font-size: 24px;
    }
    .info-box {
        background-color: rgba(0, 0, 0, 0.7);
        border-radius: 10px;
        padding: 20px;
        color: #FFFFFF;
        margin-bottom: 20px;
    }
    .result-box {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        color: #000000;
    }
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.9);
    }
    .stButton > button {
        background-color: #FFD700;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# Title and header
st.markdown("<h1 class='big-font'>🎬 Movie Graph Search Tool</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Explore the interconnected world of cinema</p>", unsafe_allow_html=True)

# Info box
st.markdown("""
<div class='info-box'>
    <h3>About this tool</h3>
    <p>I am a Graph Search tool equipped to provide insightful answers by delving into, comprehending, 
    and condensing information from the Movies GraphDatabase.</p>
</div>
""", unsafe_allow_html=True)

# Container setup
reply_container = st.container()
container = st.container()

with container:
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("Ask a question:", key='input', 
                                   placeholder="e.g., What movies connect Tom Hanks and Leonardo DiCaprio?")
        submit_button = st.form_submit_button(label='🔍 Search')
    
    # Response generation
    if submit_button and user_input:
        with st.spinner("Searching the movie graph..."):
            result = utils.main(user_input)
        
        st.markdown("""
        <div class='result-box'>
            <h3>🎞️ Search Results</h3>
            <p>{}</p>
        </div>
        """.format(result), unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='position: fixed; bottom: 0; left: 0; width: 100%; background-color: rgba(0, 0, 0, 0.7); 
            color: white; text-align: center; padding: 10px;'>
    Made with ❤️ for movie enthusiasts
</div>
""", unsafe_allow_html=True)
