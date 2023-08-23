import time
import logger
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import consts
import re


# smooth scrooling for the app to get all the images withlut me schooling
def smooth_scroll(driver, scroll_pause_time=0.7, max_scrolls=100):
    y_position = 0
    scrolls_performed = 0

    while scrolls_performed < max_scrolls:
        driver.execute_script(f"window.scrollBy(0, 400);")  # scrolling by 400 pixels
        scrolls_performed += 1
        time.sleep(scroll_pause_time)  # allow for the page to load

# extracts fiel names fro the url
def extract_filename_from_url(url):
    match = re.search(r'/([^/]+?)(\?|$)', url)
    return match.group(1) if match else None

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
    logger.info("Starting up web scraper to scrape fursuits....")
    driver.get(url)

    logger.warning("set scrool time too 7 seconds...")
    SCROLL_PAUSE_TIME = 0.7  # time to wait for content to load, you can adjust this
    smooth_scroll(driver,SCROLL_PAUSE_TIME,100)
    logger.PipeLine_Ok("set school time to 7 seconds")



    while True:

        logger.Warning("starting to schrool...")
        # Scroll down to the bottom incrementally
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for content to load
        time.sleep(SCROLL_PAUSE_TIME)

        logger.PipeLine_Ok("done scrooling time to download images")
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # if heights are the same after waiting, we've probably reached the bottom
            break
        last_height = new_height

        logger.warning("found images....")
        # Wait for up to 10 seconds until the desired elements are present on the page.
        img_tags = WebDriverWait(driver, 300).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img.index-image-actual'))
        )


        # If found, extract and print the links.
        for a in img_tags:
            link = a.get_attribute('src')
            print(link)
            consts.lastlink = extract_filename_from_url(link)





# Set up the Selenium WebDriver
driver = webdriver.Chrome()
driver.get(url)

downloadmultiple(driver,"https://www.furtrack.com/index/solo_focus+dragon")

driver.quit()  # Ensure the browser closes even if there's an error.

