import requests
from requests.auth import HTTPBasicAuth

device_ip = "66.129.235.201"
port = "39008"
username = "jcluser"
password = "Juniper!1"

url = f"http://{device_ip}:{port}/rpc/load-configuration"
headers = {
    "Content-Type": "application/xml",
    "Accept": "application/xml"
}

# CLI-style config commands using <configuration-text>
config_payload = """
<load-configuration xmlns="http://xml.juniper.net/xnm/1.1/xnm" action="merge">
  <configuration-text>
    set protocols ospf router-id 1.1.1.49
    set protocols ospf lsa-refresh-interval 1000
    set protocols ospf area 0.0.0.1 stub
    set protocols ospf area 0.0.0.1 interface ge-0/0/0.0 priority 100
  </configuration-text>
</load-configuration>
"""

response = requests.post(
    url,
    headers=headers,
    data=config_payload,
    auth=HTTPBasicAuth(username, password)
)

print(f"Status Code: {response.status_code}")
print("Response:")
print(response.text)
