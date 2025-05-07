# rest_client.py
"""
This module provides helper functions to send XML-based REST API payloads
to Juniper devices for configuration and commit operations.

Functions:
- send_payload: Sends a given configuration payload to a Juniper device.
- commit_configuration: Sends a commit command to finalize candidate configuration.
"""

import requests
from requests.auth import HTTPBasicAuth
from colorama import Fore, Style, init

# ───────────────────────────────────────────────────────────────
# Sends XML Payload via REST to Juniper RPC endpoint
# ───────────────────────────────────────────────────────────────
def send_payload(device, payload):
    """
    Sends a payload to a Juniper device via REST API.

    Args:
        device (dict): Device connection info from config.yaml
        payload (str): Jinja2-rendered XML payload

    Returns:
        tuple: (status_code, response_text)
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

        status_color = (
            Fore.GREEN if response.status_code == 200 else
            Fore.YELLOW if 400 <= response.status_code < 500 else
            Fore.RED
        )

        print(f"\n{status_color}[REST] Sent to {device['name']} - Status: {response.status_code}")
        print(response.text)
        return response.status_code, response.text

    except requests.exceptions.RequestException as e:
        print(f"\n[ERROR] REST call to {device['name']} failed: {e}")
        return None, str(e)

# ───────────────────────────────────────────────────────────────
# Sends Commit Operation
# ───────────────────────────────────────────────────────────────
def commit_configuration(device):
    """
    Sends a commit-configuration RPC to the device via REST API.

    Args:
        device (dict): Device connection info from config.yaml

    Returns:
        tuple: (status_code, response_text)
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

    status_color = (
        Fore.GREEN if response.status_code == 200 else
        Fore.YELLOW if 400 <= response.status_code < 500 else
        Fore.RED
    )

    print(f"\n{status_color}[REST] Commit on {device['name']} - Status: {response.status_code}")
    print(response.text)
    return response.status_code, response.text
