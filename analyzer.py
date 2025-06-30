import re

def check_password_strength(password):
    if not password.strip():
        return "Weak", ["Password cannot be empty or just spaces"], 0
    
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        score -= 1
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

    if re.search(r"[!@#$%^&*(),.?\":{}|<>\\[\]/]", password):
        score += 1
    else:
        feedback.append("Use special characters.")

    if re.search(r"(.)\1{2,}", password):
        score -= 1
        feedback.append("Avoid repeated characters like 'aaa' or '111'.")

    common_patterns = ["1234", "password", "qwerty", "admin", "letmein"]
    if any(p in password.lower() for p in common_patterns):
        score -= 1
        feedback.append("Avoid common patterns like '1234' or 'password'.")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 5:
        strength = "Average"
    else:
        strength = "Strong"

    return strength, feedback, score

# This is the part that actually runs the check
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result, tips, score = check_password_strength(pwd)
    print(f"\nPassword Strength: {result} ({score}/6)")
    if tips:
        print("Suggestions:")
        for tip in tips:
            print(f"- {tip}")

