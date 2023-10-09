# File Cleanup in Downloads Folder

This set of scripts automates the cleanup of files in the Downloads folder based on the last access time. It provides scripts for Windows (.bat) and Unix-like systems (Linux, MacOS) (.sh) to make running the Python script easy and intuitive.

## Scripts

- **file_cleanup_in_downloads_folder.py**: Python script that performs the file cleanup in the Downloads folder.

- **cleanup_downloads.bat**: Batch script for Windows to run the Python script and pause for user input before closing.

- **cleanup_downloads.sh**: Shell script for Unix-like systems (Linux, MacOS) to run the Python script and wait for user input before closing.

## Usage

### Windows (.bat)

1. Double-click `cleanup_downloads.bat`.
2. The script will run, perform the file cleanup, and display a message.
3. Press `any key` to close the window.

### Linux and MacOS (.sh)

1. Open a terminal.
2. Navigate to the directory containing `cleanup_downloads.sh`.
3. Don't forget to make the script executable:

```
chmod +x cleanup_downloads.sh
```

4. Run the command: `./cleanup_downloads.sh`
5. The script will run, perform the file cleanup, and display a message.
6. Press `any key` to close the terminal.

### Python Script (file_cleanup_in_downloads_folder.py)

1. Run the Python script directly using the Python interpreter:
   ```
   python file_cleanup_in_downloads_folder.py
   ```

## Configuration

Adjust the `days_threshold` variable in `file_cleanup_in_downloads_folder.py` to set the number of days for the cleanup threshold (default is 30 days).

```python
# Specify the number of days for the threshold
days_threshold = 30
```
