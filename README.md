# Curso de Scrapy
Este repositorio contiene los notebooks del curso en Platzi [Curso de Scrapy](https://platzi.com/cursos/scrapy/)

# Comandos basicos

## Crear Proyecto con Scrapy
```
scrapy startproject nombre_proyecto
```

## Ejecutar Proyecto con Scrapy
```
scrapy crawl name_del_spider
```

## Ejecutar Shell de Scrapy
```
scrapy shell 'url_del_sitio'
```

### Ejemplo de Usos de Xpath en Shell

**Pagina: Quotes**
```
scrapy shell 'http://quotes.toscrape.com/'

#Obtener el titulo
response.xpath('//span[@class="text"]/text()').get()

Obtener el author
response.xpath('//small[@class="author" and @itemprop="author"]/text()').getall()

```

**Pagina: Coin Market Cap**
```
scrapy shell 'https://coinmarketcap.com/'

Obtener el nombre de las criptomendas
response.xpath('//div[@class="sc-16r8icm-0 sc-1teo54s-1 dNOTPP"]/p[@class="sc-1eb5slv-0 iworPT"]/text()').getall()

Obtener el precio de las criptomonedas
response.xpath('//div[@class="sc-131di3y-0 cLgOOr"]/a[@class="cmc-link"]/text()').getall()
```
