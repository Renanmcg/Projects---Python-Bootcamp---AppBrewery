from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

n_articles = driver.find_element(By.XPATH, "//*[@id='articlecount']/a[1]")
# or n_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(n_articles.text)

n_articles.click() #click on this element that happen is an hyperlink
driver.back()

Galego = driver.find_element(By.LINK_TEXT, "Galego")
Galego.click()
driver.back()

search =driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.get('http://secure-retreat-92358.herokuapp.com/')
f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Renan")
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Gomes")
email = driver.find_element(By.NAME, "email")
email.send_keys("aaA@aaa.com")
submit = driver.find_element(By.XPATH, "/html/body/form/button")
submit.click()
#driver.quit()
