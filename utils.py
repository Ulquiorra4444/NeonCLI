import platform
import random
import string
import requests

def system_info():
    print("\n--- SYSTEM INFORMATION ---")
    print("OS:", platform.system())
    print("Version:", platform.version())
    print("Machine:", platform.machine())

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))

def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = response.json()
        return f"{data['setup']} - {data['punchline']}"
    except:
        return "Failed to fetch joke."
