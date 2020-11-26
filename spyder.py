import scrapy
from scrapy import Request


# from ..items import MedicineItem


class Medicine(scrapy.Spider):
    name = "medicine"
    #allowed_domain = "https://www.yourdiscountchemist.com.au/"




    #page_number = 10
    start_urls = {
        "https://www.yourdiscountchemist.com.au/"
    }
    def parse(self,response):

        for link in response.css(".level-top::attr(href)").extract():
            link = response.urljoin(link)
            yield Request(link, callback=self.parse_main)


         


    def parse_main(self, response):
        for link in response.css(".product-item-link::attr(href)").extract():
            link = response.urljoin(link)
            yield Request(link, callback=self.parse_category)
        next_link = response.css(".action.next::attr(href)").get()
        if next_link :
            next_link = response.urljoin(next_link)
            yield Request(next_link, callback=self.parse_main)




    def parse_category(self, response):

        yield {
            "name": response.css(".page-title span::text").extract(),
            "cost": response.css(".price").css("::text").extract(),
            "saving": response.css(".msrp-savings").css("::text").extract(),
            "overview": response.css(".value p::text").extract(),
             "link" : response.url
            # "instructions": response.css(".value b+ p::text")[0].extract() + response.css(".value b+ p::text")[1].extract(),
            # "safety": response.css(".value b+ p::text")[2].extract()

            }
        #next_link = response.css(".action.next::attr(href)").get()
        #if next_link:
         #  next_link = response.urljoin(next_link)
          # yield Request(next_link, callback=self.parse_main)


        #next_page = 'https://www.yourdiscountchemist.com.au/perfume.html?p=' + str(Medicine.page_number) + ' '
        #if Medicine.page_number <= 3:
        #    Medicine.page_number += 1
        #    yield response.follow(next_page, callback=self.parse)
