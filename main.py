import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price_unit: float, quantity=0):
        assert price_unit >= 0, f"Price {price_unit} must be greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} must be greater than or equal to zero!"
        self.name = name
        self.price_unit = price_unit
        self.quantity = quantity
        # print("Item Created")
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price_unit * self.quantity

    def apply_discount(self):
        self.price_unit = self.price_unit * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price_unit=float(item.get('price_unit')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def check_is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price_unit}, {self.quantity})"


class Mobile(Item):
    all = []

    def __init__(self, name: str, price_unit: float, quantity=0, broken_phone=0):
        super().__init__(
            name, price_unit, quantity
        )
        assert broken_phone >= 0, f"Broken phone {broken_phone} must be greater than or equal to zero!"
        self.broken_phone = broken_phone
        # print("Item Created")
        Mobile.all.append(self)


mobile1 = Mobile("samsung", 8000, 3, 1)
print(mobile1.calculate_total_price())
