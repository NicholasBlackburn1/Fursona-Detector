import requests
from bs4 import BeautifulSoup

def extract_links(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all <a> tags
    a_tags = soup.find_all('a')

    # Extract href attributes from the <a> tags
    links = [a['href'] for a in a_tags if a.has_attr('href')]

    return links

url = 'https://www.furtrack.com/index/species:fox'
print(extract_links(url))
