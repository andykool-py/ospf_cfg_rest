import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

def get_device_interfaces(config, device_name):
    for device in config['devices']:
        if device['name'] == device_name:
            return device['interfaces']
    raise ValueError(f"Device '{device_name}' not found.")

# Get interfaces for vmx1
vmx1_interfaces = get_device_interfaces(config, "vmx1")
print(vmx1_interfaces)

# You can now call this for vmx2, vmx3, etc.
