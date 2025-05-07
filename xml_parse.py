import xml.etree.ElementTree as ET

def parse_ping_results(xml_data):
    ns = {'junos': 'http://xml.juniper.net/junos/21.1R0/junos-probe-tests'}
    root = ET.fromstring(xml_data)

    try:
        summary = root.find('junos:probe-results-summary', ns)
        loss = summary.find('junos:packet-loss', ns).text
        rtt_avg = summary.find('junos:rtt-average', ns).text
        probes = summary.find('junos:probes-sent', ns).text
        responses = summary.find('junos:responses-received', ns).text

        print(f"📡 Ping Success: {responses}/{probes} received")
        print(f"📉 Packet Loss: {loss}")
        print(f"⏱️ Avg RTT: {rtt_avg} ms")
        return {
            "probes_sent": int(probes),
            "responses": int(responses),
            "loss": int(loss),
            "rtt_avg": int(rtt_avg)
        }

    except Exception as e:
        print(f"❌ Failed to parse ping output: {e}")
        return None
