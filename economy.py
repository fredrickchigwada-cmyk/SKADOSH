from dataclasses import dataclass


@dataclass
class Item:
    item_id: str
    name: str
    category: str
    price: int
    description: str = ""


class Economy:
    def __init__(self, starting_money=100000):
        self.money = starting_money
        self.transactions = []

    def can_afford(self, price):
        return self.money >= price

    def buy(self, item, quantity=1):
        total = item.price * quantity

        if not self.can_afford(total):
            return False

        self.money -= total

        self.transactions.append({
            "type": "BUY",
            "item": item.name,
            "quantity": quantity,
            "amount": total
        })

        return True

    def sell(self, item, quantity=1, sell_rate=0.5):
        total = int(
            item.price *
            quantity *
            sell_rate
        )

        self.money += total

        self.transactions.append({
            "type": "SELL",
            "item": item.name,
            "quantity": quantity,
            "amount": total
        })

        return total

    def add_money(self, amount, reason="income"):
        self.money += amount

        self.transactions.append({
            "type": "INCOME",
            "reason": reason,
            "amount": amount
        })

    def spend_money(self, amount, reason="expense"):
        if amount > self.money:
            return False

        self.money -= amount

        self.transactions.append({
            "type": "EXPENSE",
            "reason": reason,
            "amount": amount
        })

        return True


ITEMS = {
    "food_pack": Item(
        "food_pack",
        "Food Pack",
        "Food",
        25,
        "Restores player energy."
    ),

    "med_kit": Item(
        "med_kit",
        "Med Kit",
        "Medical",
        150,
        "Restores player health."
    ),

    "street_outfit": Item(
        "street_outfit",
        "Street Outfit",
        "Clothes",
        500,
        "Custom street clothing."
    ),

    "armor_kit": Item(
        "armor_kit",
        "Armor Kit",
        "Equipment",
        2500,
        "Fictional protective equipment."
    ),

    "speed_upgrade": Item(
        "speed_upgrade",
        "Vehicle Speed Upgrade",
        "Vehicle Upgrade",
        5000,
        "Improves vehicle performance."
    ),

    "handling_upgrade": Item(
        "handling_upgrade",
        "Vehicle Handling Upgrade",
        "Vehicle Upgrade",
        4000,
        "Improves vehicle handling."
    ),

    "radio_upgrade": Item(
        "radio_upgrade",
        "Radio Upgrade",
        "Vehicle Upgrade",
        1500,
        "Unlocks additional radio features."
    ),
}


class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, item_id, quantity=1):
        self.items[item_id] = (
            self.items.get(item_id, 0)
            + quantity
        )

    def remove(self, item_id, quantity=1):
        current = self.items.get(
            item_id,
            0
        )

        if current < quantity:
            return False

        self.items[item_id] = current - quantity

        if self.items[item_id] <= 0:
            del self.items[item_id]

        return True

    def has(self, item_id, quantity=1):
        return self.items.get(
            item_id,
            0
        ) >= quantity

    def count(self, item_id):
        return self.items.get(
            item_id,
            0
        )

    def status(self):
        return dict(self.items)


class Shop:
    def __init__(self, shop_id, name, category):
        self.shop_id = shop_id
        self.name = name
        self.category = category
        self.items = []

    def add_item(self, item_id):
        if item_id in ITEMS:
            self.items.append(item_id)

    def list_items(self):
        return [
            ITEMS[item_id]
            for item_id in self.items
        ]

    def buy(
        self,
        item_id,
        economy,
        inventory,
        quantity=1
    ):
        if item_id not in self.items:
            return False

        item = ITEMS[item_id]

        if economy.buy(item, quantity):
            inventory.add(
                item_id,
                quantity
            )
            return True

        return False


@dataclass
class Business:
    business_id: str
    name: str
    business_type: str
    purchase_price: int
    income_per_cycle: int
    owned: bool = False

    def purchase(self, economy):
        if self.owned:
            return False

        if not economy.spend_money(
            self.purchase_price,
            f"Purchase {self.name}"
        ):
            return False

        self.owned = True
        return True

    def collect_income(self, economy):
        if not self.owned:
            return False

        economy.add_money(
            self.income_per_cycle,
            f"Income from {self.name}"
        )

        return True


BUSINESSES = {
    "garage": Business(
        "garage",
        "SKADOSH Garage",
        "Garage",
        25000,
        2500
    ),

    "restaurant": Business(
        "restaurant",
        "SKADOSH Restaurant",
        "Restaurant",
        50000,
        5000
    ),

    "clothing": Business(
        "clothing",
        "SKADOSH Clothing",
        "Clothing",
        40000,
        4000
    ),

    "dealership": Business(
        "dealership",
        "SKADOSH Motors",
        "Car Dealership",
        100000,
        10000
    ),

    "hotel": Business(
        "hotel",
        "SKADOSH Hotel",
        "Hotel",
        250000,
        25000
    ),

    "nightclub": Business(
        "nightclub",
        "SKADOSH Nightclub",
        "Entertainment",
        150000,
        15000
    ),

    "transport": Business(
        "transport",
        "SKADOSH Transport",
        "Transport",
        125000,
        12000
    ),

    "construction": Business(
        "construction",
        "SKADOSH Construction",
        "Construction",
        200000,
        18000
    ),

    "security": Business(
        "security",
        "SKADOSH Security",
        "Security",
        175000,
        16000
    ),

    "gaming": Business(
        "gaming",
        "SKADOSH Gaming Centre",
        "Gaming",
        90000,
        8500
    ),

    "electronics": Business(
        "electronics",
        "SKADOSH Electronics",
        "Electronics",
        85000,
        7500
    ),
}
