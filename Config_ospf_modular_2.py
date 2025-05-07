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