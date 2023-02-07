class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price_unit: float, quantity=0):
        assert price_unit >= 0, f"Price {price_unit} must be greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} must be greater than or equal to zero!"
        self.name = name
        self.price_unit = price_unit
        self.quantity = quantity
        print("Item Created")
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price_unit * self.quantity

    def apply_discount(self):
        self.price_unit = self.price_unit * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price_unit}, {self.quantity})"


Item1 = Item('Mobile', 5000, 5)
Item2 = Item('Laptop', 15000, 2)
Item3 = Item('Mouse', 50, 8)
Item4 = Item('Keyboard', 500, 10)
Item5 = Item('Microphone', 800, 7)
print(Item.all)
