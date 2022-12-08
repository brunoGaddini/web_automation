# Import Libraries

#import selenium
#import webdriver_manager # allows to create a browser controlled by selenium

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service # Play ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Identifies the current browser version and install ChromeDriverManager
service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)
# For perfect operation it is necessary to download the web driver corresponding to the chosen browser

# Accessing the address to carry out the automation process
browser.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")

# Searching for an element within the page and write in the fields
browser.find_element('xpath',
                     '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys('Bruno')

browser.find_element('xpath',
                     '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('bruno_gaddini@hotmail.com')

browser.find_element('xpath',
                     '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys('')

# Setting browser read wait with some conditions
try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    browser.quit()
