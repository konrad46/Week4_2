class Receipt:

    def __init__(self, date, sale_amt):
        self.__date = date
        self.__sale_amt = sale_amt

    def get_sales(self):
        return self.__sale_amt
