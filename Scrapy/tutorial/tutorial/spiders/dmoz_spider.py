import scrapy
class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        "https://www.imooc.com/course/list?c=test",
        "https://www.imooc.com/course/list?c=linux"
    ]
    def parse(self, response):
        filename = response.url.split('=')[-1]
        with open(filename,'wb') as f :
            f.write(response.body)
