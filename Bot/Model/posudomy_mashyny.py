


class PosudomyiniMashyny:

    def __init__(self, product_name, price, in_stock):
        self.product_name = product_name
        self.price = price
        self.in_stock = in_stock

    def __repr__(self):
        return f"{self.product_name}: {self.price} -> {self.in_stock}"