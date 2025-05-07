from Config_ospf_modular_2 import interface_payloads, ospf_payloads, devices
from Rest_calls_1_modular import send_payload, commit_configuration


# Send configs to all devices
for i in range(1, len(devices) + 1):
    name = f"vmx{i}"
    device = devices[name]

    print(f"\n=== Sending Interface Config to {name} ===")
    send_payload(device, interface_payloads[name])

    print(f"\n=== Sending OSPF Config to {name} ===")
    send_payload(device, ospf_payloads[name])

    print(f"\n=== Committing Config on {name} ===")
    commit_configuration(device)