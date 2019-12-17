import urllib.request
from bs4 import BeautifulSoup
import re

url = 'http://sampl.cs.washington.edu/tvmconf'

r_pdf = re.compile(r'\.pdf$')
r_video = re.compile(r'youtu\.be')

pdfs = []
videos = []
with urllib.request.urlopen(url) as f:
    data = f.read().decode('utf-8')
    soup = BeautifulSoup(data, 'lxml')
    #print(soup.prettify())
    for a in soup.find_all('a'):
        link = a['href']
        if r_pdf.search(link):
            pdfs.append(link)
        if r_video.search(link):
            videos.append(link)

print("PDF files")
root = 'http://sampl.cs.washington.edu'
[print(root + p) for p in pdfs]

print("\nVideos")
[print(v) for v in videos]