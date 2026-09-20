from locations import create_location_manager


def main():

    print("SKADOSH LOCATION SYSTEM TEST")
    print("============================")

    manager = create_location_manager()

    print(
        "Total locations:",
        manager.count()
    )

    print()

    for location_type in [
        "SCHOOL",
        "SHOP",
        "GARAGE",
        "RESTAURANT",
        "HOSPITAL",
        "BUSINESS",
        "PROPERTY",
        "RACE",
        "VIP",
        "LANDMARK",
    ]:

        print(
            location_type + ":",
            len(
                manager.by_type(
                    location_type
                )
            )
        )

    print()

    print("Nearby player locations:")

    nearby = manager.nearby(
        2500,
        2500,
        1000
    )

    for location in nearby[:10]:

        print(
            "-",
            location.name,
            "|",
            location.location_type,
            "| distance:",
            round(
                location.distance_to(
                    2500,
                    2500
                ),
                1
            )
        )

    print()

    nearest_school = manager.nearest(
        2500,
        2500,
        "SCHOOL"
    )

    print(
        "Nearest school:",
        nearest_school.name
    )

    print()

    print("LOCATION SYSTEM OK")


if __name__ == "__main__":
    main()
