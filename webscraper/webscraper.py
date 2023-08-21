from selenium import webdriver
from bs4 import BeautifulSoup

def extract_character_links_selenium(url):
    # Make sure to have the appropriate driver for the browser you want to use
    # This example uses Chrome
    driver = webdriver.Chrome()
    driver.get(url)

    # Let the content load (you might need to adjust the sleep duration)
    driver.implicitly_wait(10)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract <a> tags with the specific class
    a_tags = soup.find_all( class_='index-child character nothumb')




    # Extract href attributes from the <a> tags
    character_links = ["https://www.furtrack.com" + a['href'] for a in a_tags if a.has_attr('href')]
    print(character_links)
    driver.quit()

    return character_links

url = 'https://www.furtrack.com/index/species:fox'
print(extract_character_links_selenium(url))
