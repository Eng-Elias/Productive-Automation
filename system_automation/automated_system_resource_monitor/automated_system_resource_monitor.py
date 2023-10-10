import psutil
import time
import sys
from colorama import Fore, Style
from plyer import notification

# Predefined thresholds (you can adjust these as needed)
CPU_THRESHOLD = 70  # 70% CPU usage
MEMORY_THRESHOLD = 70  # 70% memory usage
DISK_THRESHOLD = 70  # 70% disk usage


def get_disk_usage():
    disk_usage = {}
    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        if partition.device and partition.mountpoint:
            usage = psutil.disk_usage(partition.mountpoint).percent
            disk_usage[partition.device] = usage
    return disk_usage


def print_colored_message(message, color):
    print(color + message + Style.RESET_ALL)


def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10,  # Display the notification for 10 seconds
    )


def monitor_resources():
    while True:
        # Get CPU, memory, and disk usage
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = get_disk_usage()

        # Check CPU usage
        if cpu_usage > CPU_THRESHOLD:
            print_colored_message(f"High CPU usage detected: {cpu_usage}%", Fore.RED)
            send_notification("High CPU Usage", f"CPU usage is at {cpu_usage}%")

        # Check memory usage
        if memory_usage > MEMORY_THRESHOLD:
            print_colored_message(
                f"High memory usage detected: {memory_usage}%", Fore.RED
            )
            send_notification(
                "High Memory Usage", f"Memory usage is at {memory_usage}%"
            )

        # Check disk usage
        for device, usage in disk_usage.items():
            if usage > DISK_THRESHOLD:
                print_colored_message(
                    f"High disk usage detected on {device}: {usage}%", Fore.RED
                )
                send_notification(
                    f"High Disk Usage on {device}", f"Disk usage is at {usage}%"
                )

        # Sleep for a short duration before checking again
        time.sleep(420)


if __name__ == "__main__":
    try:
        monitor_resources()
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
        sys.exit(0)
