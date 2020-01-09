import requests
from bs4 import BeautifulSoup
import json
import urllib.request
import os
import ctypes
import platform
import sys

def bing_daily_wallpaper(location,index):

	response = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
	image_data = json.loads(response.text)

	image_url = image_data["images"][0]["url"]
	image_url = image_url.split("&")[0]
	src = "https://www.bing.com" + image_url

	urllib.request.urlretrieve(src,os.path.join(location,'wallpaper%s.jpg'%index))


def brainy_quotes(location,index):

	link = 'https://www.brainyquote.com/quote_of_the_day'
	html = requests.get(link)
	soup = BeautifulSoup(html.content,'html.parser')
	img = soup.find('img',class_ = 'p-qotd')
	src = img['data-img-url']
	src = 'https://www.brainyquote.com'+src
	opener=urllib.request.build_opener()
	opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
	urllib.request.install_opener(opener)
	urllib.request.urlretrieve(src,os.path.join(location,'wallpaper%s.jpg'%index))

def change_wallpaper(location,index):
	pcos = (platform.system()).lower()
	if pcos=='windows':
	    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(location,'wallpaper%s.jpg'%index) , 0)
	elif pcos=='linux':
		path = os.path.join(os.path.realpath('.'),os.path.join(location,'wallpaper%s.jpg'%index))
		os.system("gsettings set org.gnome.desktop.background picture-uri file://"+path)
	else:
		print("Can't work for this platform!")


