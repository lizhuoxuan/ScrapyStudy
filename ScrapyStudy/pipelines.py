# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ScrapystudyPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # for image_url in item['imglink']:
        imglink = item['imglink']
        yield scrapy.Request(imglink)

    # def item_completed(self, results, item, info):
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     item['imglink'] = image_paths
    #     return item