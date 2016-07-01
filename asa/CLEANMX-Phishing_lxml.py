#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests
import StringIO

from datetime import datetime, timedelta
from lxml import etree

if __name__ == '__main__':
    url = "http://support.clean-mx.de/clean-mx/phishing.php"
    page = requests.get(url, verify=False)

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO.StringIO(page.text), parser)

    dl_dict = {}
    # xpath = "//ul[@id='treemenu1']/li[text()='%s']/ul/li[text()='%s']/ul/li[text()='%s']/ul/li/a" % (year, month, int(day)-2)
    # xpath = "//table[@class='liste']/tr/td[@class='zellennormal']/text()"
    # xpath = "//table[@class='liste']/tr/td[@class!='th']/text()"
    xpath = "//table[@class='liste']/tr"
    content = tree.xpath(xpath)

    result = {}
    for i in content:
        tmp_row = i.xpath('td')
        if tmp_row:
            for j in range(len(tmp_row)):
                # Get id
                if j == 0:
                    sid = unicode(tmp_row[j].text.strip()).encode('utf8')
                    print sid
                # Get timestamp
                elif j == 2:
                    origin_time = datetime.strptime(unicode(tmp_row[j].text.strip()).encode('utf8'),
                                                    '%Y-%m-%d\xc2\xa0%H:%M:%S')
                    # timestamp to our timezone
                    timestamp = origin_time+timedelta(hours=6)
                    print origin_time
                # Get URL
                elif j == 8:
                    url = tmp_row[j].xpath("a[@title='open Url in new Browser at your own risk !']/@href")[0]
                    print url
                # Get IP
                elif j == 11:
                    origin_ip = tmp_row[j].xpath('text()')[1]
                    ip = origin_ip.strip()
                    print ip
                # Get domain name
                elif j == 14:
                    # dn = unicode(tmp_row[j].text.strip()).encode('utf8').replace('\xc2\xa0', '')
                    dn = tmp_row[j].xpath('text()')[1].strip()
                    print dn

                # result[sid] = [timestamp, ip, dn]

    # for i in sorted(result):
    #     print i
    #     print result[i]
