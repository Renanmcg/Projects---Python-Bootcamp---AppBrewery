import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

BUY_PRICE = 34000
PRODUCT_URL = url

header = {  # you can find these informations on http://myhttpheader.com/. If these two aren't enough you can add more.
'Accept-Language': XXX,
'User-Agent': XXX
}

response = requests.get(PRODUCT_URL, headers= header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

product_title = soup.find(id = "productTitle", class_="a-size-large product-title-word-break").get_text()  # You must inspect the html of the page to find the information you need tofind the informations.
product_price = soup.find(class_="a-offscreen").get_text().split(',')[0].replace('.', '')
# The split is to split taking out the brazilian notation with comma.
# The replace is in order to take the dot off.
price_without_currency = product_price.split("R$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
'''Or
product_price = soup.find(class_="a-offscreen").get_text().split(',')[0].replace('.', '')
price_without_currency = product_price.split("R$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
print(float(product_price[2::]))'''

if price_as_float > BUY_PRICE:
    message = f"{product_title} is now {product_price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRODUCT_URL}"
        )



