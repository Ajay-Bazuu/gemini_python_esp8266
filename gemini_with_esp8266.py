# for network connectivity
import network
import time

# for using gemini API
import urequests as requests
import json

# Replace these with your WiFi credentials
SSID = 'CyborG.net'
PASSWORD = 'Bazuu/098'

# Replace with your API key
API_KEY = "AIzaSyBIPI-iB7HwZcR7XVmY68KGxoXsIZBCZOQ"
# Replace with your desired model endpoint
MODEL_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + API_KEY
# Define the max output tokens
MAX_TOKENS = 200

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # Wait for connection
    timeout = 10  # seconds
    start_time = time.time()
    while not wlan.isconnected() and (time.time() - start_time) < timeout:
        time.sleep(1)
    
    if wlan.isconnected():
        print('Connected to WiFi')
        print('IP address:', wlan.ifconfig()[0])
        return wlan
    else:
        print('Failed to connect to WiFi')
        return None

def ask_question(question):

        # Prepare the request payload
        payload = {
            "contents": [{
                "parts": [{
                    "text": question
                }]
            }],
            "generationConfig": {
                "maxOutputTokens": MAX_TOKENS
            }
        }
    
        # Send POST request
        headers = {"Content-Type": "application/json"}
        response = requests.post(MODEL_URL, headers=headers, data=json.dumps(payload))
        
        # Check if the request was successful
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        
        # Parse the JSON response
        result = response.json()
        
        # Check if the result contains the expected fields
        if "candidates" in result and len(result["candidates"]) > 0:
            answer = result["candidates"][0]["content"]["parts"][0]["text"]
            # Clean the answer
            return answer.strip()
        else:
            print("Unexpected response format.")
            return None


if __name__ == "__main__":
    wlan = connect_wifi(SSID, PASSWORD)
    if wlan and wlan.isconnected():
        while True:
            # For testing, you can hardcode the question or use another method to get input
            question = input("Ask your question: ")
            answer = ask_question(question)
            if answer:
                print("Here is your answer:")
                print(answer)
            else:
                print("Failed to get an answer.")
            time.sleep(10)  # Wait before making another request
    else:
        print('Not connected to WiFi. Cannot make API requests.')

