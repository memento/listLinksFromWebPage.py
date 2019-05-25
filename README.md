# listLinksFromWebPage.py
This python 3 script will help printing zip file links and allow me to simply apply wget to download them

# Install missing librairies

I use pip as a package manager.
```
sudo pip install beautifulsoup4
```

# Modify variables : 

I want to list zip files in href tags from that page : http://rpg.ifi.uzh.ch/uzh-fpv.html
I choose to split that link to two variables.

```python3
site_base = "http://rpg.ifi.uzh.ch"
site_page = "/uzh-fpv.html"
```
Then, I'll use again site_base to concatenate the base url to the zip file relative links my script found to obtain the list of absolute paths.

# Usage : 
In command line : 
```
wget $(python listLinksFromWebPage.py)
```

Enjoy.
Memento.
