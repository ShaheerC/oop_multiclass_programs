from product import Product

class Cart:

    def __init__ (self):
        self.cart_list = []

    def add (self, item):
        self.cart_list.append(item)

    def remove (self, item):
        self.cart_list.remove(item)

    def before_tax(self):
        for product in self.cart_list:
            return product.base

    def after_tax(self):
        for product in self.cart_list:
            return product.total_price()

apples = Product('apples', 2, 10)
print(apples.total_price())

oranges = Product('oranges', 4, 10)

supremecart = Cart()

supremecart.add(apples)
supremecart.add(oranges)

for items in supremecart.cart_list:
    print(items)

supremecart.remove(oranges)

for items in supremecart.cart_list:
    print(items)

print(supremecart.before_tax())
print(supremecart.after_tax())