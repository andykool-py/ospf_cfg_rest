from orchestrator import configure_all_devices, verify_all_device_pings, verify_ospf_all_devices
import time

def main():
    print("\n🚀 Starting full provisioning and validation...\n")

    # configure_all_devices()
    # #Wait for OSPF to converge
    # print("Wait for OSPF to converge")
    #
    # time.sleep(120)
    # verify_all_device_pings()

    verify_ospf_all_devices()


if __name__ == "__main__":
    main()
