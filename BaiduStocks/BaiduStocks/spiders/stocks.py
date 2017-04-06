# -*- coding: utf-8 -*-
import scrapy
import re



class StocksSpider(scrapy.Spider):
    name = "stocks"
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
    	for herf in response.css('a:attrs(href)').extract():
    		try:
    			stock = re.findall(r'[s][hz]\d{6}',href)[0]
    			url = 'https://gupiao.baidu.com/stock/'+stock +'.html'
    			yield scrapy.Requests(url, callback = self.parse_stock)
    		except:
    			continue


    def parse_stock(self, response):
    	infoDict = {}
    	stockInfo = response.css('.stock-bets')
    	name = stockInfo.css('.bets-name').extract()[0]
    	keyList = stockInfo.css('dt').extract()
    	valueList = stockInfo.css('dd').extract()
    	for i in range(len(keyList)):
    		key = re.findall(r'>.*<dt>', keyList[i])[0][1:-5]
    		try:
    			val = re.findall(r'\d+\.?.*</db>', valueList[i])[0][0:-5]
    		except:
    			val = '--'
    		infoDict[key] = val

    	infoDict.updata({
    		'stock_name':re.findall('\s.*\(',name)[0].split()[0] + re.findall('\>.*\<',name)[0][1:-1]
    		})

    	yield infoDict


#callback 是一个callable或string(该spider中同名的函数将会被调用)。 从link_extractor中每获取到链接时将会调用该函数。
#该回调函数接受一个response作为其第一个参数， 并返回一个包含 Item 以及(或) Request 对象(或者这两者的子类)的列表(list)。