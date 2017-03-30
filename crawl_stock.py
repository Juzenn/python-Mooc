import requests
from bs4 import BeautifulSoup
import re
import traceback

def getHTMLText(url, code = 'utf-8'):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = code
		return r.text
	except:
		return ""


def getStockList(lst, stockURL):
	html = getHTMLText(stockURL, 'GB2312')
	soup = BeautifulSoup(html, 'html.parser')
	a = soup.find_all('a')
	for i in a:
		try:
			href = i.attrs['href']
			lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
		except:
			continue


 
def getStockInfo(lst,stockURL,fpath):
	count = 0		
	for stock in lst:
		url = stockURL + stock + ".html"
		html = getHTMLText(url)
		try:
			if html == "":
				continue
			infoDict = {}
			soup = BeautifulSoup(html, 'html.parser')
			stockInfo = soup.find('div', attrs ={'class':'stock-bets'})

			name = stockInfo.find_all(attrs = {'class':'bets-name'})[0]
			infoDict.update({'stock_name':name.text.split()[0]})#name.text.split([0]) error!

			keyList = stockInfo.find_all('dt')
			valueList = stockInfo.find_all('dd')
			for i in range(len(keyList)):
				key = keyList[i].text
				val = valueList[i].text
				infoDict[key] = val

			with open(fpath, 'a', encoding = 'utf-8') as f:
				f.write(str(infoDict)+'\n')
				count += 1
				print("\rcurrent speed:{:.2f}%".format(count/len(lst)),end='')

		except:
			traceback.print_exc()
			print("\rcurrent sped:{:.2f}%".format(count/len(lst)),end='')
			continue




def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
	stock_info_url = 'https://gupiao.baidu.com/stock/'
	output_file = 'BaiduInfo.txt'
	slist = []
	getStockList(slist, stock_list_url)
	getStockInfo(slist, stock_info_url,output_file)

main()

