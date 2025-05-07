import time

from rest_runner import configure_all_devices
from verify_ping import verify_all_device_pings
from time import sleep

def main():
    print("\n🚀 Starting Full Configuration and Verification Process...\n")

    # Step 1: Configure interfaces + OSPF on all devices
    config_results = configure_all_devices()

    print("\n📋 Configuration Summary:")
    for line in config_results:
        print("•", line)

    # Wait for OSPF to converge
    print("Wait for OSPF to converge")
    time.sleep(120)

    # Step 2: Verify loopback reachability across all devices
    print("\n🔍 Starting Ping Verification...\n")
    ping_results = verify_all_device_pings()

    print("\n📋 Ping Summary:")
    for result in ping_results:
        print(f"{result['source']} → {result['target']} ({result['target_ip']}): "
              f"Loss = {result['packet_loss']}%, Avg RTT = {result['rtt_avg']} ms")

    print("\n✅ Process Complete.\n")

if __name__ == "__main__":
    main()
