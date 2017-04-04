# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import os


def getHTMLText(url):
	try:
		kv = {'user-agent':'Mozilla/5.0'}
		r = requests.get(url, headers = kv)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""


def getPages(article_url, fpath):
	html = getHTMLText(article_url)
	soup = BeautifulSoup(html, 'html.parser')
	page_title = soup.find("title").string
	print(page_title+ '\n')
	page_reply = soup.find("li", "l_reply_num").get_text()
	print(page_reply + '\n')
	page_num = page_reply.split("，")[1]
	page_num = int(re.findall(r'\d', page_num)[0])
	with open(fpath, 'a', encoding = 'utf-8') as f:
		f.write(page_title)
		f.write(page_reply)
	return page_num


def parsePage(ilt, article_url):
	html = getHTMLText(article_url)
	soup = BeautifulSoup(html, 'html.parser')
	# test = soup.find_all('div', attrs = {'class':'l_post j_l_post l_post_bright noborder '})
	# print(test[0])
	floors = soup.find_all(id =re.compile("post_content_"))


	for n in floors:
		# m = soup.find(class_=re.compile("d_post_content"))
		if len(n.get_text()) != 0:
			text_floor = n.get_text().strip()
			num_floor = '-------第'+' '+'楼---------'
			floor = (text_floor, num_floor)
			ilt.append(list(floor))
			



def printArticleList(ilt, fpath):
	# html = getHTMLText(article_url)
	# soup = BeautifulSoup(html, 'html.parser')
	# print((soup.h1)[0].get_text())
	count = 0
	for g in ilt:
		# print(g[0])
		# print(g[1])
		count+=1
		g[1] = '--------------------第'+ str(count) +'楼---------------------'
		with open(fpath, 'a', encoding = 'utf-8') as f:
			f.write(g[0]+'\n')
			f.write(g[1]+'\n')




def main():
	start_url = input("Input the link you want to read:")
	print('----------只看楼主请输入1，看全部帖子回复2-----------')
	key = input('请输入您的选择：')
	if key == '1':
		start_url = start_url.split('?')[0]+'?see_lz=1'
	elif key == '2':
		start_url = start_url
	else:
		print('请检查您输入的选项是否正确!')
	output_file = 'tiezi.txt'
	page = getPages(start_url, output_file)
	infoList=[]
	for i in range(1, page+1):
		try:
			print('正在抓取第' + str(i) +'页')
			url = start_url +'&pn='+str(i)
			parsePage(infoList, url)
		except:
			continue
	printArticleList(infoList, output_file)

main()

		



# http://tieba.baidu.com/p/5014042526?red_tag=u2909961476
# http://tieba.baidu.com/p/5014042526?see_lz=1