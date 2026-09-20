from vehicles import create_vehicle


def main():
    print("SKADOSH VEHICLE SYSTEM TEST")
    print("============================")

    car = create_vehicle("Sports Car")

    print("Created:", car.name)
    print("Class:", car.vehicle_class)
    print("Max speed:", car.max_speed)

    print()
    print("Entering vehicle...")
    assert car.enter()

    print("Engine:", car.engine_on)

    print()
    print("Accelerating...")
    for _ in range(10):
        car.accelerate()

    print("Speed:", round(car.speed, 2))
    print("Fuel:", round(car.fuel, 2))

    print()
    print("Steering left...")
    steering = car.steer(-1)
    print("Steering value:", steering)

    print()
    print("Braking...")
    car.brake()
    print("Speed:", round(car.speed, 2))

    print()
    print("Turning lights on...")
    car.toggle_lights()
    print("Lights:", car.lights_on)

    print()
    print("Applying damage...")
    car.damage(25)
    print("Health:", car.health)

    print()
    print("Repairing...")
    car.repair()
    print("Health:", car.health)

    print()
    print("Exiting vehicle...")
    car.exit()

    print("Occupied:", car.occupied)
    print("Engine:", car.engine_on)

    print()
    print("VEHICLE SYSTEM OK")


if __name__ == "__main__":
    main()
