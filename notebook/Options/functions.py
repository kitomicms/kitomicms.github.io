from lxml import html,cssselect
import requests
import sys


def get_quote(tickers):
    global result
    result = []
    global ticker
    for ticker in tickers:
        if ticker == "":
            result.append('')
        else:
            page = requests.get('http://dbpower.com.hk/en/quote/quote-warrant/code/' + ticker)
            tree = html.fromstring(page.content)
            lastprice_path = '//*[@id="column_left"]/article/div/div/ul/li[1]/text()'
            change_path = '//*[@id="column_left"]/article/div/div/ul/li[2]/span/text()'

            quote = tree.xpath(lastprice_path)
            for foo in quote:
                #string = string + foo
                if foo == "":
                    print "empty"
                else:
                    result.append(foo.encode("utf-8"))



    return result
