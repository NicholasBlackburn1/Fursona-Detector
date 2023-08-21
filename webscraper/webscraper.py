import requests
from bs4 import BeautifulSoup

def scrape_fursona_type(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Here you'd target the specific HTML elements or classes that contain the fursona types
    fursona_type = soup.find('YOUR_TARGET_ELEMENT_OR_CLASS_HERE').text

    return fursona_type

url = 'YOUR_FURTRACK_URL_HERE'
print(scrape_fursona_type("https://www.furtrack.com/index/species:fox"))
