from dataclasses import dataclass, field


@dataclass
class Vehicle:
    name: str
    vehicle_class: str
    max_speed: float
    acceleration: float
    braking: float
    handling: float
    fuel_capacity: float
    health: float = 100.0

    speed: float = 0.0
    fuel: float = field(init=False)
    engine_on: bool = False
    lights_on: bool = False
    handbrake: bool = False
    occupied: bool = False

    def __post_init__(self):
        self.fuel = self.fuel_capacity

    def enter(self):
        if self.health <= 0:
            return False

        self.occupied = True
        self.engine_on = True
        return True

    def exit(self):
        self.engine_on = False
        self.occupied = False
        self.speed = 0

    def accelerate(self, amount=1.0):
        if not self.occupied or not self.engine_on:
            return

        if self.fuel <= 0:
            return

        if self.handbrake:
            return

        self.speed += self.acceleration * amount
        self.speed = min(self.speed, self.max_speed)

        self.fuel -= 0.02 * amount
        self.fuel = max(0, self.fuel)

    def brake(self, amount=1.0):
        self.speed -= self.braking * amount
        self.speed = max(0, self.speed)

    def reverse(self, amount=1.0):
        if not self.occupied or not self.engine_on:
            return

        self.speed -= self.acceleration * 0.5 * amount
        self.speed = max(-30, self.speed)

    def steer(self, direction):
        if not self.occupied:
            return

        # -1 = left, 0 = straight, +1 = right
        direction = max(-1, min(1, direction))

        steering_effect = self.handling * direction

        return steering_effect

    def refuel(self, amount=None):
        if amount is None:
            self.fuel = self.fuel_capacity
        else:
            self.fuel = min(
                self.fuel_capacity,
                self.fuel + max(0, amount)
            )

    def damage(self, amount):
        self.health -= max(0, amount)
        self.health = max(0, self.health)

        if self.health == 0:
            self.engine_on = False
            self.speed = 0

    def repair(self, amount=None):
        if amount is None:
            self.health = 100
        else:
            self.health = min(100, self.health + max(0, amount))

    def toggle_lights(self):
        self.lights_on = not self.lights_on

    def toggle_handbrake(self):
        self.handbrake = not self.handbrake

    def status(self):
        return {
            "name": self.name,
            "class": self.vehicle_class,
            "speed": round(self.speed, 2),
            "fuel": round(self.fuel, 2),
            "health": round(self.health, 2),
            "engine": self.engine_on,
            "lights": self.lights_on,
            "handbrake": self.handbrake,
            "occupied": self.occupied,
        }


VEHICLE_DATABASE = {
    "Sports Car": {
        "max_speed": 220,
        "acceleration": 7,
        "braking": 8,
        "handling": 8,
        "fuel": 70,
    },

    "Supercar": {
        "max_speed": 300,
        "acceleration": 10,
        "braking": 10,
        "handling": 9,
        "fuel": 65,
    },

    "SUV": {
        "max_speed": 180,
        "acceleration": 5,
        "braking": 7,
        "handling": 6,
        "fuel": 90,
    },

    "Sedan": {
        "max_speed": 170,
        "acceleration": 5,
        "braking": 6,
        "handling": 7,
        "fuel": 75,
    },

    "Taxi": {
        "max_speed": 160,
        "acceleration": 5,
        "braking": 6,
        "handling": 7,
        "fuel": 80,
    },

    "Bus": {
        "max_speed": 120,
        "acceleration": 3,
        "braking": 5,
        "handling": 4,
        "fuel": 150,
    },

    "Truck": {
        "max_speed": 130,
        "acceleration": 3,
        "braking": 5,
        "handling": 4,
        "fuel": 160,
    },

    "Luxury Car": {
        "max_speed": 210,
        "acceleration": 6,
        "braking": 8,
        "handling": 8,
        "fuel": 85,
    },

    "Off-Road": {
        "max_speed": 150,
        "acceleration": 5,
        "braking": 7,
        "handling": 8,
        "fuel": 100,
    },

    "Motorbike": {
        "max_speed": 240,
        "acceleration": 9,
        "braking": 9,
        "handling": 10,
        "fuel": 25,
    },

    "Hover Vehicle": {
        "max_speed": 350,
        "acceleration": 12,
        "braking": 11,
        "handling": 10,
        "fuel": 100,
    },
}


def create_vehicle(vehicle_class):
    data = VEHICLE_DATABASE.get(vehicle_class)

    if data is None:
        raise ValueError(f"Unknown vehicle: {vehicle_class}")

    return Vehicle(
        name=vehicle_class,
        vehicle_class=vehicle_class,
        max_speed=data["max_speed"],
        acceleration=data["acceleration"],
        braking=data["braking"],
        handling=data["handling"],
        fuel_capacity=data["fuel"],
    )
