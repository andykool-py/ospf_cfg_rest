from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError, ConfigLoadError, CommitError
import yaml

# Load device info
with open("config.yaml") as f:
    config = yaml.safe_load(f)

devices = config['devices']

# Loop through vmx1 to vmx6
for device in devices:
    name = device['name']
    print(f"\n=== Connecting to {name} ===")

    try:
        # Connect to the device
        dev = Device(host=device['ip'], user=device['username'], passwd=device['password'], port=device['netconf_port'])
        dev.open()

        # Bind config utility
        dev.bind(cfg=Config)
        dev.cfg.rollback(rb_id=3)
        dev.cfg.commit()

        print(f"[SUCCESS] Rolled back and committed on {name}")

    except (ConnectError, ConfigLoadError, CommitError) as e:
        print(f"[ERROR] Failed on {name}: {e}")

    finally:
        dev.close()
