import yaml
from jinja2 import Template

with open("config.yaml") as f:
    config = yaml.safe_load(f)

with open("payload.yaml") as f:
    payloads = yaml.safe_load(f)

interface_template = payloads["interface_config"]["template"]

def get_device_interfaces(config, device_name):
    for device in config['devices']:
        if device['name'] == device_name:
            return device['interfaces']
    raise ValueError(f"Device '{device_name}' not found.")

def generate_interface_config_payload(template_string, interfaces):
    """
    Renders the interface configuration payload using a Jinja2 template.

    Args:
        template_string (str): Jinja2 template for IP configuration.
        interfaces (list): List of interface dictionaries from the config.

    Returns:
        str: Rendered XML payload ready to be sent via REST.
    """
    template = Template(template_string)
    return template.render(interfaces=interfaces)


# Get interfaces for vmx1
vmx1_interfaces = get_device_interfaces(config, "vmx1")
print(vmx1_interfaces)


vmx1_interface_payload = generate_interface_config_payload(interface_template, vmx1_interfaces)
print(vmx1_interface_payload)

