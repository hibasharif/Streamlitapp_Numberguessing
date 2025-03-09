import streamlit as st
import random

# Initialize session state variables
if 'random_number' not in st.session_state:
    st.session_state.random_number = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'max_attempts' not in st.session_state:
    st.session_state.max_attempts = None
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Streamlit UI Enhancements
st.markdown("""
    <style>
    .main {background-color: #f4f4f4;}
    .stButton>button {background-color: #4CAF50; color: white; font-size: 18px;}
    .stTextInput>div>div>input {font-size: 16px;}
    .stSelectbox>div>div>select {font-size: 16px;}
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 Number Guessing Game")
st.subheader("🌟 Can you guess the secret number?")
st.write("Select difficulty, set your range, and start guessing!")

# Difficulty levels
difficulty = st.selectbox("⚙️ Select Difficulty:", ["Easy", "Medium", "Hard"], index=0)

# Set max attempts based on difficulty
if difficulty == "Easy":
    max_attempts = 10
elif difficulty == "Medium":
    max_attempts = 7
else:
    max_attempts = 5

st.session_state.max_attempts = max_attempts

# Set custom range
min_val = st.number_input("🔢 Enter minimum number:", min_value=1, value=1)
max_val = st.number_input("🔢 Enter maximum number:", min_value=min_val + 1, value=100)

if st.button("🚀 Start New Game"):
    st.session_state.random_number = random.randint(min_val, max_val)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.success("🎮 New game started! Try guessing the number.")

if st.session_state.random_number is not None and not st.session_state.game_over:
    guess = st.number_input("🎯 Enter your guess:", min_value=min_val, max_value=max_val, step=1)
    if st.button("🔍 Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.random_number:
            st.warning("📉 Too low! Try again.")
        elif guess > st.session_state.random_number:
            st.warning("📈 Too high! Try again.")
        else:
            st.balloons()
            st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True

        if st.session_state.attempts >= st.session_state.max_attempts and not st.session_state.game_over:
            st.error(f"❌ Game Over! The correct number was {st.session_state.random_number}.")
            st.session_state.game_over = True

st.write(f"📊 Attempts: **{st.session_state.attempts} / {st.session_state.max_attempts}**")

if st.session_state.game_over and st.button("🔄 Play Again"):
    st.session_state.random_number = None
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.experimental_rerun()
