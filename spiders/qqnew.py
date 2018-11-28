import scrapy
from zz_text.items import ZzTextItem,QbItem

class QQnewsSpider(scrapy.Spider):
    name = 'qqnews'
    start_urls = ['https://www.qiushibaike.com/pic/page/2/?s=5142602']
    



    def parse(self,response):
        item = QbItem()
        next = response.xpath('//span[contains(text(),"下一页")]/parent::a/@href').extract()[0]
        next_full = response.urljoin(next)
        print(next_full)
        yield scrapy.Request(next_full, callback = self.parse)
        for each in response.css('.thumb'):
            a = each.css('img::attr("src")').extract()[0]
            item['download_url'] = response.urljoin(a)
            print(item)
    
            yield item
