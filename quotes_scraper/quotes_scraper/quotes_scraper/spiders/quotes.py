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
                'fields': ['title', 'top_tags', 'quotes','authors'],
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
        current_authors = response.xpath(self.__authors).getall()
        current_quotes = response.xpath(self.__quotes).getall()
        current_quotes_tags = response.xpath(self.__quotes_tags).getall()
        
        if kwargs:
            quotes = kwargs['quotes']

        quotes = self.get_full_quotes(quotes, current_quotes, current_authors,current_quotes_tags)

        next_page_buttom_link = response.xpath(self.__next_page_buttom_link).get()
        if next_page_buttom_link:
            yield response.follow(
                next_page_buttom_link, 
                callback=self.parse_only_quotes,
                cb_kwargs={'quotes': quotes}
            )
        else:
            # Guardando las citas y el autor
            yield {
                'quotes': quotes,
            }



    def parse(self, response):
        title = response.xpath(self.__title).get()
        current_authors = response.xpath(self.__authors).getall()
        current_quotes = response.xpath(self.__quotes).getall()
        current_quotes_tags = response.xpath(self.__quotes_tags).getall()
        top_tags = response.xpath(self.__top_tags).getall()

        quotes = []
        quotes = self.get_full_quotes([], current_quotes, current_authors,current_quotes_tags)

        # Obtener la cantidad de top deseado
        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            top_tags = top_tags[:top]


        yield {
            'title': title,
            'top_tags': top_tags
        }

        next_page_buttom_link = response.xpath(self.__next_page_buttom_link).get()
        if next_page_buttom_link:
            yield response.follow(
                next_page_buttom_link, 
                callback=self.parse_only_quotes,
                cb_kwargs={'quotes': quotes} # Pasamos argumentos a la otra funcion
            )
            

    def get_full_quotes(self, quotes, current_quotes, current_authors,current_quotes_tags):
        if len(current_quotes) == len(current_authors):
            for quote, author, tags in zip(current_quotes, current_authors,current_quotes_tags):
                full_quote = {
                'quote': quote,
                'author': author,
                'tags': tags,
                }
                quotes.append(full_quote)
        return quotes
