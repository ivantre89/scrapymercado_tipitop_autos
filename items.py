# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapymercadoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
	titulo = scrapy.Field()
	anio = scrapy.Field()
	kilometros = scrapy.Field()
	precio = scrapy.Field()
	ubicacion = scrapy.Field()
	tipo = scrapy.Field()
