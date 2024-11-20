import smtplib
import random
import pandas
import datetime as dt

my_email = "pasindusandamalsenanayake@gmail.com"
password = "agey pgyj sdst slmv"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )

# I uploaded every codes related to birthday wisher into the pythonanywhere(https://www.pythonanywhere.com/user/sandamalpython/)
# 1 - Upload the all files into the pythonanywhere
# 2 - console - bash - run python3 main.py(birthday.py)
# 3 - dashboard - task - UTC - enter "python3 main.py" add time and click create. automatically run the project every day