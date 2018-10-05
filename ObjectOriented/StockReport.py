
class StockReport:

    def set_name(self, share_name):
        self.__shareName = share_name

    def set_no_of_share(self, no_of_share):
        self.__noOfShare = no_of_share

    def set_prize(self, prize):
        self.__sharePrize = prize

    def set_total(self, total):
        self.__shareTotal = total

    def get_name(self):
        return self.__shareName

    def get_no_of_share(self):
        return self.__noOfShare

    def get_prize(self):
        return self.__sharePrize

    def get_shareTotal(self):
        return self.__shareTotal
