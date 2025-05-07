import yaml
from jinja2 import Template

with open("Config.yaml","r") as file:
    config = yaml.safe_load(file)

with open("payload.yaml","r") as file:
    payload = yaml.safe_load(file)

vmx1 = config['devices'][0]
# vmx2 = config['devices'][1]
# vmx3 = config['devices'][2]
# vmx4 = config['devices'][3]
# print(vmx1)
#
# vmx1_ip = vmx1['ip']
# print(vmx1_ip)

vmx1_interfaces_ge0 = vmx1['interfaces']
print(vmx1_interfaces_ge0[1]['name'], vmx1_interfaces_ge0[1]['ip'])

# raw_template = payload['ip_config_single']['template']
#
# template = Template(raw_template)
# rendered_payload = template.render(
#     name=vmx1_interfaces_ge0[1]['name'],
#     address=vmx1_interfaces_ge0[1]['ip']
# )

# print(rendered_payload)

print("#"*100)

vmx1_interfaces = vmx1['interfaces'][:4]
print(vmx1_interfaces)

raw_template_int4 = payload['ip_config_multiple']['template']
temp4 = Template(raw_template_int4)


Interface_cfg_vmx1 = temp4.render(interfaces=vmx1_interfaces)
print(Interface_cfg_vmx1)

ospf_template4 = payload['ospf_config_clean']['template']
ospf_template = Template(ospf_template4)

ospf_cfg_vmx1 = ospf_template.render(interfaces=vmx1['interfaces'], router_id=vmx1["router-id"])
print(ospf_cfg_vmx1)
