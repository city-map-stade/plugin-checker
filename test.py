import requests
from bs4 import BeautifulSoup

word = str(input()).lower()
url = 'https://www.thesaurus.com/browse/{}'.format(word)

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select('li > span > a[data-linkid]')[:5]

for link in result:
    print(link.string)