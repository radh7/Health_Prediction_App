import streamlit as st
from streamlit_option_menu import option_menu
from frontend.heart_disease_prediction import heart_disease_prediction_tab

def load_page():
    #sidebar for navigation
    with st.sidebar:
        selected = option_menu('Disease Prediction',
                               ['Heart Disease',
                                        'Diabetes',
                                        'Asthma'],
                               icons=['heart beat', 'heart', 'breath'],
                               default_index=0)
    #heart disease prediction
    if (selected == 'Heart Disease'):
        # Streamlit UI
        st.title("Heart Disease Prediction Using ML")
        heart_disease_prediction_tab()

    elif (selected== 'Diabetes'):
        # Streamlit UI
        st.title("Diabetes Prediction Using ML")
        st.text("Coming Soon...")

    elif (selected== 'Asthma'):
        # Streamlit UI
        st.title("Asthma Prediction Using ML")
        st.text("Coming Soon...")

