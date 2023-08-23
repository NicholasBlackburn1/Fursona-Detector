from selenium import webdriver
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define your URL
url = 'https://www.furtrack.com/index/species:dragon'


def downloadSingleImage(driver,url):
    i =0
    print("tryinng to downklaod")

    driver.get(url)

    # Wait for up to 10 seconds until the desired elements are present on the page.
    img_tags = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img.index-image-actual'))
    )

    # If found, extract and print the links.

    # If found, extract and print the links.
    for a in img_tags:
        link = a.get_attribute('src')
        print(link)
        i = 1
        if(i == 1):
            return
        return





# Set up the Selenium WebDriver
driver = webdriver.Chrome()
driver.get(url)

try:
    # Wait for up to 10 seconds until the desired elements are present on the page.
    a_tags = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.index-child.character.nothumb'))
    )
    links = [a.get_attribute('href') for a in a_tags]

    # If found, extract and print the links.
    for link in links:
            print(link)
            downloadSingleImage(driver, link)




finally:
    driver.quit()  # Ensure the browser closes even if there's an error.

