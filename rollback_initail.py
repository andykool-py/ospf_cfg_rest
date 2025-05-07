from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError, ConfigLoadError, CommitError
import yaml

# Load device info
with open("config.yaml") as f:
    config = yaml.safe_load(f)

devices = config['devices']

# Junos 'set' commands to delete specific interfaces and ospf
reset_cmds = [
    "delete interfaces ge-0/0/0",
    "delete interfaces ge-0/0/1",
    "delete interfaces ge-0/0/2",
    "delete interfaces ge-0/0/3",
    "delete interfaces ge-0/0/4",
    "delete interfaces lo0",
    "delete protocols ospf"
]

for device in devices:
    name = device['name']
    print(f"\n=== Resetting config on {name} ===")

    try:
        dev = Device(
            host=device['ip'],
            user=device['username'],
            passwd=device['password'],
            port=device['netconf_port']
        )
        dev.open()
        dev.bind(cfg=Config)
        dev.cfg.lock()

        for cmd in reset_cmds:
            try:
                dev.cfg.load(cmd, format="set")
                print(f"[{name}] Loaded: {cmd}")
            except ConfigLoadError as e:
                if "statement not found" in str(e):
                    print(f"[{name}] Skipped (not found): {cmd}")
                else:
                    print(f"[{name}] ERROR loading cmd: {cmd} => {e}")

        dev.cfg.commit()
        print(f"[{name}] Configuration committed successfully.")

    except (ConnectError, CommitError) as e:
        print(f"[ERROR] on {name}: {e}")

    finally:
        try:
            dev.cfg.unlock()
        except:
            pass
        dev.close()
