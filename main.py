# main.py
# -------------------------------------------------------
# OWNER: Jaineel (entry point & project orchestration)
# NOTE FOR NICHOLAS: add model inference call here
#                    once your model is trained and saved
# -------------------------------------------------------

from capture.sniffer import start_capture

# project entry point — run this file to start the NIDS
# currently runs the packet capture and logger
if __name__ == "__main__":
    print("=" * 50)
    print("Starting NIDS...")
    print("=" * 50)

    # start capturing and logging network traffic
    # count=20 is for testing, increase for real captures
    start_capture(count=20)