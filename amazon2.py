from bs4 import BeautifulSoup
soup = BeautifulSoup("amazon_out.txt", 'html.parser')

print(soup.prettify())