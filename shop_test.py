from economy import (
    Economy,
    Inventory,
    Shop,
    ITEMS,
    BUSINESSES
)


def main():
    print("SKADOSH ECONOMY TEST")
    print("====================")

    economy = Economy(100000)
    inventory = Inventory()

    print("Starting money: $", economy.money)

    shop = Shop(
        "equipment",
        "SKADOSH Equipment",
        "Equipment"
    )

    shop.add_item("food_pack")
    shop.add_item("med_kit")
    shop.add_item("street_outfit")
    shop.add_item("armor_kit")

    print()
    print("SHOP:", shop.name)

    for item in shop.list_items():
        print(
            "-",
            item.name,
            ": $",
            item.price
        )

    print()
    print("Buying items...")

    shop.buy(
        "food_pack",
        economy,
        inventory,
        2
    )

    shop.buy(
        "med_kit",
        economy,
        inventory,
        1
    )

    shop.buy(
        "street_outfit",
        economy,
        inventory,
        1
    )

    print("Inventory:")
    print(inventory.status())

    print()
    print("Money after purchases:")
    print("$", economy.money)

    print()
    print("Purchasing business...")

    garage = BUSINESSES["garage"]

    purchased = garage.purchase(
        economy
    )

    print(
        "Garage purchased:",
        purchased
    )

    print(
        "Money:",
        economy.money
    )

    print()
    print("Collecting business income...")

    garage.collect_income(
        economy
    )

    print(
        "Money after income:",
        economy.money
    )

    print()
    print("Business owned:",
          garage.owned)

    print()
    print("ECONOMY SYSTEM OK")


if __name__ == "__main__":
    main()
