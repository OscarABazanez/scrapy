import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes-csv'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    custom_settings = {
        'FEEDS': {
            'quotes.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'fields': ['title', 'top_tags','quotes','authors','tags'],
                'overwrite': True
            }
        },
        'CONCURRENT_REQUESTS':24,
        'MEMUSAGE_LIMIT_MB':1024,
        'MEMUSAGE_NOTIFY_MAIL':['zombie-buzz@hotmail.com'],
        'ROBOTSTXT_OBEY':True,
    }


    def __init__(self,top=''):
        self.__title = '//h1/a/text()'
        self.__authors = '//small[@class="author" and @itemprop="author"]/text()'
        self.__quotes = '//span[@class="text"]/text()'
        self.__quotes_tags = '//div[@class="tags"]//meta[@class="keywords" and @itemprop="keywords"]/@content'
        self.__top_tags = '//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a[@class="tag"]/text()'
        self.__next_page_buttom_link = '//ul[@class="pager"]//li[@class="next"]/a/@href'
        self.top = top


    def parse_only_quotes(self, response, **kwargs):
        authors = response.xpath(self.__authors).getall()
        quotes = response.xpath(self.__quotes).getall()
        quotes_tags = response.xpath(self.__quotes_tags).getall()
        next_page_buttom_link = response.xpath(self.__next_page_buttom_link).get()

        if kwargs:
            quotes = kwargs['quotes']

        # Guardando las citas, tags y el autor
        for quote, author, tags in zip(quotes, authors, quotes_tags):
            yield {
            'quotes': quote,
            'authors': author,
            'tags': tags,
            }

        if next_page_buttom_link:
            yield response.follow(
                next_page_buttom_link, 
                callback=self.parse_only_quotes,
                cb_kwargs={'quotes': quotes}
            )



    def parse(self, response):
        title = response.xpath(self.__title).get()
        authors = response.xpath(self.__authors).getall()
        quotes = response.xpath(self.__quotes).getall()
        quotes_tags = response.xpath(self.__quotes_tags).getall()
        top_tags = response.xpath(self.__top_tags).getall()
        next_page_buttom_link = response.xpath(self.__next_page_buttom_link).get()

        # Obtener la cantidad de top deseado
        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            top_tags = top_tags[:top]

        yield {
            'title': title,
            'top_tags': top_tags
        }

        for quote, author, tags in zip(quotes, authors, quotes_tags):
            yield {
            'quotes': quote,
            'authors': author,
            'tags': tags,
            }
        
        if next_page_buttom_link:
            yield response.follow(
                next_page_buttom_link, 
                callback=self.parse_only_quotes,
                cb_kwargs={'quotes': quotes} # Pasamos argumentos a la otra funcion
            )
