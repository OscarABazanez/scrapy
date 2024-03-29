# Curso de Scrapy
Este repositorio contiene los notebooks del curso en Platzi [Curso de Scrapy](https://platzi.com/cursos/scrapy/)

# Comandos basicos

## Crear Proyecto con Scrapy
```
scrapy startproject nombre_proyecto
```

## Ejecutar Proyecto con Scrapy
```
scrapy crawl name_spider
```

## Ejecutar Shell de Scrapy
```
scrapy shell 'url_del_sitio'
```

## Guardar datos en un archivo
```
scrapy crawl name_spider -o nombre_archivo.csv
```
## Argumentos por consola
Top **n** tags
```
scrapy crawl name_spider -a top=5
```
### Ejemplo de Usos de Xpath en Shell

**Pagina: Quotes**
```
scrapy shell 'http://quotes.toscrape.com/'

# Obtener el titulo
response.xpath('//h1/a/text()').get()

# Obtener las citas
response.xpath('//span[@class="text"]/text()').get()

# Obtener el author
response.xpath('//small[@class="author" and @itemprop="author"]/text()').getall()

# Obtener Top Ten tags
response.xpath('//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a[@class="tag"]/text()').getall()

# Boton de siguiente pagina
response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
```
**Ejemplo de Shell en Coin Market Cap**
```
scrapy shell 'https://coinmarketcap.com/'

# Obtener el nombre de las criptomendas
response.xpath('//div[@class="sc-16r8icm-0 sc-1teo54s-1 dNOTPP"]/p[@class="sc-1eb5slv-0 iworPT"]/text()').getall()

# Obtener el precio de las criptomonedas
response.xpath('//div[@class="sc-131di3y-0 cLgOOr"]/a[@class="cmc-link"]/text()').getall()
```

# Scraper CIA

```
scrapy shell https://www.cia.gov/readingroom/historical-collections

# Obtener los links de los archivos desclasificados
response.xpath('//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').getall()

# Titulo del archivo desclasificado
response.xpath('//h1[@class="documentFirstHeading"]/text()').get()

# Obtener el contenido del archivo desclasificado
response.xpath('//div[@class="field-item even"]/p[not(@class)]/text()').getall()
```

# Usando la API publica de Scrapy Cloud
[Documentacion de Scrapy Cloud](https://docs.zyte.com/scrapy-cloud.html)
```
# Podemos ejecutar el spider de forma remota por ejemplo desde nuestro BackEnd o linea de comando.
curl -u APIKEY: https://app.scrapinghub.com/api/run.json -d project=PROJECT -d spider=SPIDER

# Obtener los datos de un proceso:
curl -u APIKEY https://storage.scrapinghub.com/items/PROJECT_ID/SPYDER_NUMBER/JOB_NUMBER
```