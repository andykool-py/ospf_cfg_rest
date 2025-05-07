import requests
from requests.auth import HTTPBasicAuth

device_ip = "66.129.235.200"
port = "42008"
username = "jcluser"
password = "Juniper!1"
url = f"http://{device_ip}:{port}/rpc"

# --- OSPF MULTI-AREA CONFIGURATION ---
# Replace interface names with your actual interface names!
config_xml = """
<configuration>
  <protocols>
    <ospf>
      <area>
        <name>0.0.0.0</name>
        <interface>
          <name>ge-0/0/0</name>
        </interface>
      </area>
      <area>
        <name>1.1.1.1</name>
        <interface>
          <name>ge-0/0/1</name>
        </interface>
      </area>
    </ospf>
  </protocols>
</configuration>
"""

# --- BUILD THE LOAD-CONFIGURATION RPC ---
load_config_xml = f"""
<load-configuration action="merge">
  <configuration>
    <protocols>
      <ospf>
        <area>
          <name>0.0.0.0</name>
          <interface>
            <name>ge-0/0/0</name>
          </interface>
        </area>
        <area>
          <name>0.0.0.1</name>
          <interface>
            <name>ge-0/0/1</name>
          </interface>
        </area>
      </ospf>
    </protocols>
  </configuration>
</load-configuration>
"""

headers = {
    "Content-Type": "application/xml",
    "Accept": "application/xml"
}

# --- LOAD CONFIGURATION ---
response = requests.post(
    url,
    auth=HTTPBasicAuth(username, password),
    headers=headers,
    data=load_config_xml
)
print("Load Configuration Status:", response.status_code)
print("Load Configuration Response:\n", response.text)

# --- COMMIT CONFIGURATION ---
commit_xml = "<commit/>"
commit_response = requests.post(
    url,
    auth=HTTPBasicAuth(username, password),
    headers=headers,
    data=commit_xml
)
print("\nCommit Status:", commit_response.status_code)
print("Commit Response:\n", commit_response.text)

# --- OPTIONAL: VERIFY OSPF CONFIGURATION ---
verify_xml = """
<get-configuration>
  <configuration>
    <protocols>
      <ospf/>
    </protocols>
  </configuration>
</get-configuration>
"""
verify_response = requests.post(
    url,
    auth=HTTPBasicAuth(username, password),
    headers=headers,
    data=verify_xml
)
print("\nOSPF Configuration Verification:\n", verify_response.text)