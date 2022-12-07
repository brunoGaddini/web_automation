# Import Libraries

#import selenium
#import webdriver_manager # allows to create a browser controlled by selenium

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service # Play ChromeDriverManager

# Identifies the current browser version and install ChromeDriverManager
service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)
# For perfect operation it is necessary to download the web driver corresponding to the chosen browser

browser.get("https://pages.hashtagtreinamentos.com/arquivo-python-1jGh7kZSxQLoznA_GgwnWa8f7LEl3kKCZ?origemurl=hashtag_yt_org_planilhapyt_8AMNaVt0z_M")
