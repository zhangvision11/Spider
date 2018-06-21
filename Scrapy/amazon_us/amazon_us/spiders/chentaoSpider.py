# -*- coding: utf-8 -*-
import scrapy
from amazon_us.items import AmazonUsItem

class ChentaospiderSpider(scrapy.Spider):
    name = 'chentaoSpider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Girl-Wash-Your-Face-Believing/dp/1400201659?pd_rd_wg=nJ3FL&pd_rd_r=fe24e1e8-c60e-48b9-93d4-e5500a260724&pd_rd_w=RWT6t&ref_=pd_gw_ri&pf_rd_r=CWWDR9W3VGE7TTNR1X8P&pf_rd_p=a76d819d-d46f-5d89-be3e-dc07c7b5bb0c']

    def parse(self, response):
        item = AmazonUsItem()
        item['price'] = response.xpath("//span[@class='a-size-medium a-color-price offer-price a-text-normal']/text()").extract()
        item['zuozhe'] = response.xpath("//a[@class='a-link-normal contributorNameID']/text()").extract()
        item['shangBiao'] = response.xpath("//span[@class='a-size-medium a-color-secondary a-text-normal'][1]/text()").extract()
        item['sjTime'] = response.xpath("//span[@class='a-size-medium a-color-secondary a-text-normal'][2]/text()").extract()
        item['stars'] = response.xpath("//span[@id = 'acrPopover']//span[@class='a-icon-alt']/text()").extract()
        #item['haoPing']=response.xpath
        yield  item
