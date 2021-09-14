import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    custom_settings = {
        'FEEDS': {
            'quotes.json': {
                'format': 'json',
                'encoding': 'utf8',
                'fields': ['title', 'top_ten_tags', 'quotes','authors'],
                'overwrite': True
            }
        }
    }


    def __init__(self):
        self.__title = '//h1/a/text()'
        self.__authors = '//small[@class="author" and @itemprop="author"]/text()'
        self.__quotes = '//span[@class="text"]/text()'
        self.__top_ten_tags = '//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a[@class="tag"]/text()'
        self.__next_page_buttom_link = '//ul[@class="pager"]//li[@class="next"]/a/@href'


    def parse_only_quotes(self, response, **kwargs):
        authors = response.xpath(self.__authors).getall()
        quotes = response.xpath(self.__quotes).getall()
        
        if kwargs:
            quotes = kwargs['quotes']
            authors = kwargs['authors']
        quotes.extend(quotes)
        authors.extend(authors)   

        next_page_buttom_link = response.xpath(self.__next_page_buttom_link).get()
        if next_page_buttom_link:
            yield response.follow(
                next_page_buttom_link, 
                callback=self.parse_only_quotes,
                cb_kwargs={'quotes': quotes,'authors':authors }
            )
        else:
            # Guardando las citas y el autor
            yield {
                'quotes': quotes,
                'authors':authors
            }
            # for a,b in zip(quotes,authors):
            #     yield {
            #         'body': {
            #             'quotes': a,
            #             'authors':b
            #         }
            #     }


    def parse(self, response):

        title = response.xpath(self.__title).get()
        authors = response.xpath(self.__authors).getall()
        quotes = response.xpath(self.__quotes).getall()
        top_ten_tags = response.xpath(self.__top_ten_tags).getall()

        yield {
            'title': title,
            'top_ten_tags': top_ten_tags
        }

        next_page_buttom_link = response.xpath(self.__next_page_buttom_link).get()
        if next_page_buttom_link:
            yield response.follow(
                next_page_buttom_link, 
                callback=self.parse_only_quotes,
                cb_kwargs={'quotes': quotes,'authors':authors } # Pasamos argumentos a la otra funcion
            )

