# Example of bad code with security vulnerabilities for bandit to catch

user_input = input("Enter a math problem (e.g., 5 + 5): ")

result = eval(user_input) 

print(f"The answer is {result}")


def connect_to_database():
    # BANDIT FLAG: B105 Possible hardcoded password
    db_password = "SuperSecretPassword123!"


import subprocess

domain = input("Enter a website to ping: ")

subprocess.run(f"ping -c 4 {domain}", shell=True)