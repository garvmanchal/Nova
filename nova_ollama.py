import requests

def ask_nova(prompt):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": f"You are Nova, a smart AI assistant created by Garv. You speak in a friendly Hinglish tone. Answer shortly and helpfully.\nUser: {prompt}\nNova:",
        "stream": False
    }

    try:
        response = requests.post(url, json=data)
        return response.json().get("response", "No response from AI")
    except Exception as e:
        return f"Error: {e}"