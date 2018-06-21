# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    #爬虫名称  启动的时候（scrapy crawl  *）
    name = 'itcast'
    #爬虫允许的域
    allowed_domains = ['http://www.itcast.cn']
    #初始爬取地址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#atest']

    def parse(self, response):
        node_list = response.xpath("//div[@class = 'li_txt']")
        #用来存储所有item文件
        #items = []
        for node in node_list:
            item = ItcastItem()
            #.exract() 将xpath对象转换为Unicode 字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            #返回提取到的每个item数据，后回来继续执行后面的 代码
            yield  item
        #pass
