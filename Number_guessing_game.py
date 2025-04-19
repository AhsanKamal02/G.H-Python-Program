import streamlit as st
import random

# Function to start a new game
def start_new_game(min_value, max_value, max_attempts):
    random_number = random.randint(min_value, max_value)
    return random_number, max_attempts, 0  # random number, max attempts, current attempts

# Main function to run the Streamlit app
def main():
    st.title("Number Guessing Game")

    # Set up session state
    if 'random_number' not in st.session_state:
        st.session_state.random_number = None
    if 'max_attempts' not in st.session_state:
        st.session_state.max_attempts = None
    if 'current_attempts' not in st.session_state:
        st.session_state.current_attempts = 0

    # Difficulty levels
    difficulty = st.selectbox("Select Difficulty Level", ["Easy (10 attempts)", "Medium (7 attempts)", "Hard (5 attempts)"])
    
    if difficulty == "Easy (10 attempts)":
        max_attempts = 10
    elif difficulty == "Medium (7 attempts)":
        max_attempts = 7
    else:
        max_attempts = 5

    # Custom range input
    min_value = st.number_input("Enter minimum value:", value=1)
    max_value = st.number_input("Enter maximum value:", value=100)

    # Start a new game
    if st.button("Start New Game"):
        st.session_state.random_number, st.session_state.max_attempts, st.session_state.current_attempts = start_new_game(min_value, max_value, max_attempts)
        st.session_state.guess = None
        st.success("New game started! Guess the number between {} and {}.".format(min_value, max_value))

    # User guess input
    if st.session_state.random_number is not None:
        st.session_state.guess = st.number_input("Enter your guess:", value=0)

        if st.button("Submit Guess"):
            if st.session_state.guess < st.session_state.random_number:
                st.warning("Too low!")
            elif st.session_state.guess > st.session_state.random_number:
                st.warning("Too high!")
            else:
                st.success("Congratulations! You've guessed the number!")
                st.session_state.random_number = None  # Reset the game

            # Increment attempts
            st.session_state.current_attempts += 1

            # Check if max attempts reached
            if st.session_state.current_attempts >= st.session_state.max_attempts:
                st.error("You've reached the maximum number of attempts! The number was {}.".format(st.session_state.random_number))
                st.session_state.random_number = None  # Reset the game

            # Display attempts
            st.write("Attempts: {}/{}".format(st.session_state.current_attempts, st.session_state.max_attempts))

    # Reset game button
    if st.button("Reset Game"):
        st.session_state.random_number = None
        st.session_state.current_attempts = 0
        st.session_state.max_attempts = None
        st.success("Game has been reset!")

if __name__ == "__main__":
    main()