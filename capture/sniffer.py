# capture/sniffer.py
# -------------------------------------------------------
# OWNER: Jaineel (packet capture & infrastructure)
# NOTE FOR NICHOLAS: feature extraction can be added
#                    to process_packet() once capture is working
# -------------------------------------------------------

from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime
from capture.logger import init_log_file, get_log_filename, log_packet


# called automatically for every packet captured
# handles raw packet parsing and hands off to logger
def process_packet(packet, filename):
    if IP in packet:
        src_ip = packet[IP].src        # where the packet came from
        dst_ip = packet[IP].dst        # where the packet is going
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
        timestamp = datetime.now().strftime("%H:%M:%S")

        print(f"[{timestamp}] {protocol} | {src_ip} --> {dst_ip}")

        # log the packet to CSV
        log_packet(packet, filename)


# starts the packet sniffer and logger together
# interface: which network interface to listen on (None = default)
# count: how many packets to capture before stopping
def start_capture(interface=None, count=20):
    # create a new log file for this capture session
    filename = init_log_file(get_log_filename())

    print("Starting packet capture...")
    print("=" * 50)
    sniff(iface=interface, prn=lambda pkt: process_packet(pkt, filename), count=count, store=False)
    print("=" * 50)
    print(f"Capture complete. Data saved to: {filename}")


# entry point — run this file directly to start capturing
if __name__ == "__main__":
    start_capture()