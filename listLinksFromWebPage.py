#Author memento
# purpose : print the list of links in href that begins with /datasets and end with .zip
# I created this program to download zip files from a webpage thanks to wget 
# Usage : To download the zip file list, I'll do a simple : wget $(python listLinksFromWebPage.py)
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#We want links like : http://rpg.ifi.uzh.ch/datasets/uzh-fpv/indoor_forward_5_davis_with_gt.zip

site_base = "http://rpg.ifi.uzh.ch"
site_page = "/uzh-fpv.html"
html_page = urlopen(site_base+site_page)
soup = BeautifulSoup(html_page, features="html5lib")
# for regular expression ( re.compile(...) ), use this site : https://regex101.com/
for link in soup.findAll('a', attrs={'href': re.compile("^\/dataset.*.zip")}):
    print(site_base+link.get('href'))
