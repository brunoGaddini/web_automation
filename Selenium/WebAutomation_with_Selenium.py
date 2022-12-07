# Import Libraries

import selenium
import webdriver_manager # allows to create a browser controlled by selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service # Play ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome()
# For perfect operation it is necessary to download the web driver corresponding to the chosen browser
