class Product:
    
    def __init__(self, name, base, tax):
        self.name = name
        self.base = base
        self.tax = tax

    def __str__(self):
        return "PRODUCT: name: {} - base: {} - tax: {}".format(self.name, self.base, self.tax)

    def total_price(self):
        return self.base * (self.tax / 100 + 1)


