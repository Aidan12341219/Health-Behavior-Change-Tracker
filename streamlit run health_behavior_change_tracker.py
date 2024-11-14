import streamlit as st
import pandas as pd
import datetime

# Set the page title and layout
st.set_page_config(page_title="Health Behavior Change Tracker", layout="wide")

# Title of the app
st.title("Health Behavior Change Tracker")

# Sidebar navigation
st.sidebar.header("Navigation")
app_mode = st.sidebar.radio("Select Mode", ["Home", "Self-Efficacy", "Stages of Change", "Physical Activity", "Results"])

# Home Page
if app_mode == "Home":
    st.header("Welcome to the Health Behavior Change Tracker")
    st.write("""
    This app helps you measure your health behavior change using theories of self-efficacy (Bandura, 1986) and stages of change (Prochaska et al., 1992). 
    It also assesses your physical activity using the **Exercise Vital Sign (EVS)**. The app will provide personalized recommendations based on your responses.
    """)

# Self-Efficacy Assessment (Bandura, 1986)
elif app_mode == "Self-Efficacy":
    st.header("Self-Efficacy Assessment")
    
    st.write("""
    Self-efficacy refers to an individual's belief in their ability to succeed in specific situations or accomplish a task. 
    This assessment will help measure your confidence in making health behavior changes.
    """)

    # Self-Efficacy scale (1-10)
    confidence = st.slider("On a scale from 1 to 10, how confident are you in your ability to make a lasting change in your health behaviors?", 1, 10, 5)
    
    if st.button("Submit Self-Efficacy Score"):
        st.session_state.confidence = confidence
        st.success(f"Your self-efficacy score is: {confidence}. Higher scores indicate greater confidence in making health changes.")

# Stages of Change (Prochaska et al., 1992)
elif app_mode == "Stages of Change":
    st.header("Stages of Change Assessment")

    st.write("""
    According to Prochaska et al. (1992), behavior change occurs in stages. This assessment will help identify your current stage of change for health behaviors.
    """)

    # Stages of Change options
    stage = st.radio("Which of the following best describes your current stage of behavior change?", 
                     ("Precontemplation", "Contemplation", "Preparation", "Action", "Maintenance"))
    
    if st.button("Submit Stage of Change"):
        st.session_state.stage = stage
        st.success(f"Your current stage of change is: {stage}.")

# Physical Activity Assessment (Exercise Vital Sign, EVS)
elif app_mode == "Physical Activity":
    st.header("Physical Activity Assessment (Exercise Vital Sign)")

    st.write("""
    The Exercise Vital Sign (EVS) is a set of questions that help assess the frequency and duration of moderate to strenuous exercise you engage in each week.
    """)

    # Frequency of Exercise (How often per week)
    exercise_frequency = st.slider("How many days per week do you engage in moderate or strenuous exercise?", 0, 7, 3)

    # Duration of Exercise (How many minutes per session)
    exercise_duration = st.slider("On average, how many minutes per session do you engage in moderate or strenuous exercise?", 0, 120, 30)

    if st.button("Submit Exercise Data"):
        st.session_state.exercise_frequency = exercise_frequency
        st.session_state.exercise_duration = exercise_duration
        st.success(f"You engage in exercise {exercise_frequency} days per week for an average of {exercise_duration} minutes per session.")

# Results Page
elif app_mode == "Results":
    st.header("Health Behavior Change Results")

    if 'confidence' in st.session_state:
        st.write(f"**Self-Efficacy Score**: {st.session_state.confidence}")
    else:
        st.write("Please complete the Self-Efficacy assessment first.")
    
    if 'stage' in st.session_state:
        st.write(f"**Stage of Change**: {st.session_state.stage}")
    else:
        st.write("Please complete the Stages of Change assessment first.")
    
    if 'exercise_frequency' in st.session_state and 'exercise_duration' in st.session_state:
        st.write(f"**Physical Activity**: {st.session_state.exercise_frequency} days per week, {st.session_state.exercise_duration} minutes per session.")
    else:
        st.write("Please complete the Physical Activity assessment first.")
    
    if 'confidence' in st.session_state and 'stage' in st.session_state and 'exercise_frequency' in st.session_state:
        # Based on user input, provide tailored recommendations
        st.write("\n### Recommendations:")
        
        if st.session_state.confidence < 5:
            st.write("- **Consider focusing on building confidence** in your ability to engage in health behaviors. Small, consistent actions can improve self-efficacy over time.")
        
        if st.session_state.stage == "Precontemplation":
            st.write("- **Precontemplation**: You may not yet be considering behavior change. Reflect on why a health change is important for you.")
        elif st.session_state.stage == "Contemplation":
            st.write("- **Contemplation**: You're thinking about change but not yet committed. Consider setting small, achievable goals to move forward.")
        elif st.session_state.stage == "Preparation":
            st.write("- **Preparation**: You're getting ready to make a change. Develop a clear action plan and set a start date.")
        elif st.session_state.stage == "Action":
            st.write("- **Action**: You're actively working on change. Keep track of your progress and celebrate small wins.")
        elif st.session_state.stage == "Maintenance":
            st.write("- **Maintenance**: You're maintaining your changes. Keep up the good work and consider ways to prevent relapse.")

        # Provide exercise recommendations
        if st.session_state.exercise_frequency < 3:
            st.write("- **Physical Activity**: You may benefit from increasing your exercise frequency to 3-5 days per week for optimal health benefits.")
        if st.session_state.exercise_duration < 30:
            st.write("- **Physical Activity**: Aim for at least 150 minutes of moderate exercise per week (30 minutes on most days). Consider increasing your session duration.")
        
        st.write("Keep up the great work, and continue striving for health behavior change!")

