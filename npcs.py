from dataclasses import dataclass
import math
import random


@dataclass
class NPC:
    npc_id: int
    name: str
    role: str
    x: float
    y: float

    state: str = "WANDER"
    speed: float = 2.0
    health: float = 100.0
    target_x: float = 0.0
    target_y: float = 0.0

    def choose_random_target(self, width, height):
        self.target_x = random.uniform(0, width)
        self.target_y = random.uniform(0, height)

    def move_towards(self, target_x, target_y, dt):
        dx = target_x - self.x
        dy = target_y - self.y

        distance = math.hypot(dx, dy)

        if distance < 0.1:
            return

        self.x += (dx / distance) * self.speed * dt
        self.y += (dy / distance) * self.speed * dt

    def update(self, world_width, world_height, player_x, player_y, dt):
        distance_to_player = math.hypot(
            player_x - self.x,
            player_y - self.y
        )

        if self.state == "WANDER":
            if (
                abs(self.x - self.target_x) < 5
                and abs(self.y - self.target_y) < 5
            ):
                self.choose_random_target(
                    world_width,
                    world_height
                )

            self.move_towards(
                self.target_x,
                self.target_y,
                dt
            )

        elif self.state == "FOLLOW":
            self.move_towards(
                player_x,
                player_y,
                dt
            )

        elif self.state == "FLEE":
            dx = self.x - player_x
            dy = self.y - player_y

            distance = math.hypot(dx, dy)

            if distance > 0:
                self.x += (
                    dx / distance
                ) * self.speed * dt

                self.y += (
                    dy / distance
                ) * self.speed * dt

        elif self.state == "CHASE":
            self.move_towards(
                player_x,
                player_y,
                dt
            )

        # Keep NPC inside the world
        self.x = max(
            0,
            min(world_width, self.x)
        )

        self.y = max(
            0,
            min(world_height, self.y)
        )


class NPCManager:
    def __init__(self, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height
        self.npcs = []

        self.next_id = 1

    def spawn(
        self,
        name,
        role,
        x=None,
        y=None
    ):
        if x is None:
            x = random.uniform(0, self.world_width)

        if y is None:
            y = random.uniform(0, self.world_height)

        npc = NPC(
            npc_id=self.next_id,
            name=name,
            role=role,
            x=x,
            y=y
        )

        npc.choose_random_target(
            self.world_width,
            self.world_height
        )

        self.npcs.append(npc)

        self.next_id += 1

        return npc

    def spawn_crowd(self, amount=20):
        roles = [
            "Citizen",
            "Student",
            "Teacher",
            "Shopper",
            "Worker",
            "Driver",
            "Tourist",
            "Business Owner",
        ]

        for i in range(amount):
            self.spawn(
                name=f"NPC_{self.next_id}",
                role=random.choice(roles)
            )

    def update(self, player_x, player_y, dt):
        for npc in self.npcs:
            npc.update(
                self.world_width,
                self.world_height,
                player_x,
                player_y,
                dt
            )

    def nearby(self, player_x, player_y, radius=100):
        result = []

        for npc in self.npcs:
            distance = math.hypot(
                player_x - npc.x,
                player_y - npc.y
            )

            if distance <= radius:
                result.append(npc)

        return result


@dataclass
class TrafficVehicle:
    vehicle_id: int
    x: float
    y: float
    speed: float = 20.0
    direction: int = 1

    def update(self, world_width, dt):
        self.x += self.speed * self.direction * dt

        if self.x > world_width:
            self.x = 0

        if self.x < 0:
            self.x = world_width


class TrafficManager:
    def __init__(self, world_width):
        self.world_width = world_width
        self.vehicles = []

    def spawn_traffic(self, amount=10):
        for i in range(amount):
            vehicle = TrafficVehicle(
                vehicle_id=i + 1,
                x=random.uniform(
                    0,
                    self.world_width
                ),
                y=random.uniform(0, 500),
                speed=random.uniform(10, 35),
                direction=random.choice([-1, 1])
            )

            self.vehicles.append(vehicle)

    def update(self, dt):
        for vehicle in self.vehicles:
            vehicle.update(
                self.world_width,
                dt
            )
