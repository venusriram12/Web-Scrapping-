# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo

#from pymongo import MongoClient

class MedicinePipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        db = self.conn["medicine"]
        self.collection = db['data_tb']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
