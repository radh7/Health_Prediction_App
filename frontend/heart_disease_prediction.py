import streamlit as st
# Set page config
#st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

import pickle
from streamlit_option_menu import option_menu
import os
import gdown


# Define model filename
model_filename = "heart_disease_model.sav"

# Google Drive file ID
file_id = "1klOzQ9FxZDRQhCNKaEeBZJsM6VQiISbL"

# Check if the model exists locally
if not os.path.exists(model_filename):
    print("Downloading model...")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", model_filename, quiet=False)
else:
    print("Model already exists locally. Skipping download.")

# Load the model once
with open(model_filename, "rb") as model_file:
    heart_disease_model = pickle.load(model_file)

print("Model Loaded Successfully!")

def heart_disease_prediction_tab():
    if heart_disease_model is None:
        st.error("⚠️ Model not loaded. Please check the file path or retrain the model.")
        return

        # Mapping Dictionaries
    general_health_mapping = {"Excellent": 5, "Very Good": 4, "Good": 3, "Fair": 2, "Poor": 1, "None": 0}
    checkup_mapping = {"Within the past year": 5, "Within the past 2 years": 4, "Within the past 5 years": 3,
                       "5 or more years ago": 2, "Never": 1}
    diabetes_mapping = {"No": 0, "Yes": 1, "No, pre-diabetes or borderline diabetes": 0.5,
                        "Yes, but female told only during pregnancy": 0.5}
    age_mapping = {"0-18": 0 "18-24": 1, "25-29": 2, "30-34": 3, "35-39": 4, "40-44": 5,
                   "45-49": 6, "50-54": 7, "55-59": 8, "60-64": 9, "65-69": 10, "70-74": 11, "75-79": 12, "80+": 13}

    # User Inputs
    col1, col2, col3 = st.columns(3)
    with col1:
        general_health = st.selectbox("General Health",
                                      list(general_health_mapping.keys()),
                                      key="general_health_1",
                                      placeholder="Choose an Option",
                                      index=None
                                      )
        age_category = st.selectbox("Age Category",
                                    list(age_mapping.keys()),
                                    key="age_category_1",
                                    placeholder="Choose an Option",
                                    index=None)
        diabetes = st.selectbox("Diabetes",
                                list(diabetes_mapping.keys()),
                                key="diabetes_1",
                                placeholder="Choose an Option",
                                index=None
                                )
        checkup = st.selectbox("Last Medical Checkup",
                               list(checkup_mapping.keys()),
                               key="checkup_1",
                               placeholder="Choose an Option",
                               index=None
                               )
        exercise = st.radio("Exercise",
                            ["No", "Yes"],
                            index=None)
        depression = st.radio("Depression",
                              ["No", "Yes"],
                              index=None)
        other_cancer = st.radio("Other Cancer",
                                ["No", "Yes"],
                                index=None)
        arthritis = st.radio("Arthritis",
                             ["No", "Yes"],
                             index=None)

    with col3:
        fried_potato = st.number_input('Fried Potato Consumption',
                                       min_value=0,
                                       max_value=200,
                                       value=None,
                                       placeholder="--")
        alcohol = st.number_input('Alcohol Consumption',
                                  min_value=0,
                                  max_value=50,
                                  value=None,
                                  placeholder="--")
        green_vegetables = st.number_input('Green Vegetables Consumption',
                                           min_value=0,
                                           max_value=200,
                                           value=None,
                                           placeholder="--")
        fruit_consumption = st.number_input('Fruit Consumption',
                                            min_value=0,
                                            max_value=200,
                                            value=None,
                                            placeholder="--")

        # Height & Weight Input
        height = st.number_input("Height (cm)",
                                 min_value=100,
                                 max_value=250,
                                 value=None,
                                 placeholder="--")
        weight = st.number_input("Weight (kg)",
                                 min_value=30,
                                 max_value=200,
                                 value=None,
                                 placeholder="--")

        # BMI Calculation & Adjustment (only if both height and weight are provided)
        if height and weight:
            calculated_bmi = weight / ((height / 100) ** 2)
        else:
            calculated_bmi = 0.0  # Default to 0 or any placeholder
        bmi = st.number_input("BMI (Auto-calculated, adjustable)",
                              min_value=0.0,
                              max_value=50.0,
                              value=round(calculated_bmi, 1),
                              placeholder="--")

    # Convert Inputs to Numeric Values
    input_data = [
        general_health_mapping.get(general_health, 0),  # Default to 0 if None
        age_mapping.get(age_category, 0),  # Default to 0 if None
        diabetes_mapping.get(diabetes, 0),  # Default to 0 if None
        fried_potato if fried_potato is not None else 0,  # Default numeric inputs to 0
        bmi if bmi is not None else 0.0,
        height if height is not None else 0,
        weight if weight is not None else 0,
        alcohol if alcohol is not None else 0,
        green_vegetables if green_vegetables is not None else 0,
        1 if exercise == "Yes" else 0,
        fruit_consumption if fruit_consumption is not None else 0,
        1 if depression == "Yes" else 0,
        checkup_mapping.get(checkup, 0),  # Default to 0 if None
        1 if other_cancer == "Yes" else 0,
        1 if arthritis == "Yes" else 0
    ]

    pop_up = st.empty()
    # Define a session state variable to track rerun status
    if "rerun" not in st.session_state:
        st.session_state.rerun = False

    if st.button("Heart Disease Test"):
        prediction = heart_disease_model.predict([input_data])
        diagnosis = "✅ No Heart Disease" if prediction[0] == 0 else "⚠️ Positive for Heart Disease"

        # Create a placeholder for the pop-up
        pop_up = st.empty()

        with pop_up.container():
            # Close button to remove the pop-up
            if st.button("Close"):
                pop_up.empty()  # Clears the pop-up when clicked
            st.markdown(
                f"""
                                <div style="
                                    position: fixed;
                                    bottom: 50%;
                                    left: 50%;
                                    transform: translate(-50%, -50%);
                                    background-color: rgba(0,0,0,0.7);
                                    color: white;
                                    padding: 20px;
                                    border-radius: 10px;
                                    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
                                    text-align: center;
                                    font-size: 24px;
                                    font-weight: bold;
                                    z-index: 1000;
                                    width: 500px;
                                ">
                                    {diagnosis} 
                </div>
                """,
                unsafe_allow_html=True
            )

        # Wait before closing pop-up
        import time
        time.sleep(10)
        pop_up.empty()

        # Set session state flag to rerun app
        st.session_state.rerun = True

    if st.session_state.rerun:
        if st.button("Refresh"):
            st.session_state.rerun = False
            st.rerun()


