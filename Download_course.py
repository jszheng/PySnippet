import urllib.request
from bs4 import BeautifulSoup
import re

#url = 'https://safari.ethz.ch/digitaltechnik/spring2019/doku.php?id=schedule'
url = 'http://ece.tamu.edu/~spalermo/ecen720.html'
#root = 'https://safari.ethz.ch'
root = 'http://ece.tamu.edu/~spalermo/'

r_pdf = re.compile(r'\.pdf$')
r_ppt = re.compile(r'\.ppt$')
r_pptx = re.compile(r'\.pptx$')
r_video = re.compile(r'youtube')

pdfs = []
ppts = []
videos = []

with urllib.request.urlopen(url) as f:
    data = f.read().decode('utf-8')
    soup = BeautifulSoup(data, 'lxml')
    #print(soup.prettify())
    for a in soup.find_all('a'):
        link = a['href']
        print(link)
        if r_pdf.search(link):
            pdfs.append(link)
        if r_ppt.search(link):
            ppts.append(link)
        if r_pptx.search(link):
            ppts.append(link)
        if r_video.search(link):
            videos.append(link)



print("PDF files")
[print(root + p) for p in pdfs]

print("PPT files")
[print(root + p) for p in ppts]

print("\nVideos")
[print(v) for v in videos]