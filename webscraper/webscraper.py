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

    y_position = 0
    scrolls_performed = 0

    while scrolls_performed < 100:

        driver.execute_script(f"window.scrollBy(0, 400);")  # scrolling by 400 pixels
        scrolls_performed += 1
        time.sleep(7)  # allow for the page to load

        logger.PipeLine_Ok("done scrooling time to download images")
        # Calculate new scroll height and compare with last scroll height



        # Wait for up to 10 seconds until the desired elements are present on the page.
        img_tags = WebDriverWait(driver, 300).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img.index-image-actual'))
        )

        logger.warning("found images....")
        # If found, extract and print the links.


        # Refresh the window to show the updated line

        for a in img_tags:
            link = a.get_attribute('src')
            consts.lastlink = extract_filename_from_url(link)

            logger.PipeLine_Ok("last image name is" +consts.lastlink)
            logger.info("img link is "+link)






# Set up the Selenium WebDriver
driver = webdriver.Chrome()

logger.PipeLine_init("stasrting up webscraper for FURTRACK...")
url = "https://www.furtrack.com/index/solo_focus+dragon"

logger.warning("scraping url = "+ url)
downloadmultiple(driver,url)

driver.quit()  # Ensure the browser closes even if there's an error.

