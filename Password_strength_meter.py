def password_strength(password: str) -> tuple[str, str]:

    score = 0
    feedback = []
    special_chars = set('!@#$%^&*')

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make your password at least 8 characters long.")

    # Check uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include digits (0-9).")

    # Check special characters
    if any(c in special_chars for c in password):
        score += 1
    else:
        feedback.append("Include special characters (!@#$%^&*).")

    # Determine strength label
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Provide feedback only if password is weak
    if strength == "Weak":
        feedback_text = " ".join(feedback)
    elif strength == "Moderate":
        feedback_text = "Your password is okay but could be stronger."
    else:
        feedback_text = "Your password is strong. Great job!"

    return strength, feedback_text


def main():
    print("Welcome to Password Strength Meter!")
    print("A strong password should:")
    print("✅ Be at least 8 characters long")
    print("✅ Contain uppercase & lowercase letters")
    print("✅ Include at least one digit (0-9)")
    print("✅ Have one special character (!@#$%^&*)")
    
    password = input("Enter your password: ")

    strength, feedback = password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print(f"Feedback: {feedback}")


if __name__ == "__main__":
    main()