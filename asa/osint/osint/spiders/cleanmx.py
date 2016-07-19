# -*- coding: utf-8 -*-
import scrapy

from datetime import datetime, timedelta


class CleanmxSpider(scrapy.Spider):
    name = "cleanmx"
    allowed_domains = ["clean-mx.de"]
    start_urls = (
        'http://support.clean-mx.de/clean-mx/phishing.php',
    )

    def parse(self, response):
        for content in response.xpath("//table[@class='liste']/tr"):
            tmp_row = content.xpath('td')
            if tmp_row:
                for j in range(len(tmp_row)):
                    # Get id
                    if j == 0:
                        sid = tmp_row[j].xpath('text()').extract()[0].strip()
                        print sid
                    # Get timestamp
                    elif j == 2:
                        origin_time = datetime.strptime(unicode(tmp_row[j].xpath('text()').extract()[0].strip()).encode('utf8'),
                                                        '%Y-%m-%d\xc2\xa0%H:%M:%S')
                        # timestamp to our timezone
                        timestamp = origin_time+timedelta(hours=6)
                        print origin_time
                    # Get URL
                    elif j == 8:
                        url = tmp_row[j].xpath("a[@title='open Url in new Browser at your own risk !']/@href").extract()[0]
                        print url
                    # Get IP
                    elif j == 11:
                        origin_ip = tmp_row[j].xpath('text()').extract()[1]
                        ip = origin_ip.strip()
                        print ip
                    # Get domain name
                    elif j == 14:
                        # dn = unicode(tmp_row[j].text.strip()).encode('utf8').replace('\xc2\xa0', '')
                        dn = tmp_row[j].xpath('text()').extract()[1].strip()
                        print dn
