import smtplib
import datetime as dt
import random

my_email = "pasindusandamalsenanayake@gmail.com"
password = "agey pgyj sdst slmv"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="sandamalebay5@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )