import os
import shutil
import platform


def get_temporary_directories():
    system = platform.system()
    temp_dirs = []

    if system == "Windows":
        temp_dirs.append(os.path.join(os.environ["TEMP"], ""))
        temp_dirs.append(os.path.join(os.environ["SystemRoot"], "Temp"))
    elif system == "Linux":
        temp_dirs.append("/tmp")
    elif system == "Darwin":  # macOS
        temp_dirs.append("/private/var/tmp")
        temp_dirs.append("/Library/Caches")

    return temp_dirs


def get_cache_directories():
    system = platform.system()
    cache_dirs = []

    if system == "Windows":
        cache_dirs.append(os.path.join(os.environ["LOCALAPPDATA"], "Temp"))
        cache_dirs.append(
            os.path.join(
                os.environ["LOCALAPPDATA"], "Microsoft", "Windows", "INetCache"
            )
        )
    elif system == "Linux":
        cache_dirs.append(os.path.expanduser("~/.cache"))
    elif system == "Darwin":  # macOS
        cache_dirs.append(os.path.expanduser("~/Library/Caches"))

    return cache_dirs


def cleanup_directories(directories, directory_type):
    for dir_path in directories:
        if os.path.exists(dir_path):
            try:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        try:
                            os.remove(file_path)
                            print(f"Removed {directory_type} file: {file_path}")
                        except Exception as e:
                            print(
                                f"Unable to remove {directory_type} file: {file_path}. Error: {str(e)}"
                            )

                shutil.rmtree(dir_path)
                print(f"{directory_type} cleaned: {dir_path}")
            except Exception as e:
                print(
                    f"Unable to clean {directory_type} directory: {dir_path}. Error: {str(e)}"
                )
        else:
            print(f"{directory_type} directory not found: {dir_path}")


if __name__ == "__main__":
    print("Cleaning temporary directories:")
    temp_dirs = get_temporary_directories()
    cleanup_directories(temp_dirs, "temporary")

    print("\nCleaning cache directories:")
    cache_dirs = get_cache_directories()
    cleanup_directories(cache_dirs, "cache")
