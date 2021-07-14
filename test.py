from fetch_title import fetch_title
import sys

url = sys.argv[1]
anw = fetch_title.fetch_title(url)

print(anw)