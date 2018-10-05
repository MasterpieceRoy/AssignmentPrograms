from StockReport import *
import json

class Stock:
    def __init__(self, name, no_of_share, share_price, total_price):
        self.__name = name
        self.__no_of_share = no_of_share
        self.__share_price = share_price
        self.__total_price = total_price

    def __str__(self):
        return "Name:{0}\t No of Share:{1} \tShare Price:{2} \tTotal Price:{3} \t".format(self.__name, self.__no_of_share,
                                                                                  self.__share_price,
                                                                                  self.__total_price)


def stock_report(name_values):
    obj = StockReport()
    for data in name_values:

        name = data["name"]
        obj.set_name(name)

        no_of_share = data["no_of_share"]
        obj.set_no_of_share(no_of_share)

        share_prize = data["share_prize"]
        obj.set_prize(share_prize)

        total_Price = int(no_of_share) * int(share_prize)
        obj.set_total(total_Price)

        contact = Stock(name, no_of_share, share_prize, total_Price)
        print(contact)


class StockOperation:

    stock_data = json.load(open("stockreport.json", "r"))
    name_values = list(stock_data["stock"])
    stock_report(name_values)
