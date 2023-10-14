import speedtest
import logging
import time

# Configure logging
logging.basicConfig(
    filename="network_speed_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def run_speed_test():
    try:
        # Create a Speedtest object
        st = speedtest.Speedtest()

        # Get the best server for testing
        st.get_best_server()

        # Perform the speed test
        download_speed = st.download() / 1024 / 1024  # Convert to Mbps
        upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

        return download_speed, upload_speed
    except speedtest.SpeedtestException as e:
        logging.error(f"Speed test failed: {str(e)}")
        return None, None


def log_speed_test_results(download_speed, upload_speed):
    if download_speed is not None and upload_speed is not None:
        logging.info(f"Download Speed: {download_speed:.2f} Mbps")
        logging.info(f"Upload Speed: {upload_speed:.2f} Mbps")


if __name__ == "__main__":
    # Run the speed test every 30 minutes
    while True:
        download_speed, upload_speed = run_speed_test()
        log_speed_test_results(download_speed, upload_speed)
        print("Speed test completed. Results logged.")

        # Sleep for 30 minutes (1800 seconds)
        time.sleep(1800)
