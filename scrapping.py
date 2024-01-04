import requests
from bs4 import BeautifulSoup

github_profile="https://github.com/amankharwal/"
req=requests.get(github_profile)
scrapper=BeautifulSoup(req.content,"html.parser")
profile_picture= scrapper.find("img")  