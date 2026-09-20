import math
import time

from vehicles import create_vehicle


WORLD_WIDTH = 5000
WORLD_HEIGHT = 5000


class World:
    def __init__(self, name="Harare"):
        self.name = name
        self.width = WORLD_WIDTH
        self.height = WORLD_HEIGHT

        self.time_of_day = 8.0
        self.weather = "CLEAR"

        self.player_x = self.width / 2
        self.player_y = self.height / 2

        self.player_heading = 0.0

        self.vehicle = None

    def spawn_vehicle(self, vehicle_class):
        self.vehicle = create_vehicle(vehicle_class)

        self.vehicle.enter()

        return self.vehicle

    def update(self, throttle=0.0, brake=0.0, steering=0.0, dt=1 / 60):
        if self.vehicle is None:
            return

        vehicle = self.vehicle

        # Vehicle acceleration
        if throttle > 0:
            vehicle.accelerate(throttle)

        # Braking
        if brake > 0:
            vehicle.brake(brake)

        # Steering
        if steering != 0:
            steering_strength = vehicle.handling * steering

            # Steering becomes stronger at higher speeds
            speed_factor = min(abs(vehicle.speed) / 100.0, 1.0)

            self.player_heading += (
                steering_strength
                * speed_factor
                * dt
            )

        # Convert speed into world movement
        speed_units = vehicle.speed * dt

        radians = math.radians(self.player_heading)

        self.player_x += math.cos(radians) * speed_units
        self.player_y += math.sin(radians) * speed_units

        # World boundaries
        self.player_x = max(
            0,
            min(self.width, self.player_x)
        )

        self.player_y = max(
            0,
            min(self.height, self.player_y)
        )

        # Time progression
        self.time_of_day += dt / 60

        if self.time_of_day >= 24:
            self.time_of_day -= 24

    def set_weather(self, weather):
        allowed = [
            "CLEAR",
            "RAIN",
            "STORM",
            "FOG",
            "CLOUDY",
        ]

        weather = weather.upper()

        if weather in allowed:
            self.weather = weather
        else:
            raise ValueError("Unknown weather type.")

    def status(self):
        return {
            "map": self.name,
            "x": round(self.player_x, 2),
            "y": round(self.player_y, 2),
            "heading": round(self.player_heading, 2),
            "time": round(self.time_of_day, 2),
            "weather": self.weather,
            "vehicle": (
                self.vehicle.status()
                if self.vehicle
                else None
            ),
        }
