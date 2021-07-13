from bs4 import BeautifulSoup as bs
import requests

def fetch_title(url):
    soup = bs(requests.get(url).text, 'lxml')
    title = soup.title.string
    return title

