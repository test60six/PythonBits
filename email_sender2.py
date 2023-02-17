import smtplib
from email.message import EmailMessage
from string import template
from pathlib import Path

html= Template(Path("index.html").read_text())

email= EmailMessage()
email["from"] = "count ravioli"
email["to"] = "test60six@gmail.com"
email["subject"]= "you won a million dollars"


email.set_content(html.substitute({name:"TinTin",}),"html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email address here","password here")
    smtp.send_message(email)
    print("all good boss")
