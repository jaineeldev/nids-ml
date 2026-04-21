# main.py
# -------------------------------------------------------
# OWNER: Jaineel (entry point & project orchestration)
# NOTE FOR NICHOLAS: add model inference call here
#                    once your model is trained and saved
# -------------------------------------------------------

import argparse
from capture.sniffer import start_capture
from pipeline.preprocessor import run_preprocessor


# sets up command line arguments so you can customise the capture
# usage examples:
#   py main.py
#   py main.py --count 100
#   py main.py --count 50 --interface WiFi
def get_args():
    parser = argparse.ArgumentParser(description="NIDS-ML — Network Intrusion Detection System")
    parser.add_argument(
        "--count",
        type=int,
        default=20,
        help="Number of packets to capture (default: 20)"
    )
    parser.add_argument(
        "--interface",
        type=str,
        default=None,
        help="Network interface to capture on (default: auto)"
    )
    parser.add_argument(
        "--no-preprocess",
        action="store_true",
        help="Skip preprocessing after capture"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    print("=" * 50)
    print("  NIDS-ML — Network Intrusion Detection System")
    print("=" * 50)
    print(f"  Packets : {args.count}")
    print(f"  Interface: {args.interface or 'auto'}")
    print("=" * 50)

    # step 1: capture and log network traffic
    start_capture(count=args.count, interface=args.interface)

    # step 2: clean and encode the captured data for ML
    # NOTE FOR NICHOLAS: skip with --no-preprocess if you want raw data
    if not args.no_preprocess:
        run_preprocessor()