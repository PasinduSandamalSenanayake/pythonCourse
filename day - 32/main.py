import smtplib # smtplib - simple mail transfer protocol library
import datetime as dt

my_email = "pasindusandamalsenanayake@gmail.com"
password = "agey pgyj sdst slmv"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # tls - transfer layer security
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="sandamalebay5@gmail.com",
#         msg="Subject:Subject of the email\n\n This is the body of the email"
#     )

# # instead of
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls() # tls - transfer layer security
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="sandamalebay5@gmail.com",
#     msg="Subject:Subject of the email\n\n This is the body of the email"
# )
# connection.close()


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week) # type of day_of_week is integer 0- monday ..............

date_of_birth = dt.datetime(year=1999, month=5, day=23)
print(date_of_birth)