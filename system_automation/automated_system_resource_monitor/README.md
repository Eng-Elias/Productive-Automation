# Automated System Resource Monitor

This project includes scripts to monitor system resources and send alerts if usage exceeds predefined thresholds. It provides a way to optimize system performance and prevent slowdowns due to high resource usage.

## Files

- `automated_system_resource_monitor.py`: Python script to monitor CPU, memory, and disk usage, and send alerts if thresholds are exceeded.
- `automated_system_resource_monitor.bat`: Windows batch script to run the Python script on Windows systems.
- `automated_system_resource_monitor.sh`: Shell script to run the Python script on Unix-like systems.

## Usage

### Windows

1. Double-click `automated_system_resource_monitor.bat` to run the monitor script on a Windows system. (can run using CMD too).
2. The script will install necessary dependencies and monitor system resources.
3. It will display high usage alerts in red text and push system notification.

### Unix-like Systems (Linux, MacOS)

1. Run the following command to make the script executable:

   ```bash
   chmod +x automated_system_resource_monitor.sh
   ```

2. Terminal: Open a terminal and navigate to the folder containing `automated_system_resource_monitor.sh`.
3. GUI: Double-click `automated_system_resource_monitor.sh`.
4. The script will install necessary dependencies and monitor system resources.
5. It will display high usage alerts in red text and push system notification.

## Dependencies

- Python 3.x
- [psutil](https://pypi.org/project/psutil/)
- [colorama](https://pypi.org/project/colorama/)
- [plyer](https://pypi.org/project/plyer/)

Make sure to install the required dependencies using `pip` before running the scripts.

## Configuration

You can adjust the predefined thresholds for CPU, memory, and disk usage in the Python script `automated_system_resource_monitor.py`.

```python
CPU_THRESHOLD = 70  # 70% CPU usage
MEMORY_THRESHOLD = 70  # 70% memory usage
DISK_THRESHOLD = 70  # 70% disk usage
```
