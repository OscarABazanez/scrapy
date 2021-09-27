import scrapy
import json

class PetSpider(scrapy.Spider):
    name = 'pet'
    start_urls = [
        'https://www.petco.com.mx/petco/en/PRODUCTOS/Perro/Alimento/c/01-01-00?siteName=Petco+Mexico&siteUid=petco#'
    ]
    custom_settings = {
        'FEEDS': {
            'pet.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'fields': ['url','title_product','discount_product','price_product','rating_product','image_product','category_product','borrar'],
                'overwrite': True
            }
        },
        'CONCURRENT_REQUESTS':24,
        'MEMUSAGE_LIMIT_MB':1024,
        'MEMUSAGE_NOTIFY_MAIL':['zombie-buzz@hotmail.com'],
        'ROBOTSTXT_OBEY':True,
    }


    def parse(self,response):
        link_categorias_alimentos = response.xpath('//div[@id="product-facet"]/div[@class="facet js-facet"][3]/div[@class="facet__values js-facet-values js-facet-form body-cat"]//a[starts-with(@href, "/petco/en/PRODUCTOS/Perro/Alimento")]/@href').getall()
        link_text_categorias_alimentos = response.xpath('//div[@id="product-facet"]/div[@class="facet js-facet"][3]/div[@class="facet__values js-facet-values js-facet-form body-cat"]//a[starts-with(@href, "/petco/en/PRODUCTOS/Perro/Alimento")]/text()').getall()
        link_categorias_alimentos = set(link_categorias_alimentos)
        for link in link_categorias_alimentos:
            # print(response.urljoin(link))
            yield response.follow(link, callback=self.parse_link,cb_kwargs={'url':response.urljoin(link),'url_text':link_text_categorias_alimentos})


    def parse_link(self, response, **kwargs):
        if kwargs:
            link = kwargs['url']
            url_text = kwargs['url_text']
        titles_products = response.xpath('//div[@class="product__listing product__grid"]//div[@class="product-item hidden-xs "]//a[@class="name"]/text()').getall()
        images_products = response.xpath('//div[@class="product__listing product__grid"]//div[@class="product-item hidden-xs "]//img/@src').getall()
        ratings_products = response.xpath('//div[@class="product__listing product__grid"]//div[@class="product-item hidden-xs "]//div[@class="rating-stars pull-left js-ratingCalc "]/@data-rating').getall()

        for title_product,url_text,image_product,rating_product in zip(titles_products,url_text,images_products,ratings_products):

            if title_product != '\n':
                title_product = self._remove_new_lines_data(title_product)
                rating_product = json.loads(rating_product)
                price_product = response.xpath('//div[@class="product__listing product__grid"]//div[@class="product-item hidden-xs "]//div[@class="price no-promotion-price"]/text()').get()
                if not price_product:
                    price_product = response.xpath('//div[@class="product__listing product__grid"]//div[@class="product-item hidden-xs "]//div[@class="price "]//span[@class=" beforePrice priceEasyBuy"]/text()').get()

                discount_product = response.xpath('//div[@class="product__listing product__grid"]//div[@class="product-item hidden-xs "]//div[@class="price "]//span[@class=" discountedPrice"]/text()').get()
                if not discount_product:
                    discount_product = 0
                discount_product = self._remove_new_lines_data(discount_product)
                discount_product = self._format_price_data(discount_product)
                price_product = self._remove_new_lines_data(price_product)
                price_product = self._format_price_data(price_product)
                url_product = response.xpath('//div[@class="product__listing product__grid"]//div[@class="product-item hidden-xs "]//a[@class="thumb"]/@href').get()
                yield {
                    'url': response.urljoin(url_product),
                    'title_product': title_product,
                    'discount_product': discount_product,
                    'price_product': price_product,
                    'rating_product': rating_product['rating'],
                    'image_product': response.urljoin(image_product),
                    'category_product': url_text,
                    'borrar': link,
                }

    
    def _remove_new_lines_data(self,data):
        data = data.replace('\n','')
        return data


    def _format_price_data(self,data):
        data = data.replace('$','').replace('Antes ','')
        return data