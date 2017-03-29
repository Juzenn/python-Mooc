# python-Mooc

------

## Task-01 最好大学排名
> * 改进了原来python制表中文排版混乱问题
> * 简单的利用requests,bs4,beautiful库来实现排名跟踪
> * 指定网站2017&2016解析方式不同，前者lxml,后者html.parser

## Task-02 淘宝比价
> * 通过输入关键字观察页面链接规律
> * 对多页爬虫进行了扩展
> * 任意输入关键字，即可进行比价

### 代码块
``` python
@vapor_authorization
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
>>> The good you want to search:


```
