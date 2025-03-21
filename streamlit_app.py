import streamlit as st
import time
from frontend.Disease_Prediction import load_page

st.set_page_config(page_title="Health Prediction", layout="wide")

# Define session state to track animation
if "animation_done" not in st.session_state:
    st.session_state.animation_done = False

# Simulating heart animation first
if not st.session_state.animation_done:
    # Define the CSS and JS animation
    animation_css = """
    <style>
    @keyframes heartbeat {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.2); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }

    @keyframes explode {
        0% { transform: scale(1); opacity: 1; }
        100% { transform: scale(5); opacity: 0; visibility: hidden; }
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Center the animation */
    #heart-container {
        position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: 100%;
    }

    .heart {
        width: 100px;
        height: 100px;
        background-color: red;
        position: relative;
        transform: rotate(-45deg);
        animation: heartbeat 1s infinite;
        box-shadow: 0 0 10px red;
    }

    .heart:before,
    .heart:after {
        content: "";
        width: 100px;
        height: 100px;
        background-color: red;
        border-radius: 50%;
        position: absolute;
    }

    .heart:before { top: -50px; left: 0; }
    .heart:after { left: 50px; top: 0; }

    /* Explosion effect */
    .explode {
        animation: explode 0.8s forwards;
    }

    /* Text after explosion */
    #prediction-text {
        font-size: 36px;
        font-weight: bold;
        color: white;
        text-align: center;
        opacity: 0;
        animation: fadeIn 1s ease-in-out 1.5s forwards;
    }

    /* Button */
    #start-btn {
        display: none;
        padding: 12px 24px;
        font-size: 18px;
        background-color: #ff4757;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        margin-top: 20px;
        animation: fadeIn 1s ease-in-out 2.5s forwards;
    }
    </style>
    """

    # JavaScript for triggering explosion
    animation_js = """
    <script>
    setTimeout(() => {
        document.querySelector('.heart').classList.add('explode');
        setTimeout(() => {
            document.getElementById('prediction-text').style.opacity = '1';
            document.getElementById('start-btn').style.display = 'block';
        }, 900);
    }, 2500);
    </script>
    """

    # Injecting CSS
    st.markdown(animation_css, unsafe_allow_html=True)

    # Injecting HTML (Heart + Text + Button)
    st.markdown("""
    <div id="heart-container">
        <div class="heart"></div>
        <p id="prediction-text">Disease Prediction</p>
        <a href="/Disease_Prediction" target="_self">
            <button id="start-btn">Start Predicting</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Injecting JavaScript
    st.markdown(animation_js, unsafe_allow_html=True)
    time.sleep(3)  # Simulating animation time
    st.session_state.animation_done = True
    st.rerun()  # Reload after animation

time.sleep(0.5)
# Redirect button
load_page()