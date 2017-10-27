import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapymercado.items import ScrapymercadoItem


class ScrapymercadoSpider(CrawlSpider):
		name = 'mercado'
		allowed_domain = ['www.mercadolibre.com.mx']
		start_urls = ['https://listado.mercadolibre.com.mx/autos#D[A:autos,L:1]']

		rules = {
			Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="results-section"]/div[2]/ul/li[12]/a'))),
			Rule(LinkExtractor(allow =(), restrict_xpaths = ('//div[contains(@class, "item")]/a')),
							callback = 'parse_item', follow = False)


		}

		def parse_item(self, response):
			ml_item = ScrapymercadoItem()

			ml_item['titulo'] = response.xpath('normalize-space(//*[@id="short-desc"]/div/header/h1)').extract()
			ml_item['anio'] = response.xpath('normalize-space(//*[@id="short-desc"]/div/article/dl/dd[1])').extract()
			ml_item['kilometros'] = response.xpath('normalize-space(//*[@id="short-desc"]/div/article/dl/dd[2])').extract()
			ml_item['precio'] = response.xpath('normalize-space(//*[@id="short-desc"]/div/fieldset/span/span[2])').extract()
			ml_item['ubicacion'] = response.xpath('normalize-space(/html/body/main/div/div/div[1]/div[2]/div[1]/section[2]/p[7]/span)').extract()
			ml_item['tipo'] = response.xpath('normalize-space(/html/body/main/div/div/div[1]/div[1]/section[1]/div[1]/div/div/section/ul/li[1]/span/text())').extract()
			return ml_item