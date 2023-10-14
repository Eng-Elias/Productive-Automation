# Network Speed Test Automation

This script automates network speed testing and log the results periodically. The automation is achieved using Python and relevant packages.

## Files

1. **automated_network_speed_test.py**

   - Python script that performs network speed tests periodically and logs the results. It uses the `speedtest-cli` package to measure network speed.

2. **automated_network_speed_test.bat**

   - Windows batch script to install the necessary Python packages and run the `automated_network_speed_test.py` script. Double-click to execute on Windows.

3. **automated_network_speed_test.sh**

   - Unix shell script to install the required Python packages and run the `automated_network_speed_test.py` script. Execute in a terminal on Unix-based systems.

## Usage

1. **Windows:**

   - Double-click on `automated_network_speed_test.bat` to install required packages and run the speed test script.

2. **Unix-based Systems:**
   - Open a terminal and navigate to the directory containing `automated_network_speed_test.sh`.
   - Run the command: `chmod +x automated_network_speed_test.sh` to make the script executable.
   - Execute the script using: `./automated_network_speed_test.sh`.
