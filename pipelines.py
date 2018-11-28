# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
from hashlib import md5
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
import os

class QbPineline(ImagesPipeline):
    def get_media_requests(self,item,info):
        yield Request(item['download_url'])
    #def file_path(self,request,resnonse= None,info = None):
    #    path = os.path.join('d:/qb',''.join([request.url,'.jpg'])
    #    return path



class ZzTextPipeline(object):

    

    def process_item(self, item, spider):
        if item:
            
            content = requests.get(item['url']).content
            with open('d:/qb/{}.jpg'.format(md5(content).hexdigest()),'wb')as f:
                f.write(content)
                print('文件写入完成')
        return item

    
