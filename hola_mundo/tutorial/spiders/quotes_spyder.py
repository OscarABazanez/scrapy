import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    def parse(self, response):
        with open('resultado.html','w',encoding='utf8') as f:
            f.write(response.text)
             
