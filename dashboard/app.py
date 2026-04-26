# main dashboard route — captures fresh data on every refresh
@app.route("/")
def index():
    # run capture and preprocessing sequentially, wait for both to finish
    try:
        start_capture(count=20)
        run_preprocessor()
    except Exception as e:
        print(f"[dashboard] capture error: {e}")

    # small delay to ensure file is written before reading
    import time
    time.sleep(1)

    packets = load_data()
    total = len(packets)
    tcp = sum(1 for p in packets if p["protocol"] == "TCP")
    udp = sum(1 for p in packets if p["protocol"] == "UDP")
    return render_template("index.html", packets=packets, total=total, tcp=tcp, udp=udp)