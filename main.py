import requests
from bs4 import BeautifulSoup
import smtplib


response = requests.get("https://www.amazon.com/Apple-MacBook-13-3in-MLH12LL-Touch-Bar/dp/B08M16712F/ref=sr_1_3?crid=1TT237UH6FVB4&keywords=macbook+pro&qid=1665260772&qu=eyJxc2MiOiI2LjM5IiwicXNhIjoiNi40OCIsInFzcCI6IjUuOTQifQ%3D%3D&sprefix=mac%2Caps%2C393&sr=8-3",
             headers={"Accept-Language": "en-US,en;q=0.9", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                                                          "(KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44", })
amazon = response.text
soup = BeautifulSoup(amazon, 'html.parser')
price = soup.find_all(name="span", class_="a-offscreen")[0].get_text()
price_value = float(price[1:])

MY_EMAIL = "myemail@gmail.com"
EMAIL_PASS = "xxxxxxxxxxxxxxx"
TARGET_PRICE = 600.00

if price_value <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=MY_EMAIL, password=EMAIL_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="ferdgm@yahoo.com",
                            msg="subject: Amazon Price Alert \n\nThe price of your favourite product just hit "
                                f"${price_value}.Would you like to buy it now?\nHere is the link to purchase it"
                                f"https://www.amazon.com/Apple-MacBook-13-3in-MLH12LL-Touch-Bar/dp/B08M16712F/ref=sr_1_3?crid=1TT237UH6FVB4&keywords=macbook+pro&qid=1665260772&qu=eyJxc2MiOiI2LjM5IiwicXNhIjoiNi40OCIsInFzcCI6IjUuOTQifQ%3D%3D&sprefix=mac%2Caps%2C393&sr=8-3")




