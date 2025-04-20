import streamlit as st
import time
import pandas as pd
import random

# Set page configuration for a white theme and compact layout
st.set_page_config(page_title="TurskMind 🌟", page_icon="🪔", layout="centered")

# Custom CSS for pure white background, larger interface, and dense design
st.markdown("""
    <style>
    .main {background-color: #FFFFFF; padding: 8px;}
    h1 {color: #2c3e50; font-family: 'Arial', sans-serif; font-size: 38px; margin-bottom: 8px;}
    h2 {color: #34495e; font-size: 26px; margin-top: 8px; margin-bottom: 4px;}
    .stButton>button {background-color: #3498db; color: white; font-size: 18px; border-radius: 8px; padding: 8px; margin: 4px;}
    .stSelectbox {font-size: 16px; margin-bottom: 8px;}
    .stTextInput {font-size: 16px; margin-bottom: 8px;}
    .stTextArea {font-size: 16px; margin-bottom: 8px;}
    .stProgress .st-bo {background-color: #e74c3c;}
    .stMarkdown {font-size: 16px; line-height: 1.3;}
    .sidebar .sidebar-content {background-color: #FFFFFF;}
    </style>
""", unsafe_allow_html=True)

# App title with emojis
st.title("TurskMind: Tüürk Wellness 🌄🪔")
st.markdown("Discover Tüürk-inspired wellness to reduce stress and find balance! 🚪✨")

# Sidebar for navigation with emojis
st.sidebar.header("TurskMind Menu 🧭")
page = st.sidebar.radio("Choose a section", ["Practices 🧘‍♀️", "Affirmations 🌱", "Progress 📊", "About ℹ️"])

# Practices Section
if page == "Practices 🧘‍♀️":
    st.header("Choose Your Wellness Practice 🌟")
    
    # Define practices with durations (in seconds)
    practices = {
        "Meditation: Altai Serenity (5 min) 🏞️": 300,  # 5 minutes
        "Breathing: Pamir Winds (7 min) 🌬️": 420,    # 7 minutes
        "Ritual: Gratitude to Ancestors 🙏": 120      # 2 minutes for interactivity
    }
    
    # Select a practice
    selected_practice = st.selectbox("Select a practice", list(practices.keys()), help="Pick a Tüürk-inspired practice! 🌍")
    
    # Start practice button
    if st.button("Start Practice 🚀"):
        duration = practices[selected_practice]
        st.markdown(f"**Starting '{selected_practice}'...** 🎶")
        
        # Real-time countdown timer
        timer_placeholder = st.empty()
        progress_bar = st.progress(0)
        
        start_time = time.time()
        while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            remaining = duration - elapsed
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            timer_placeholder.markdown(f"**Time Remaining**: {minutes:02d}:{seconds:02d} ⏳")
            progress_bar.progress(min(elapsed / duration, 1.0))
            time.sleep(1)  # Update every second
        
        # Clear timer and show completion
        timer_placeholder.empty()
        progress_bar.progress(1.0)
        st.success(f"Completed '{selected_practice}'! Feel the Tüürk spirit! 🌄🎉")
    
    # Quick tips for practices
    st.markdown("**Quick Tip**: Find a quiet space to immerse in the Tüürk experience! 🕉️")

# Affirmations Section
elif page == "Affirmations 🌱":
    st.header("Tüürk Affirmations 🌟")
    st.markdown("Uplift your spirit with affirmations inspired by Tüürk wisdom! Choose, generate, or create your own. 🧠💪")
    
    # List of Tüürk-inspired affirmations
    affirmations = [
        "The strength of my ancestors flows through me 💪",
        "I am as resilient as the Altai mountains 🏔️",
        "My heart is open like the endless steppe 🌾",
        "The wisdom of the Pamir guides my path 🛤️",
        "I carry the harmony of Tüürk traditions 🎶"
    ]
    
    # Option to select or generate a random affirmation
    affirmation_option = st.radio("Choose an affirmation or get a new one", ["Select from list", "Generate random"])
    
    if affirmation_option == "Select from list":
        selected_affirmation = st.selectbox("Pick an affirmation", affirmations, help="Choose a Tüürk-inspired affirmation! 🌱")
    else:
        selected_affirmation = random.choice(affirmations)
        st.markdown(f"**Your Affirmation**: {selected_affirmation} ✨")
    
    # Save affirmation
    if st.button("Save Affirmation 💾"):
        st.success(f"Affirmation saved: '{selected_affirmation}'! Keep it close! ❤️")
    
    # Input for custom affirmation
    st.markdown("**Create Your Own Affirmation** ✍️")
    custom_affirmation = st.text_area("Write a personal affirmation inspired by Tüürk culture", height=80)
    if st.button("Save Custom Affirmation 📝"):
        if custom_affirmation:
            st.success(f"Your affirmation saved: '{custom_affirmation}'! 🥳")
        else:
            st.warning("Please enter an affirmation! 😊")

# Progress Section
elif page == "Progress 📊":
    st.header("Your Wellness Journey 📈")
    st.markdown("Track your Tüürk-inspired wellness progress! 🏆")
    
    # Mock data for progress
    progress_data = pd.DataFrame({
        "Practice": ["Meditation 🧘‍♀️", "Breathing 🌬️", "Ritual 🙏"],
        "Sessions Completed": [5, 3, 4]
    })
    
    # Display bar chart
    st.bar_chart(progress_data.set_index("Practice"), height=250)
    
    # Achievements with emojis
    st.subheader("Your Achievements 🏅")
    total_sessions = sum(progress_data["Sessions Completed"])
    if total_sessions >= 10:
        st.markdown("🌟 **Nomad's Spirit**: Completed 10+ sessions! 🎉")
    elif total_sessions >= 5:
        st.markdown("🪔 **Steppe Wanderer**: Completed 5+ sessions! 🚶‍♂️")
    else:
        st.markdown("Keep practicing to earn Tüürk-inspired badges! 💪")

# About Section
else:
    st.header("About TurskMind ℹ️")
    st.markdown("""
        TurskMind is your gateway to wellness inspired by Tüürk culture, uniting traditions from Kazakhstan, Turkey, Uzbekistan, Kyrgyzstan, Azerbaijan, and Turkmenistan. 🌍  
        Enjoy **meditations** with Altai serenity, **breathing exercises** with Pamir winds, and **micro-rituals** like gratitude and affirmations rooted in Tüürk wisdom. 🧘‍♀️🙏  
        Reduce stress, enhance focus, and connect with your heritage! 🎶✨
    """)

# Footer with Tüürk proverb and emojis
st.markdown("---")
st.markdown("**Tüürk Proverb**: *The steppe teaches patience, the mountains teach strength.* 🏞️💪")