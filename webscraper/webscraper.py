from selenium import webdriver
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define your URL
url = 'https://www.furtrack.com/index/species:dragon'


def downloadSingleImage(driver,url):
    print("tryinng to downklaod")

    driver.get(url)

    # Wait for up to 10 seconds until the desired elements are present on the page.
    img_tags = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img.index-image-actual'))
    )

    # If found, extract and print the links.
    print(img_tags)




# Set up the Selenium WebDriver
driver = webdriver.Chrome()
driver.get(url)

try:
    # Wait for up to 10 seconds until the desired elements are present on the page.
    a_tags = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.index-child.character.nothumb'))
    )

    # If found, extract and print the links.
    for a in a_tags:
        link = a.get_attribute('href')
        print(link)
        downloadSingleImage(driver,link)




finally:
    driver.quit()  # Ensure the browser closes even if there's an error.

