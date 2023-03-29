


import doctest


class Cellphone:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_data(self):
        string = "Make: {0}, Model: {1}, Year: {2}, Price: ${3:.2f}"
        info = string.format(self.make, self.model, self.year, self.price)
        print(info)

    def depreciated(self, years):
        DEPRECIATION_RATE = 0.67
        dep_price = self.price
        for i in range(years):
            dep_price = dep_price * DEPRECIATION_RATE
        string = "Depreciated value after{0} years: ${1:.2f}"
        info = string.format(years, dep_price)
        print(info)

if __name__ == "__main__":
    doctest.testmod(verbose=False)
    c1 = Cellphone("Nokia", "2270", 2003, 600)
    c1.display_data()
    c1.depreciated(2)
    

