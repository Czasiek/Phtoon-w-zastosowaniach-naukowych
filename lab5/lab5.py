from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# set options to disable notifications
options = Options()
options.add_argument('--disable-notifications')

# initialize the web driver
driver = webdriver.Chrome(options=options)

# navigate to website
driver.get('https://www.doctors-of-doom.com/')

# find elements with the specified CSS selectors
elements = driver.find_elements(By.CSS_SELECTOR, 'h2, h2 + div')

# display the text of each element
for element in elements:
    print(element.text)

# close the web driver
driver.close()
