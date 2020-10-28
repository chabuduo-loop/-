from scrapy.spiders import Spider
from scrapy import Request
from dongman.items import DongmanItem


class PictureSpider(Spider):
    name = 'picture'

    def start_requests(self):
        url = "https://www.mmonly.cc/ktmh/"
        yield Request(url ,callback = self.parse1)

    def parse1(self, response):
        for i in range(5):
            new_url = "https://www.mmonly.cc/ktmh/list_28_%d.html"%(i)
            yield Request(new_url , callback = self.parse)
    def parse(self, response):
        contents = response.xpath("//div[contains(@class,'item_list infinite_scroll masonry')]/div")
        for content in contents:
            item = DongmanItem()
            item['src'] = content.xpath('.//a/img/@src').extract()[0]
            item['name'] = content.xpath('.//a/img/@alt').extract()[0]
            
            yield item
        
