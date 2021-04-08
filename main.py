import requests
from bs4 import BeautifulSoup
import smtplib

email = "******@gmail.com"
password = "*********"
recipient_email = "**********@outlook.com"

header = {
    "User-Agent": "Defined",
    "Accept-Language": "en-US,en;q=0.9,fr-CA;q=0.8,fr;q=0.7"

}

link = "https://www.amazon.ca/Instant-Pot-Plus-Programmable-Pressure/dp/B075CYMYK6/ref=sr_1_1?dchild=1&keywords" \
       "=Instant+Pot+Ultra+60+Ultra+6+Qt+10-in-1+Multi-+Use+Programmable+Pressure+Cooker%2C+Slow+Cooker%2C+Rice" \
       "+Cooker%2C+Yogurt+Maker%2C+Cake+Maker%2C+Egg+Cooker%2C+Saut%C3%A9%2C+and+more%2C+Stainless+Steel%2FBlack&qid" \
       "=1617830671&sr=8-1 "
response = requests.get(link, headers=header)

data = response.text

soup = BeautifulSoup(data, "html.parser")

price_tag = soup.find(id="priceblock_ourprice")
title_tag = soup.find(id="title")
title = title_tag.getText().strip()
price = float(price_tag.getText().split("$")[1].strip())


message = f"{title} is now {price}"
message = message.encode('utf-8')  # encodes the message in utf-8


if price < 200:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # secure connection with TLS
        connection.login(user=email, password=password)  # login into the email address of the sender
        connection.sendmail(from_addr=email, to_addrs=recipient_email,
                            msg=f"Subject: Amazon Price Alert ! \n {message} \n {link}")

