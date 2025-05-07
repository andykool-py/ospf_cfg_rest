# import yaml
# from jinja2 import Template
#
# # Load YAML files
# with open("config.yaml") as f:
#     config = yaml.safe_load(f)
#
# with open("payload.yaml") as f:
#     payloads = yaml.safe_load(f)
#
#
# # ---------- Helper Functions ----------
#
# def get_device_interfaces(config, device_name):
#     for device in config['devices']:
#         if device['name'] == device_name:
#             return device['interfaces']
#     raise ValueError(f"Device '{device_name}' not found.")
#
#
# def get_router_id(config, device_name):
#     for device in config['devices']:
#         if device['name'] == device_name:
#             return device.get('router-id', '1.1.1.1')
#     raise ValueError(f"Device '{device_name}' not found.")
#
#
# # ---------- Payload Rendering Functions ----------
#
# def generate_interface_config_payload(template_string, interfaces):
#     template = Template(template_string)
#     return template.render(interfaces=interfaces)
#
#
# def generate_ospf_config_payload(template_string, interfaces, router_id):
#     template = Template(template_string)
#     return template.render(interfaces=interfaces, router_id=router_id)
#
#
# # ---------- Device-Level Generator Wrappers ----------
#
# def build_interface_payload_for_device(config, payloads, device_name):
#     interfaces = get_device_interfaces(config, device_name)
#     template_string = payloads["interface_config"]["template"]
#     return generate_interface_config_payload(template_string, interfaces)
#
#
# def build_ospf_payload_for_device(config, payloads, device_name):
#     interfaces = get_device_interfaces(config, device_name)
#     router_id = get_router_id(config, device_name)
#     template_string = payloads["ospf_config"]["template"]
#     return generate_ospf_config_payload(template_string, interfaces, router_id)
#
#
# # ---------- Main Loop (Optional) ----------
#
# # Loop through all devices and print their payloads
# for device in config['devices']:
#     name = device['name']
#
#     print(f"\n==== Interface Config for {name} ====")
#     iface_payload = build_interface_payload_for_device(config, payloads, name)
#     print(iface_payload)
#
#     print(f"\n==== OSPF Config for {name} ====")
#     ospf_payload = build_ospf_payload_for_device(config, payloads, name)
#     print(ospf_payload)

import yaml
from jinja2 import Template


# ---------- Load YAML Files ----------

with open("Config.yaml") as f:
    config = yaml.safe_load(f)


with open("payload.yaml") as f:
    payloads = yaml.safe_load(f)

# ---------- Instantiate Devices ----------

devices = {d['name']: d for d in config['devices']}

# ---------- Templating Functions ----------

def generate_interface_config_payload(template_string, interfaces):
    template = Template(template_string)
    return template.render(interfaces=interfaces)

def generate_ospf_config_payload(template_string, interfaces, router_id):
    template = Template(template_string)
    return template.render(interfaces=interfaces, router_id=router_id)

# ---------- Device-Level Wrapper ----------

def build_interface_payload(device, template_string):
    return generate_interface_config_payload(template_string, device['interfaces'])

def build_ospf_payload(device, template_string):
    return generate_ospf_config_payload(template_string, device['interfaces'], device["router-id"])

# ---------- Main Execution ----------

# Grab templates
interface_template = payloads["interface_config"]["template"]
ospf_template = payloads["ospf_config"]["template"]

interface_payloads = {}
ospf_payloads = {}

for i in range(1, len(config['devices']) + 1):
    name = f"vmx{i}"
    device = devices[name]

    interface_payloads[name] = build_interface_payload(device, interface_template)
    ospf_payloads[name] = build_ospf_payload(device, ospf_template)

# print(interface_payloads['vmx3'])