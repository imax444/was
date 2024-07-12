import requests

# URL of your Flask server
url = "http://127.0.0.1:5000/"
get_message_url = "http://127.0.0.1:5000/get_message"

# Function to get public IP address
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json()['ip']
        return ip
    except Exception as e:
        print(f"Error getting public IP: {e}")
        return None

# Function to get the current message from the server
def get_server_message():
    try:
        response = requests.get(get_message_url)
        if response.status_code == 200:
            message = response.json().get('message')
            return message
        else:
            print(f"Failed to get server message: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error getting server message: {e}")
        return None

# Function to send IP address to Flask server
def send_ip_to_server(ip):
    try:
        response = requests.post(url, data={'plzdont': ip})
        if response.status_code == 200:
            print("IP address sent successfully!")
        else:
            print(f"Failed to send IP address: {response.status_code}")
    except Exception as e:
        print(f"Error sending IP address: {e}")

# Main logic
if __name__ == "__main__":
    ip_address = get_public_ip()
    if ip_address:
        server_message = get_server_message()
        if server_message != ip_address:
            send_ip_to_server(ip_address)
        else:
            print("IP address on server is up to date.")
    else:
        print("No IP address to send.")
