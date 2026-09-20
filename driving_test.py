from world import World


def main():
    print("SKADOSH DRIVING WORLD TEST")
    print("==========================")

    world = World("Harare")

    print("Map:", world.name)
    print("World size:", world.width, "x", world.height)

    print()
    print("Spawning Sports Car...")

    car = world.spawn_vehicle("Sports Car")

    print("Vehicle:", car.name)
    print("Starting position:")
    print(
        "X =", round(world.player_x, 2),
        "Y =", round(world.player_y, 2)
    )

    print()
    print("Driving forward...")

    for _ in range(120):
        world.update(
            throttle=1.0,
            steering=0.0,
            dt=1 / 60
        )

    print("Speed:", round(car.speed, 2))

    print("Position:")
    print(
        "X =", round(world.player_x, 2),
        "Y =", round(world.player_y, 2)
    )

    print()
    print("Turning right...")

    for _ in range(120):
        world.update(
            throttle=1.0,
            steering=1.0,
            dt=1 / 60
        )

    print("Heading:", round(world.player_heading, 2))
    print("Position:")
    print(
        "X =", round(world.player_x, 2),
        "Y =", round(world.player_y, 2)
    )

    print()
    print("Testing weather...")
    world.set_weather("RAIN")
    print("Weather:", world.weather)

    print()
    print("WORLD DRIVING SYSTEM OK")


if __name__ == "__main__":
    main()
