import requests
from requests.auth import HTTPBasicAuth

# Device and login info
device_ip = "66.129.235.202"
port = "36017"
username = "jcluser"
password = "Juniper!1"

# Use the general /rpc/ endpoint like your working curl
url = f"http://{device_ip}:{port}/rpc/"

headers = {
    "Content-Type": "application/xml",
    "Accept": "application/xml"
}

# Same payload as your working curl command
xml_payload = """
<load-configuration action="merge">
  <configuration>
    <interfaces>
      <interface>
        <name>ge-0/0/0</name>
        <unit>
          <name>0</name>
          <family>
            <inet>
              <address>
                <name>100.10.0.1/24</name>
              </address>
            </inet>
          </family>
        </unit>
      </interface>
      <interface>
        <name>ge-0/0/1</name>
        <unit>
          <name>0</name>
          <family>
            <inet>
              <address>
                <name>100.10.1.1/24</name>
              </address>
            </inet>
          </family>
        </unit>
      </interface>
      <interface>
        <name>ge-0/0/2</name>
        <unit>
          <name>0</name>
          <family>
            <inet>
              <address>
                <name>100.10.2.1/24</name>
              </address>
            </inet>
          </family>
        </unit>
      </interface>
      <interface>
        <name>ge-0/0/3</name>
        <unit>
          <name>0</name>
          <family>
            <inet>
              <address>
                <name>100.10.3.1/24</name>
              </address>
            </inet>
          </family>
        </unit>
      </interface>
    </interfaces>
  </configuration>
</load-configuration>
"""
ospf_payload = """
<load-configuration action="merge">
  <configuration>
    <protocols>
      <ospf>
        <area>
          <name>0.0.0.0</name>
          <interface>
            <name>ge-0/0/0.0</name>
          </interface>
          <interface>
            <name>ge-0/0/1.0</name>
          </interface>
        </area>
        <area>
          <name>0.0.0.1</name>
          <interface>
            <name>ge-0/0/2.0</name>
          </interface>
          <interface>
            <name>ge-0/0/3.0</name>
          </interface>
        </area>
      </ospf>
    </protocols>
  </configuration>
</load-configuration>

"""

# Send the config
response = requests.post(
    url,
    headers=headers,
    data=ospf_payload,
    auth=HTTPBasicAuth(username, password)
)

print("Response Status:", response.status_code)
print(response.text)

# Commit step (send to /rpc/ as well)
commit_payload = """<commit-configuration/>"""
commit_response = requests.post(
    url,
    headers=headers,
    data=commit_payload,
    auth=HTTPBasicAuth(username, password)
)

print("\nCommit Response Status:", commit_response.status_code)
print(commit_response.text)
