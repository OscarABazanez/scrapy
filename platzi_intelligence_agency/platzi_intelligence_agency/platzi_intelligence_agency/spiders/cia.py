import scrapy


class SpiderCia(scrapy.Spider):

    name = 'cia'
    start_urls = [
        'https://www.cia.gov/readingroom/historical-collections'
    ]
    custom_settings = {
        'FEEDS': {
            'quotes.json': {
                'format': 'json',
                'encoding': 'utf8',
                'fields': ['url', 'title', 'body'],
                'overwrite': True
            },
            'quotes.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'fields': ['url', 'title', 'body'],
                'overwrite': True
            }
        },
        'CONCURRENT_REQUESTS':24,
        'MEMUSAGE_LIMIT_MB':1024,
        'MEMUSAGE_NOTIFY_MAIL':['zombie-buzz@hotmail.com'],
        'ROBOTSTXT_OBEY':True,
    }


    def __init__(self):
        self.links_desclassified = '//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href'
        self.title = '//h1[@class="documentFirstHeading"]/text()'
        self.paragraph = '//div[@class="field-item even"]/p[not(@class)]/text()'


    def parse(self, response):
        links_desclassified = response.xpath(self.links_desclassified).getall()

        for link in links_desclassified:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url':response.urljoin(link)})
            
    
    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath(self.title).get()
        paragraph = response.xpath(self.paragraph).get()

        yield {
            'url': link,
            'title': title,
            'body':paragraph
        }