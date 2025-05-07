import requests
from requests.auth import HTTPBasicAuth

# URL and credentials
device_ip = "66.129.235.200"
port = "42008"
url = f"http://{device_ip}:{port}/rpc/get-software-information"
username = "jcluser"
password = "Juniper!1"

# Headers
headers = {
    "Content-Type": "application/xml",
    "Accept": "application/xml"
}

# Make the GET request with authentication and headers
response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers)

# Print the status code and response content (XML data)
print("Status Code:", response.status_code)
print("Response Body:\n", response.text)
