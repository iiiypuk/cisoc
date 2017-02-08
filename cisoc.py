#!/usr/bin/env python3

import urllib.request
import lxml.html as html
import re

__author__ = 'Alexander Popov'
__version__ = '0.1.0'
__license__ = 'MIT'


# get countryes list
def getList():
    COUNTRY = list()

    Html = html.parse(urllib.request.urlopen('https://countrycode.org/'))
    table = Html.xpath('//div[@class="visible-sm visible-xs"]//table/tbody/tr')
    for item in table:
        result = re.findall(r'([A-Z].*)', item.text_content())
        iso = result[1].split(' / ')
        COUNTRY.append((result[0], iso[0], iso[1]))

    return(COUNTRY)


# save countryes list in csv file
def CSV():
    countryes = getList()

    with open('./cisoc.csv', 'w+', encoding='utf-8') as f:
        for country in countryes:
            f.write('%s,%s,%s\n' % (country[0], country[1], country[2],))


if __name__ == '__main__':
    CSV()
