import os
import shutil
from datetime import datetime, timedelta
import platform


def get_downloads_folder():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Linux":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Darwin":  # MacOS
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Android":
        return "/sdcard/Download"  # Example path for Android Downloads
    else:
        raise NotImplementedError(f"Unsupported operating system: {system}")


def cleanup_downloads_folder(days_threshold):
    downloads_path = get_downloads_folder()
    now = datetime.now()
    threshold_date = now - timedelta(days=days_threshold)

    for root, dirs, files in os.walk(downloads_path):
        for file in files:
            file_path = os.path.join(root, file)
            last_access_time = datetime.fromtimestamp(os.path.getatime(file_path))

            if last_access_time < threshold_date:
                try:
                    # Determine the destination directory in the archive folder
                    relative_path = os.path.relpath(root, downloads_path)
                    archive_dir = os.path.join(downloads_path, "Archive", relative_path)

                    # Create the corresponding directory structure in the archive folder
                    os.makedirs(archive_dir, exist_ok=True)

                    # Move the file to the corresponding directory in the archive folder
                    shutil.move(file_path, os.path.join(archive_dir, file))
                    print(
                        f"Moved '{file}' to '{archive_dir}' within the archive folder."
                    )
                except Exception as e:
                    print(f"Failed to move '{file}': {str(e)}")
                    # You can add more error handling here


if __name__ == "__main__":
    # Specify the number of days for the threshold
    days_threshold = 30

    cleanup_downloads_folder(days_threshold)
