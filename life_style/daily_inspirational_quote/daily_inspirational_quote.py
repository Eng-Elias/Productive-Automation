import os
import requests
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

# Path to store the last sent date
LAST_SENT_DATE_FILE = "last_sent_date.txt"


def fetch_bible_verse():
    response = requests.get("https://bible-api.com/?translation=kjv&random=verse")
    if response.status_code == 200:
        data = response.json()
        verses = data["verses"]
        verse = verses[0]["text"]
        book = verses[0]["book_name"]
        chapter = verses[0]["chapter"]
        verse_number = verses[0]["verse"]
        print(f"{verse} - {book} {chapter}:{verse_number}")
        return f"{verse} - {book} {chapter}:{verse_number}"
    else:
        return "Failed to fetch a Bible verse."


def fetch_inspirational_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()[0]
        quote = data["q"]
        author = data["a"]
        return f"{quote} - {author}"
    else:
        return "Failed to fetch a quote."


def send_daily_messages(bible_verse, inspirational_quote):
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    email = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    recipient_email = os.getenv("RECIPIENT_EMAIL")

    subject = "Daily Inspirational Message"

    body = f"Here's your daily inspirational message:\n\nBible Verse:\n{bible_verse}\n\nInspirational Quote:\n{inspirational_quote}"

    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email, password)
        server.sendmail(email, recipient_email, msg.as_string())


def get_last_sent_date():
    if os.path.exists(LAST_SENT_DATE_FILE):
        with open(LAST_SENT_DATE_FILE, "r") as file:
            last_sent_date_str = file.read()
            return datetime.datetime.strptime(last_sent_date_str, "%Y-%m-%d").date()
    else:
        return None


def update_last_sent_date():
    today = datetime.date.today()
    with open(LAST_SENT_DATE_FILE, "w") as file:
        file.write(today.strftime("%Y-%m-%d"))


if __name__ == "__main__":
    # Get the last sent date
    last_sent_date = get_last_sent_date()
    today = datetime.date.today()

    # If the last sent date is None or not today, fetch a new Bible verse and quote and send them
    if last_sent_date is None or last_sent_date < today:
        # Fetch a random Bible verse
        bible_verse = fetch_bible_verse()

        # Fetch a random inspirational quote
        inspirational_quote = fetch_inspirational_quote()

        # Send the daily messages via email
        send_daily_messages(bible_verse, inspirational_quote)

        # Update the last sent date to today
        update_last_sent_date()

        print("Daily inspirational messages sent successfully.")
    else:
        print(
            "Messages already sent for today. Run the script again tomorrow for new messages."
        )
