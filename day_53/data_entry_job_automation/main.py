from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSer6YbpVgMtF5AGGIePOHL8Y6QsjL06L9rerce6zX2ArrWoaQ/' \
            'viewform?usp=sf_link'

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22'
           'mapBounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%22%3A37'
           '.609299211511704%2C%22north%22%3A37.94091184009742%7D%2C%22mapZoom%22%3A11%2C%22'
           'isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%2'
           '2beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22'
           'max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3A'
           'false%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22c'
           'msn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22'
           'isListVisible%22%3Atrue%7D')

time.sleep(6)
soup = BeautifulSoup(driver.page_source, 'html.parser')

all_link_elements = soup.findAll('a', attrs={'data-test': 'property-card-link'})

all_links = []
for link in all_link_elements:
    href = link["href"]
    #print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_address_elements = soup.findAll('address', attrs={'data-test': 'property-card-addr'})
all_addresses = [address.get_text() for address in all_address_elements]


all_price_elements = soup.findAll('span', attrs={'data-test': 'property-card-price'})
all_prices = [price.get_text() for price in all_price_elements]


for n in range(len(all_links)):
    driver.get(FORM_LINK)

    time.sleep(6)
    address = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
