import requests
import json

# Define the API endpoint URL
url = "http://127.0.0.1:1234/v1/chat/completions"

# Create a user message in the required format
user_message = {
    "model": "deepseek-r1-distill-qwen-7b",
    "messages": [
        {
            "role": "user",
            "content": "Hello! How can I help you today?"
        }
    ]
}

# Send a POST request to the API with the user message
response = requests.post(url, json=user_message)

# Handle any exceptions or errors
try:
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}")

    # Parse the JSON response and extract the reply
    response_text = response.json()
    reply = response_text.get("choices", [{}])[0].get("message", {}).get("content")
    
    print("Received reply:", reply)
except requests.exceptions.RequestException as e:
    print(f"Request failed with error: {str(e)}")

# Close the connection explicitly to prevent resource leaks
response.close()