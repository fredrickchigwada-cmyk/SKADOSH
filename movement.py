class MovementSystem:

    def __init__(self, world_width=5000, world_height=5000):

        self.world_width = float(world_width)
        self.world_height = float(world_height)

        self.min_x = 0.0
        self.min_y = 0.0

        self.max_x = self.world_width
        self.max_y = self.world_height

        self.player_speed = 8.0

        self.vehicle_max_speed = 80.0
        self.vehicle_reverse_speed = 25.0

        self.acceleration = 12.0
        self.braking = 20.0

        self.drag = 4.0

        self.distance_travelled = 0.0

    # --------------------------------------------------
    # LIMIT POSITION TO WORLD
    # --------------------------------------------------

    def clamp_position(self, x, y):

        x = max(self.min_x, min(x, self.max_x))
        y = max(self.min_y, min(y, self.max_y))

        return x, y

    # --------------------------------------------------
    # ON FOOT
    # --------------------------------------------------

    def move_on_foot(self, x, y, commands):

        old_x = x
        old_y = y

        if commands.get("accelerate"):
            y += self.player_speed

        if commands.get("brake"):
            y -= self.player_speed

        if commands.get("steer_left"):
            x -= self.player_speed

        if commands.get("steer_right"):
            x += self.player_speed

        x, y = self.clamp_position(x, y)

        self.distance_travelled += self.distance(
            old_x,
            old_y,
            x,
            y
        )

        return x, y

    # --------------------------------------------------
    # VEHICLE
    # --------------------------------------------------

    def update_vehicle(self, x, y, speed, commands):

        old_x = x
        old_y = y

        # ACCELERATION
        if commands.get("accelerate"):
            speed += self.acceleration

        # BRAKE / REVERSE
        if commands.get("brake"):
            speed -= self.braking

        # NATURAL DRAG
        if not commands.get("accelerate") and not commands.get("brake"):

            if speed > 0:
                speed -= self.drag

            elif speed < 0:
                speed += self.drag

        # HANDBRAKE
        if commands.get("handbrake"):
            speed *= 0.70

        # SPEED LIMITS
        speed = max(
            -self.vehicle_reverse_speed,
            min(speed, self.vehicle_max_speed)
        )

        # STEERING
        steering = 0.0

        if commands.get("steer_left"):
            steering = -1.0

        if commands.get("steer_right"):
            steering = 1.0

        direction = 1.0

        if speed < 0:
            direction = -1.0

        movement = abs(speed) * 0.05

        x += steering * movement * direction
        y += movement * direction

        x, y = self.clamp_position(x, y)

        self.distance_travelled += self.distance(
            old_x,
            old_y,
            x,
            y
        )

        return x, y, speed

    # --------------------------------------------------
    # DISTANCE
    # --------------------------------------------------

    @staticmethod
    def distance(x1, y1, x2, y2):

        dx = x2 - x1
        dy = y2 - y1

        return (dx * dx + dy * dy) ** 0.5

    # --------------------------------------------------
    # STATUS
    # --------------------------------------------------

    def status(self):

        return {
            "world_width": self.world_width,
            "world_height": self.world_height,
            "player_speed": self.player_speed,
            "vehicle_max_speed": self.vehicle_max_speed,
            "vehicle_reverse_speed": self.vehicle_reverse_speed,
            "distance_travelled": round(
                self.distance_travelled,
                2
            )
        }


def test():

    movement = MovementSystem()

    x = 2500.0
    y = 2500.0

    print("SKADOSH MOVEMENT SYSTEM")
    print("-----------------------")

    print("Starting position:", x, y)

    # Walk
    for _ in range(5):

        x, y = movement.move_on_foot(
            x,
            y,
            {
                "accelerate": True
            }
        )

    print("After walking:", round(x, 2), round(y, 2))

    # Vehicle
    speed = 0.0

    for _ in range(5):

        x, y, speed = movement.update_vehicle(
            x,
            y,
            speed,
            {
                "accelerate": True
            }
        )

    print(
        "After driving:",
        round(x, 2),
        round(y, 2)
    )

    print("Vehicle speed:", round(speed, 2))

    # Steering
    for _ in range(5):

        x, y, speed = movement.update_vehicle(
            x,
            y,
            speed,
            {
                "accelerate": True,
                "steer_right": True
            }
        )

    print(
        "After turning:",
        round(x, 2),
        round(y, 2)
    )

    # Boundary test
    x = 999999
    y = 999999

    x, y = movement.clamp_position(x, y)

    print(
        "Boundary test:",
        x,
        y
    )

    print(
        "Distance travelled:",
        round(movement.distance_travelled, 2)
    )

    print()
    print("MOVEMENT SYSTEM OK")


if __name__ == "__main__":
    test()
