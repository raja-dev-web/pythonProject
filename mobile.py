from item import Item


class Mobile(Item):

    def __init__(self, name: str, price_unit: float, quantity=0, broken_phone=0):
        super().__init__(
            name, price_unit, quantity
        )
        assert broken_phone >= 0, f"Broken phone {broken_phone} must be greater than or equal to zero!"
        self.broken_phone = broken_phone
        # print("Item Created")
        # Mobile.all.append(self)


mobile1 = Mobile("samsung", 8000, 3, 1)
# print(mobile1.calculate_total_price())
print(Item.all)
print(Mobile.all)