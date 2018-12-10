import requests
from bs4 import BeautifulSoup
import ctypes,os,platform
import urllib.request
from urllib.parse import urljoin

def displaymenu():
	x = input("\nMain Menu\n(Enter the number before a choice to choose it)\n1 - Change Wallpaper\n2 - Change Category\nEnter your choice : ")
	return int(x)

def changewallpaper():
	pcos = (platform.system()).lower()
	if pcos=='windows':
	    ctypes.windll.user32.SystemParametersInfoW(20, 0, 'new.jpg' , 0)
	elif pcos=='linux':
		path = os.path.join(os.path.realpath('.'),'new.jpg')
		os.system("gsettings set org.gnome.desktop.background picture-uri file://"+path)
	else:
		print("Can't work for this platform!")



def main():
	f = open("settings.dat",mode = 'a+',encoding = 'utf-8')
	f.seek(0)
	if len(f.readline())==0:
		f.write("1\n")
	f.seek(0)
	x = displaymenu()
	if(x==2):
		y = input("1 - Bing Wallpaper\n2 - Quote Wallpaper from BrainyQuote\n")
		f = open("settings.dat",mode = 'w+',encoding = 'utf-8')
		f.write(y)
		f.close()
	else:
		f = open("settings.dat",mode = 'a+',encoding = 'utf-8')
		f.seek(0)
		y = f.readline()
		if len(y)==0:
			f.write("1\n")
			y = 1
		else:
			y = int(y)

	f.close()

	if y==1:
		link = 'https://bingwallpaper.com/'
		html = requests.get(link)
		soup = BeautifulSoup(html.content,'html.parser')
		img = soup.find('a',class_ = 'cursor_zoom')
		img = img.find('img')
		src = img['src']		
		urllib.request.urlretrieve(src,'new.jpg')

	else:
		link = 'https://www.brainyquote.com/quote_of_the_day'
		html = requests.get(link)
		soup = BeautifulSoup(html.content,'html.parser')
		img = soup.find('img',class_ = 'p-qotd')
		src = img['data-img-url']
		src = 'https://www.brainyquote.com'+src
		#print(src)
		opener=urllib.request.build_opener()
		opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
		urllib.request.install_opener(opener)
		urllib.request.urlretrieve(src,'new.jpg')

	changewallpaper()

if __name__ == '__main__':
 main()


    