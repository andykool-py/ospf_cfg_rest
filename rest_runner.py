from Config_ospf_modular_2 import interface_payloads, ospf_payloads, devices
from Rest_calls_1_modular import send_payload, commit_configuration

# Get vmx1 and its payloads
vmx1 = devices["vmx1"]
print(vmx1)
vmx1_interface_payload = interface_payloads["vmx1"]
print(vmx1_interface_payload)
vmx1_ospf_payload = ospf_payloads["vmx1"]
print(vmx1_ospf_payload)



# # Send interface config
# print("\n=== Sending Interface Config to vmx1 ===")
# send_payload(vmx1, vmx1_interface_payload)
#
# # Send OSPF config
# print("\n=== Sending OSPF Config to vmx1 ===")
# send_payload(vmx1, vmx1_ospf_payload)
#
# # Commit config
# print("\n=== Committing Config on vmx1 ===")
# commit_configuration(vmx1)
