class CarLamp:
    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image

    def __repr__(self):
        return f"{self.name}: {self.price} -> {self.image}"

