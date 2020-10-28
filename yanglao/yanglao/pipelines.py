from itemadapter import ItemAdapter
from yanglao.settings import MONGO_DB , MONGO_URI
import pymongo


class YanglaoPipeline(object):
    collection = "OLD_PEOPLE"
    def __init__(self, MONGO_URI , MONGO_DB):
        self.mongo_uri = MONGO_URI
        self.mongo_db = MONGO_DB

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            MONGO_URI=crawler.settings.get('MONGO_URI'),
            MONGO_DB=crawler.settings.get('MONGO_DB')
        )
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(item)
        table = self.db[self.collection]
        table.insert_one(data)
        return item


