import smtplib
from dotenv import load_dotenv
import os
import random
import datetime as dt
import pandas as pd

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv('APP_PASSWORD')
birthday_data = pd.read_csv("birthdays.csv")
now = dt.datetime.now()

def get_message(name):
    letter_number = random.randint(1, 3)
    with open(f'letter_templates/letter_{letter_number}.txt') as letter_file:
        lines = letter_file.readlines()
        lines[0] = lines[0].replace('[NAME]', name)

    return "".join(lines)


for index,row in birthday_data.iterrows():
    month = row['month']
    day = row['day']

    today = now.day
    this_month = now.month

    if this_month == month and today == day:
        name = row['name']
        email = row['email']

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(my_email, my_password)
        my_message = get_message(name)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Happy Birthday!\n\n{my_message}".encode("utf-8"))
        connection.close()