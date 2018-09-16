#!/usr/bin/python3
import scrapy


class ReviewspiderSpider(scrapy.Spider):
    name = 'reviewspider'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/JBL-C100SI-Ear-Headphones-Black/product-reviews/B01DEWVZ2C/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews&pageNumber={}'.format(i) for i in range(1,4)]

    def parse(self, response):
        review_body = response.xpath('//span[contains(@class, "a-size-base review-text")]/text()').extract()
        yield {
                'reviews_body' : reviews

            }


