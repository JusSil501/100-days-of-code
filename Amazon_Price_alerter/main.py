import smtplib
from bs4 import BeautifulSoup
import requests
TARGET_PRICE = 45




def check_price(price):
    if float(price.getText()) < TARGET_PRICE:
        send_email()
info = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0',
    "Accept-Language": 'en-US'
}

response = requests.get("https://www.amazon.com/Veniceball-Basketball-Outdoor-Leather-Official/dp/B097F8KHQX/ref=sr_1_1_sspa?keywords=basketball&qid=1654834630&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNkJVV0lKRVk0VzkwJmVuY3J5cHRlZElkPUEwOTcxMDYzM1BWM0g4U082QkFUMSZlbmNyeXB0ZWRBZElkPUEwMDYyMzkwQUQwMEsyNkhVT1FZJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
                        headers=info)

htmL = response.text

soup = BeautifulSoup(htmL, "lxml")

title = (soup.find("h1", class_= "a-size-large a-spacing-none")).getText()
price = soup.find("span", class_="a-price-whole")
link_to_buy = "https://www.amazon.com/Veniceball-Basketball-Outdoor-Leather-Official/dp/B097F8KHQX/ref=sr_1_1_sspa?keywords=basketball&qid=1654834630&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNkJVV0lKRVk0VzkwJmVuY3J5cHRlZElkPUEwOTcxMDYzM1BWM0g4U082QkFUMSZlbmNyeXB0ZWRBZElkPUEwMDYyMzkwQUQwMEsyNkhVT1FZJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
def send_email():
    email = input('Type your email and press enter:')
    password = input("Type your password and press enter:")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(email, password)

    send_email = email
    reciver_email = email
    message = f'{title}\n now {price}$\n{link_to_buy}'
    connection.sendmail(send_email, reciver_email, message)









check_price(price)



