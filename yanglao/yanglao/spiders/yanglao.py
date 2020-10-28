from scrapy.spiders import Spider
from scrapy import Request
from yanglao.items import YanglaoItem
import time

class Yanglao(Spider):
	name = "yanglao"
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
	def start_requests(self):
		url = "http://www.yanglao.com.cn/heilongjiang"
		yield Request(url , callback = self.parse1)

	def parse1(self, response):
		items=[]
		a = response.xpath("//div[contains(@class,'list-view')]/ul/li/a/@href").extract()
		base_url = "http://www.yanglao.com.cn"
		for i in a:
			parse1_url = base_url + i
			item = YanglaoItem()
			item['src'] = parse1_url
			items.append(item)
			time.sleep(1)
			#yield item
			yield Request(item['src'], callback=self.parse,meta={"item":item})

	def parse(self, response):
		item = response.meta["item"]
		item['name'] = response.xpath("//div[contains(@class,'inst-summary')]/h1/text()").extract()
		item['address'] = response.xpath("//div[contains(@class,'inst-summary')]/ul/li[1]/text()").extract()
		item['bed'] = response.xpath("//div[contains(@class,'inst-summary')]/ul/li[2]/text()").extract()
		item['charge'] = response.xpath("//div[contains(@class,'inst-summary')]/ul/li[3]/text()").extract()
		item['phone_num'] = response.xpath("//div[contains(@class,'inst-summary')]/ul/li[4]/text()").extract()	
		yield item