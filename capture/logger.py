# capture/logger.py
# -------------------------------------------------------
# OWNER: Jaineel (packet logging & data export)
# CONTRIBUTOR: Nicholas — logged CSV data feeds directly
#              into his ML training pipeline
# -------------------------------------------------------

import csv
import os
from datetime import datetime
from scapy.all import IP, TCP, UDP

# folder where all captured data gets saved
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
os.makedirs(LOG_DIR, exist_ok=True)


# generates a unique filename based on the current timestamp
# example: data/capture_2026-04-20_12-30-00.csv
def get_log_filename():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join(LOG_DIR, f"capture_{timestamp}.csv")


# creates the CSV file and writes the header row
# these columns are what Nicholas's ML model will train on
def init_log_file(filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "timestamp",
            "src_ip",
            "dst_ip",
            "protocol",
            "src_port",
            "dst_port",
            "packet_size"
        ])
    print(f"[logger] Log file created: {filename}")
    return filename


# extracts features from a packet and appends them to the CSV
# Jaineel: handles extraction
# Nicholas: these features will be used for ML classification
def log_packet(packet, filename):
    # skip packets that don't have an IP layer
    if IP not in packet:
        return

    timestamp = datetime.now().strftime("%H:%M:%S")
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    packet_size = len(packet)

    # extract ports based on protocol
    if TCP in packet:
        protocol = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
    elif UDP in packet:
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
    else:
        protocol = "Other"
        src_port = None
        dst_port = None

    # append the row to the CSV file
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            src_ip,
            dst_ip,
            protocol,
            src_port,
            dst_port,
            packet_size
        ])