# Daily Inspirational Quote Automation Scripts

This automation script sends daily inspirational quotes via email. The script fetches a Bible verse and a random inspirational quote and sends them to a specified email address.

## Files

- `daily_inspirational_quote.py`: Python script to fetch a random Bible verse and an inspirational quote, then send them via email.

- `daily_inspirational_quote.bat`: Batch script (for Windows) to install the required Python packages and run the `daily_inspirational_quote.py` script.

- `daily_inspirational_quote.sh`: Shell script (for Linux/Unix) to install the required Python packages and run the `daily_inspirational_quote.py` script.

## Usage

### Python Script (`daily_inspirational_quote.py`)

1. Make sure you have Python 3.x installed on your system.

2. Install the required Python packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Python script to fetch and send the daily inspirational messages:
   ```bash
   python daily_inspirational_quote.py
   ```

### Batch Script (Windows) (`daily_inspirational_quote.bat`)

1. Double-click on the `daily_inspirational_quote.bat` file to execute it.

### Shell Script (Linux/Unix) (`daily_inspirational_quote.sh`)

1. Double-click or Run the shell script from the terminal:
   ```bash
   bash daily_inspirational_quote.sh
   ```

The scripts will fetch a random Bible verse and an inspirational quote, then send them to the recipient's email address specified in the `.env` file.

You can integrate this script with a cron job to run it everyday at specific time.
