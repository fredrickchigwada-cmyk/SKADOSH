import time
import random

from control_game import ControlDrivenGame


class LiveWorld:

    def __init__(self):

        self.engine = ControlDrivenGame()

        # ---------------------------------------------
        # WORLD
        # ---------------------------------------------

        self.running = True

        self.tick = 0
        self.game_time = 8.0

        self.day_length = 24.0

        self.weather = "CLEAR"

        self.weather_options = [
            "CLEAR",
            "CLOUDY",
            "RAIN",
            "FOG",
            "STORM"
        ]

        # ---------------------------------------------
        # PLAYER
        # ---------------------------------------------

        self.health = 100.0

        # ---------------------------------------------
        # VEHICLE
        # ---------------------------------------------

        self.fuel = 100.0

        # ---------------------------------------------
        # WORLD STATISTICS
        # ---------------------------------------------

        self.npc_count = 50
        self.traffic_count = 20

        self.active_mission = "Welcome to SKADOSH"

        self.gps_distance = 707.11

        # ---------------------------------------------
        # SAVE TIMER
        # ---------------------------------------------

        self.save_timer = 0.0
        self.auto_save_interval = 60.0

    # =================================================
    # TIME
    # =================================================

    def update_time(self, delta):

        # 1 real second = small game-time movement

        self.game_time += delta * 0.02

        if self.game_time >= 24:

            self.game_time -= 24

    # =================================================
    # WEATHER
    # =================================================

    def update_weather(self):

        # Occasionally change weather

        if random.random() < 0.01:

            self.weather = random.choice(
                self.weather_options
            )

    # =================================================
    # NPC
    # =================================================

    def update_npcs(self):

        # Basic simulation layer

        if self.tick % 10 == 0:

            print(
                "NPC simulation:",
                self.npc_count,
                "NPCs active"
            )

    # =================================================
    # TRAFFIC
    # =================================================

    def update_traffic(self):

        if self.tick % 10 == 0:

            print(
                "Traffic simulation:",
                self.traffic_count,
                "vehicles active"
            )

    # =================================================
    # MISSION
    # =================================================

    def update_mission(self):

        if self.tick % 20 == 0:

            print(
                "Mission:",
                self.active_mission
            )

            print(
                "GPS distance:",
                round(
                    self.gps_distance,
                    2
                )
            )

    # =================================================
    # VEHICLE
    # =================================================

    def update_vehicle(self, delta):

        if not self.engine.in_vehicle:

            return

        speed = abs(
            self.engine.vehicle_speed
        )

        # Fuel consumption

        fuel_use = (
            speed *
            0.0008 *
            delta
        )

        self.fuel -= fuel_use

        self.fuel = max(
            0.0,
            self.fuel
        )

        # Fuel protection

        if self.fuel <= 0:

            self.engine.vehicle_speed = 0

            print(
                "VEHICLE OUT OF FUEL"
            )

    # =================================================
    # PLAYER HEALTH
    # =================================================

    def update_player(self):

        self.health = max(
            0.0,
            min(
                self.health,
                100.0
            )
        )

    # =================================================
    # AUTO SAVE
    # =================================================

    def update_save(self, delta):

        self.save_timer += delta

        if (
            self.save_timer
            >= self.auto_save_interval
        ):

            self.save_timer = 0

            print(
                "AUTO-SAVE CHECKPOINT"
            )

    # =================================================
    # WORLD TICK
    # =================================================

    def update(self, delta=1.0):

        self.tick += 1

        self.update_time(delta)

        self.update_weather()

        self.update_npcs()

        self.update_traffic()

        self.update_mission()

        self.update_vehicle(delta)

        self.update_player()

        self.update_save(delta)

    # =================================================
    # LIVE STATUS
    # =================================================

    def status(self):

        print()
        print(
            "========== SKADOSH LIVE WORLD =========="
        )

        print(
            "Tick:",
            self.tick
        )

        print(
            "Game time:",
            f"{self.game_time:05.2f}"
        )

        print(
            "Weather:",
            self.weather
        )

        print(
            "Position:",
            round(
                self.engine.x,
                2
            ),
            round(
                self.engine.y,
                2
            )
        )

        print(
            "Vehicle:",
            self.engine.in_vehicle
        )

        print(
            "Speed:",
            round(
                self.engine.vehicle_speed,
                2
            )
        )

        print(
            "Fuel:",
            round(
                self.fuel,
                2
            )
        )

        print(
            "Health:",
            round(
                self.health,
                2
            )
        )

        print(
            "NPCs:",
            self.npc_count
        )

        print(
            "Traffic:",
            self.traffic_count
        )

        print(
            "Mission:",
            self.active_mission
        )

        print(
            "========================================"
        )

    # =================================================
    # DEMO LOOP
    # =================================================

    def demo(self):

        print()
        print(
            "========================================"
        )
        print(
            "        SKADOSH LIVE WORLD ENGINE"
        )
        print(
            "========================================"
        )

        self.status()

        print()
        print("Starting world simulation...")

        # Enter vehicle

        self.engine.process_input({
            "enter_exit": True
        })

        # Simulate driving

        for _ in range(30):

            self.engine.process_input({
                "accelerate": True
            })

            self.update(1.0)

            if self.tick % 5 == 0:

                print(
                    "LIVE TICK",
                    self.tick,
                    "| Position:",
                    round(
                        self.engine.x,
                        2
                    ),
                    round(
                        self.engine.y,
                        2
                    ),
                    "| Speed:",
                    round(
                        self.engine.vehicle_speed,
                        2
                    )
                )

        self.status()

        print()
        print(
            "SKADOSH LIVE WORLD ENGINE OK"
        )


if __name__ == "__main__":

    world = LiveWorld()

    world.demo()
