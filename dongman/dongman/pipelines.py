# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from dongman.items import DongmanItem
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

class DongmanPipeline(ImagesPipeline):
    def get_media_requests(self, item , info):
        #name = item['name']
        #urls = item['src']
        #for url in urls:
        #    Request(url = url , meta = {'name':name})
        yield Request(url = item['src'] , meta = {'item':item})
    
    def file_path(self , request , info = None , response = None):
        item = request.meta['item']
        filename = item['name']
        return filename + '.jpg'

