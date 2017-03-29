# https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170329&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=0
# https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170329&bcoffset=1&ntoffset=1&p4ppushleft=1%2C48&s=44
# https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170329&bcoffset=1&ntoffset=1&p4ppushleft=1%2C48&s=88
# https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170329&bcoffset=-5&ntoffset=-5&p4ppushleft=1%2C48&s=132
import requests
import re

def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def parsePage(ilt, html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			tag = eval(tlt[i].split(':')[1])
			ilt.append([price,tag])
	except:
			print("")



def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("xuhao","jiage","mingcheng"))
	count = 0
	for g in ilt:
		count +=1
		print(tplt.format(count,g[0],g[1]))



def main():
	goods = input('The good you want to search:')
	depth = 2
	infoList = []
	start_url = 'https://s.taobao.com/search?q='+goods
	for i in range(depth):
		try:
			url = start_url+'&s=' +str(44*i)
			html = getHTMLText(url)
			parsePage(infoList, html)
		except:
			continue
	printGoodsList(infoList)

main()