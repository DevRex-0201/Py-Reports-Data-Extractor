import requests
from bs4 import BeautifulSoup

# List of URLs
urls = [
    "https://www.judiciary.uk/pfd-types/suicide-from-2015/", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/2", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/3", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/4", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/5", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/6", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/7", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/8", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/9", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/10", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/11", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/12", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/13", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/14", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/15", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/16", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/17", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/18", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/19", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/20", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/21", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/22", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/23", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/24", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/25", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/26", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/27", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/28", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/29", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/30", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/31", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/32", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/33", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/34", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/35", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/36", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/37", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/38", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/39", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/40", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/41", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/42", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/43", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/44", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/45", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/46", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/47", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/48", "https://www.judiciary.uk/pfd-types/suicide-from-2015/page/49"
]

# Function to extract href values from <a> elements with class "card__link"
def get_href_values(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # Find all <a> elements with class "card__link"
    links = soup.find_all('a', class_='card__link')
    
    # Extract href values
    href_values = [link.get('href') for link in links]
    
    return href_values

# Iterate through all URLs and extract href values
all_href_values = []
for url in urls:
    href_values = get_href_values(url)
    all_href_values.extend(href_values)

# Print the result
for index, href_value in enumerate(all_href_values, start=1):
    print(f"Link {index}: {href_value}")
