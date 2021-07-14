from bs4 import BeautifulSoup as bs
import requests

status = ''
message = ''
def fetch_title(url):
    try:
        soup = bs(requests.get(url).text, 'lxml')
        status = 'OK'
        message = 'fetching title success.'
        res = soup.title.string
    except requests.exceptions.MissingSchema as err:
        status = 'ERR'
        message = str(err)
        res = None
    return (status, message, res)
