import network
import time

# Replace these with your WiFi credentials
SSID = 'your_SSID'
PASSWORD = 'your_PASSWORD'

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
    else:
        print('Failed to connect to WiFi')

# Call the function
connect_wifi(SSID, PASSWORD)

