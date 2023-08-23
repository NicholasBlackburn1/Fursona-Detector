import time
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define your URL fopr unsotrd
url = 'https://www.furtrack.com/index/species:dragon'

#unsotrtred randomly grabbing imagwes from furtyrsck in a catagory
def unsortedimagesurl(url):

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


# gets single omages from users in a catagory
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

# this schrools the page and grabs all the images on that page

def downloadmultiple(driver, url):

    print("tryinng to downklaod a bunch of images...")

    driver.get(url)

    SCROLL_PAUSE_TIME = 2  # time to wait for content to load, you can adjust this
    last_height = driver.execute_script("return document.body.scrollHeight")  # get the initial height of the document



    while True:

        # Scroll down to the bottom incrementally
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for content to load
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # if heights are the same after waiting, we've probably reached the bottom
            break
        last_height = new_height

        # Wait for up to 10 seconds until the desired elements are present on the page.
        img_tags = WebDriverWait(driver, 300).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img.index-image-actual'))
        )

        # If found, extract and print the links.

        # If found, extract and print the links.
        for a in img_tags:
            link = a.get_attribute('src')
            print(link)


# Set up the Selenium WebDriver
driver = webdriver.Chrome()
driver.get(url)

downloadmultiple(driver,"https://www.furtrack.com/index/solo_focus+dragon")

driver.quit()  # Ensure the browser closes even if there's an error.

