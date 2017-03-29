from bs4 import BeautifulSoup
import requests
import bs4


def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""


def fillUnivList(ulsit,html):
	soup = BeautifulSoup(html,"lxml")
	# for tr in soup.find('tbody').children:
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds = tr('td')
			ulsit.append([tds[0].string,tds[1].string,tds[2].string])


# def fillUnivList(ulist, html):
#     soup = BeautifulSoup(html, "html.parser")#2016
#     for tr in soup.find('tbody').children:
#         if isinstance(tr, bs4.element.Tag):
#             tds = tr('td')
#             ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulsit,num):
	tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
	print(tplt.format("Rank","Name","Score",chr(12288)))
	for i in range(num):
		u = ulsit[i]
		print(tplt.format(u[0],u[1],u[2],chr(12288)))
	# print("Suc"+str(num))

# def printUnivList(ulist, num):
#     print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
#     for i in range(num):
#         u=ulist[i]
#         print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))

def main():
	uinfo = []
	url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html'
	html = getHTMLText(url)
	fillUnivList(uinfo,html)
	printUnivList(uinfo,20)

main()
