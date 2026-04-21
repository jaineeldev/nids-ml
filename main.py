# main.py
# -------------------------------------------------------
# OWNER: Jaineel (entry point & project orchestration)
# NOTE FOR NICHOLAS: add model inference call here
#                    once your model is trained and saved
# -------------------------------------------------------

from capture.sniffer import start_capture
from pipeline.preprocessor import run_preprocessor

# project entry point — run this file to start the NIDS
# currently runs the packet capture, logger and preprocessor
if __name__ == "__main__":
    print("=" * 50)
    print("Starting NIDS...")
    print("=" * 50)

    # step 1: capture and log network traffic
    start_capture(count=20)

    # step 2: clean and encode the captured data for ML
    run_preprocessor()