#  Password Strength Analyzer

This Python-based tool evaluates the strength of a given password and provides helpful feedback to improve it. It uses pattern matching and scoring logic to classify passwords as **Weak**, **Average**, or **Strong**, and it gives detailed suggestions for improvement.

---

##  Project Objectives

This project demonstrates a simple example of security automation by automating the process of password evaluation. It meets the following goals:

- Automatically checks password strength based on multiple factors
- Provides human-readable feedback to users
- Avoids relying on outdated rules (e.g., just "8 characters minimum")
- Shows how automation can reduce user-side security risks

---

##  Features

- Evaluates passwords based on:
  - Length (8 minimum, 12+ preferred)
  - Use of uppercase and lowercase characters
  - Presence of numbers
  - Inclusion of special characters
  - Avoidance of repeated characters (e.g., "aaa")
  - Avoidance of weak/common patterns (e.g., "1234", "password", etc.)
- Ignores empty or space-only input
- Scores the password out of 6 points and gives a rating:
  - **Weak** (0–2)
  - **Average** (3–5)
  - **Strong** (6+)
- Provides clear feedback suggestions based on what’s missing

---

##  How to Set Up and Run

###  Requirements

- Python 3.6 or higher
- No third-party dependencies (only built-in `re` module is used)

###  Running the Script

1. Clone or download the repository:
   ```bash
   git clone https://github.com/ZakStep1/password-strength-analyzer.git
   cd password-strength-analyzer


## Author

Zakary Stepniewski
