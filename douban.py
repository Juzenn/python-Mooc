import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
	try:
		r = requests.get(url,  timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""



def parsePage(ilt, movie_url):
	html = getHTMLText(movie_url)
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', attrs = {'class':'item'})

	for n in items:
		name = n.find(attrs = {'class':'hd'})
		movie_name = name.get_text().split('[')[0]
		names = movie_name.replace('\n', ' ')

		notes = n.find(attrs = {'class':'bd'})
		director = notes.get_text().split()[1]
		#print(director)


		years = re.findall(r'\d{4}[\xa0]',notes.get_text())
		year = "".join(years)
		year = year[:4]
		#print(year)

		star = re.findall(r'\d\.\d',notes.get_text())
		#print(star)

		note = (star, names, director, year )
		#msg = map(list, notes)
		
		ilt.append(list(note))


def printMovieList(ilt):
	count = 0
	print('豆瓣电影TOP250\n')
	# ilt = sorted(ilt, key=lambda ele:ele.rate, reverse = 1)
	ilt = sorted(ilt,reverse=True)
	for g in ilt:
		count+=1
		print(count, end='')
		print(g[1])
		print("     中文名称:%s"%g[1].split('/')[0])
		print("     外文名称:%s"%g[1].split('/')[1])
		print("     评分:%s"%("".join(g[0])))
		print("     导演:%s"%g[2])
		print("     上映年份:%s"%g[3])
  



def main():
	start_url = 'https://movie.douban.com/top250'
	depth = 10
	infoList = []
	for i in range(depth):
		try:
			url = start_url + '?start=' +str(25*i)
			parsePage(infoList, url)
		except:
			continue
	printMovieList(infoList)

main()
