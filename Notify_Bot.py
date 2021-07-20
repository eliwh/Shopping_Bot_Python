import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests, datetime

#Beautiful Soup 4
from bs4 import BeautifulSoup
#Endpoint setting: TLOZ Skyward Sword Best Buy
url = "https://www.bestbuy.com/site/searchpage.jsp?st=the+legend+of+zelda+skyward+sword&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"
req = requests.get(url)
bsObj = BeautifulSoup(req.text, "html.parser")
data = bsObj.find_all("div", class_="btn btn-primary btn-sm btn-block btn-leading-ficon add-to-cart-button")

#Email Accouts
email_sender_account = "python.dev2397@gmail.com"
email_sender_username = "python.dev2397"
email_sender_password = "2O9p31cRI8hE"
email_smtp_server = "smtp.gmail.com"
email_smtp_port = 587

#Email Content
# chilipepperer@gmail.com
email_recipients = ["eliwh2k12@gmail.com", "chilipepperer@gmail.com"]
email_subject = "Back in stock!: The Legend of Zelda Skyward Sword"
email_body = f"The Legend of Zelda Skyward Sword is back in stock at best buy, click the link below to go to the site! By the way G this is a test from Elijah. Hope your having a goodnight homie. {url}"

#Login to email server
server = smtplib.SMTP(email_smtp_server, email_smtp_port)
print(f"Logging in to {email_sender_account}")
server.starttls()
server.login(email_sender_username, email_sender_password)


#for Loop, sending email to all email recipients
for recipient in email_recipients:
    print(f"Sendin email to {recipient}")
    message = MIMEMultipart('alternative')
    message['From'] = email_sender_account
    message['To'] = recipient
    message['Subject'] = email_subject
    message.attach(MIMEText(email_body, 'html'))
    text = message.as_string()
    server.sendmail(email_sender_account, recipient, text)

#All emails sent, log out / kill server
server.quit()


