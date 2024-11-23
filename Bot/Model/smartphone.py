

class Smartphone:
    def __init__(self, name, old_price, new_price):
        self.name = name
        self.old_price = old_price
        self.new_price = new_price

    def __repr__(self):
        return f"имя {self.name}: {self.old_price} -> {self.new_price}"

