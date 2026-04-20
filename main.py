# main.py
# -------------------------------------------------------
# OWNER: Jaineel (entry point & project orchestration)
# CONTRIBUTOR: Nicholas — will add model inference here
#              once training is complete
# -------------------------------------------------------


from capture.sniffer import start_capture

# project entry point — run this file to start the NIDS
# currently runs the packet capture and logger
# Nicholas please work on adding the ML inference here once you have a trained model ready

if __name__ == "__main__":
    print("=" * 50)
    print("Starting NIDS...")
    print("=" * 50)

    #start the capture and logging network traffic (captures 20 packets for testing)
    start_capture(count=20)