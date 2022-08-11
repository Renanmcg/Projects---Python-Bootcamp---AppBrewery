from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.x-rates.com/table/?from=USD&amount=1')

exch_rate_euro = driver.find_element(By.XPATH, "//*[@id='content']/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[1]/td[2]/a")
exch_rate_brl = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr[5]/td[2]/a')
exch_rate_rublo = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr[41]/td[2]/a')
exch_rate_pound = driver.find_element(By.XPATH, "//*[@id='content']/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[2]/td[2]/a")

dollar_exch_rate = {'euro': exch_rate_euro.text,
                    'pounds': exch_rate_pound.text,
                    'brazilian_real': exch_rate_brl.text,
                    'russian_rublos': exch_rate_rublo.text
                    }
print(f' The dollar exchange rate: {dollar_exch_rate} ')

driver.get('https://www.x-rates.com/table/?from=BRL&amount=1')

exch_rate_euro = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[2]/td[2]/a')
exch_rate_dollar = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[1]/td[2]/a')
exch_rate_rublo = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr[40]/td[2]/a')
exch_rate_pound = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr[40]/td[2]/a')

brl_exch_rate = {'euro': exch_rate_euro.text,
                 'pounds': exch_rate_pound.text,
                 'dollar': exch_rate_dollar.text,
                 'russian_rublos': exch_rate_rublo.text
                }
print(f' The brazilian real exchange rate: {brl_exch_rate} ')
