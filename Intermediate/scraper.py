import requests
from bs4 import BeautifulSoup

url = "https://www.wiktionary.org"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
div_tags = soup.find_all('div', class_="footer")


for div_tag in div_tags:
    titles = div_tag.find('a', class_="other-project-link").get_text()
    print(titles)







"""for a_tag in a_tags:
    print(a_tag.get_text())


#assignment
titles = list(map(lambda a_tag: a_tag.get_text(), a_tags))
print(titles)"""
