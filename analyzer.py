import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make your password at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include some numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Use special characters.")

    common_patterns = ["1234", "password", "qwerty", "admin", "letmein"]
    if any(p in password.lower() for p in common_patterns):
        score -= 1
        feedback.append("Avoid common patterns like '1234' or 'password'.")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Average"
    else:
        strength = "Strong"

    return strength, feedback

# ✅ This is the part that actually runs the check
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result, tips = check_password_strength(pwd)
    print(f"\nPassword Strength: {result}")
    if tips:
        print("Suggestions:")
        for tip in tips:
            print(f"- {tip}")

