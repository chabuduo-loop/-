# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
import json
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class YanglaoSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class YanglaoDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
class Random_Proxy:
    def __init__(self):
        self.proxy_url = r"http://api.wandoudl.com/api/ip?app_key=bdfff8ff91f441bc07272adc5f8e26e1&pack=0&num=5&xy=1&type=2&lb=\r\n&port=4&mr=1&"
        self.test_url = r"https://www.baidu.com/?tn=62095104_19_oem_dg"
        self.proxy_list = []
        self.count = 0
        self.eve_count = 0

    def get_proxy(self):
        temp_data = requests.get(url = self.proxy_url).text
        contents = json.loads(temp_data)['data']
        for content in contents:
            self.proxy_list.append({
                'ip':content['ip'],
                'port':content['port']
            })
    
    def change_proxy(self,request):
        request.meta['proxy'] = 'http://' + str(self.proxy_list[self.count - 1]['ip']) + ':' + str(self.proxy_list[self.count-1]['port'])

    def yanzheng(self):
        requests.get(url = self.test_url, proxies = {'http':str(self.proxy_list[self.count - 1]['ip']) + ':' + str(self.proxy_list[self.count-1]['port'])}, timeout = 5)
    
    def ifused(self,request):
        try:
            self.change_proxy(request)
            self.yanzheng()
        except:
            if self.count == 0 or self.count == 5:
                self.get_proxy()
                self.count += 1
            self.count += 1
            self.ifused(request)
    
    def process_request(self, request , spider):
        if self.count ==0 or self.count ==5:
            self.get_proxy()
            self.count += 1
        if self.eve_count == 10:
            self.eve_count = 0
            self.count += 1
        else:
            self.eve_count += 1
        self.ifused(request)



