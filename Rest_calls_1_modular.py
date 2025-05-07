import requests
from requests.auth import HTTPBasicAuth

def send_payload(device, payload):
    """
    Sends a payload to a Juniper device via REST API.
    """
    url = f"http://{device['ip']}:{device['port']}/rpc/"
    headers = {
        "Content-Type": "application/xml",
        "Accept": "application/xml"
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            data=payload,
            auth=HTTPBasicAuth(device['username'], device['password'])
        )

        print(f"\nSent to {device['name']} - Status: {response.status_code}")
        print(response.text)
        return response.status_code, response.text

    except requests.exceptions.RequestException as e:
        print(f"\n[ERROR] Could not send to {device['name']}: {e}")
        return None, str(e)


def commit_configuration(device):
    """
    Commits the configuration on the device.
    """
    url = f"http://{device['ip']}:{device['port']}/rpc/"
    headers = {
        "Content-Type": "application/xml",
        "Accept": "application/xml"
    }

    commit_payload = "<commit-configuration/>"

    response = requests.post(
        url,
        headers=headers,
        data=commit_payload,
        auth=HTTPBasicAuth(device['username'], device['password'])
    )

    print(f"\nCommit on {device['name']} - Status: {response.status_code}")
    print(response.text)
    return response.status_code, response.text
