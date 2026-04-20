# capture/sniffer.py
# -------------------------------------------------------
# OWNER: Jaineel (packet capture & infrastructure)
# CONTRIBUTOR: Nicholas (feature extraction & ML integration)
# -------------------------------------------------------

from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

def process_packet(packet):
    """
    Called automatically for every packet captured.
    Jaineel: handles raw packet parsing
    Nicholas: will later extract ML features from each packet
    """
    if IP in packet:
        src_ip = packet[IP].src        # where the packet came from
        dst_ip = packet[IP].dst        # where the packet is going
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
        timestamp = datetime.now().strftime("%H:%M:%S")

        print(f"[{timestamp}] {protocol} | {src_ip} --> {dst_ip}")

def start_capture(interface=None, count=20):
    """
    Starts the packet sniffer.
    - interface: which network interface to listen on (None = default)
    - count: how many packets to capture before stopping
    Nicholas: count will eventually feed into the ML pipeline
    """
    print("Starting packet capture...")
    print("=" * 50)
    sniff(iface=interface, prn=process_packet, count=count, store=False)
    print("=" * 50)
    print("Capture complete.")

if __name__ == "__main__":
    # Entry point — run this file directly to start capturing
    start_capture()