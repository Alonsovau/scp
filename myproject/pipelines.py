# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os
from urllib.request import urlopen

class MyprojectPipeline(object):
    def process_item(self, item, spider):
        return item


class WeatherPipeLine(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y-%m-%d', time.localtime())
        fileName = today + '.txt'
        with open(fileName, 'ab') as f:
            f.write(item['cityDate'].encode('utf8') + b'\t')
            f.write(item['week'].encode('utf8') + b'\t')
            imgName = os.path.basename(item['img'])
            f.write(bytes(imgName, encoding='utf8') + b'\t')
            if os.path.exists(imgName):
                pass
            else:
                with open(imgName, 'wb') as f:
                    response = urlopen(item['img'])
                    f.write(response.read())
            f.write(item['temperature'].encode('utf8') + b'\t')
            f.write(item['weather'].encode('utf8') + b'\t')
            f.write(item['wind'].encode('utf8') + b'\n\n')
            time.sleep(1)
        return item