from bs4 import BeautifulSoup
import requests
import smtplib
import os

URL = input("Enter link to the item you want to track: ")
my_data = {
    'User-Agent': os.environ.get("UserAgent"),
    'Accept_Language': 'en-US,en;q=0.9'
}
target_price = 900.00
response = requests.get(url=URL, headers=my_data)
response.raise_for_status()
content = response.text
soup = BeautifulSoup(content, 'html.parser')

price = float(soup.find(name='span', class_='a-offscreen').getText().split('EGP')[1])
product_title = soup.find(name='span', id='productTitle').getText().strip()

my_email = os.environ.get('Email')
password = os.environ.get('Password')
if price < target_price:
    with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=os.environ.get('myEmail'),
                            msg=f'Subject: Price Alert\n\n{product_title}\'s price is now {price} \n Link:{URL}'
                            )