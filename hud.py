class HUDSystem:

    def __init__(
        self,
        screen_width=1280,
        screen_height=720
    ):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.landscape = (
            screen_width >= screen_height
        )

        # -----------------------------
        # UI SAFE AREA
        # -----------------------------

        self.margin = 24

        # -----------------------------
        # PLAYER
        # -----------------------------

        self.health = 100
        self.max_health = 100

        self.money = 100000

        self.level = 1
        self.xp = 0

        # -----------------------------
        # VEHICLE
        # -----------------------------

        self.vehicle_active = False

        self.speed = 0
        self.max_speed = 80

        self.fuel = 100
        self.max_fuel = 100

        # -----------------------------
        # MISSION
        # -----------------------------

        self.mission_name = "Welcome to SKADOSH"

        self.mission_text = (
            "Explore the city"
        )

        self.gps_distance = 707.11

        # -----------------------------
        # WORLD
        # -----------------------------

        self.weather = "CLEAR"

        self.game_time = 12.0

        # -----------------------------
        # RADIO
        # -----------------------------

        self.radio_on = False

        self.radio_station = "SKADOSH FM"

        # -----------------------------
        # INTERACTION
        # -----------------------------

        self.interaction_text = ""

        # -----------------------------
        # MINIMAP
        # -----------------------------

        self.minimap_size = 190

    # =================================================
    # PLAYER
    # =================================================

    def set_player(
        self,
        health,
        money,
        level,
        xp
    ):

        self.health = max(
            0,
            min(
                health,
                self.max_health
            )
        )

        self.money = money

        self.level = level

        self.xp = xp

    # =================================================
    # VEHICLE
    # =================================================

    def set_vehicle(
        self,
        active,
        speed,
        fuel
    ):

        self.vehicle_active = active

        self.speed = max(
            0,
            speed
        )

        self.fuel = max(
            0,
            min(
                fuel,
                self.max_fuel
            )
        )

    # =================================================
    # MISSION
    # =================================================

    def set_mission(
        self,
        name,
        text,
        distance
    ):

        self.mission_name = name

        self.mission_text = text

        self.gps_distance = max(
            0,
            distance
        )

    # =================================================
    # WORLD
    # =================================================

    def set_world(
        self,
        weather,
        game_time
    ):

        self.weather = weather

        self.game_time = (
            game_time % 24
        )

    # =================================================
    # RADIO
    # =================================================

    def set_radio(
        self,
        active,
        station="SKADOSH FM"
    ):

        self.radio_on = active

        self.radio_station = station

    # =================================================
    # INTERACTION
    # =================================================

    def set_interaction(
        self,
        text
    ):

        self.interaction_text = text

    # =================================================
    # MINIMAP
    # =================================================

    def minimap(self):

        return {
            "size": self.minimap_size,

            "player": {
                "x": 0.5,
                "y": 0.5
            },

            "mission": {
                "visible": True,
                "distance": round(
                    self.gps_distance,
                    2
                )
            },

            "north": True
        }

    # =================================================
    # TOUCH HUD
    # =================================================

    def touch_controls(self):

        return {

            "joystick": {
                "x": 110,
                "y": self.screen_height - 120,
                "radius": 75
            },

            "accelerate": {
                "x": self.screen_width - 100,
                "y": self.screen_height - 110,
                "radius": 55
            },

            "brake": {
                "x": self.screen_width - 220,
                "y": self.screen_height - 90,
                "radius": 48
            },

            "handbrake": {
                "x": self.screen_width - 330,
                "y": self.screen_height - 90,
                "radius": 42
            },

            "interact": {
                "x": self.screen_width - 70,
                "y": 100,
                "radius": 38
            },

            "map": {
                "x": self.screen_width - 170,
                "y": 80,
                "radius": 35
            },

            "radio": {
                "x": self.screen_width - 260,
                "y": 80,
                "radius": 35
            },

            "pause": {
                "x": self.screen_width - 50,
                "y": 35,
                "radius": 25
            }
        }

    # =================================================
    # FULL HUD DATA
    # =================================================

    def build(self):

        return {

            "screen": {
                "width":
                    self.screen_width,

                "height":
                    self.screen_height,

                "landscape":
                    self.landscape
            },

            "player": {
                "health":
                    self.health,

                "max_health":
                    self.max_health,

                "money":
                    self.money,

                "level":
                    self.level,

                "xp":
                    self.xp
            },

            "mission": {
                "name":
                    self.mission_name,

                "text":
                    self.mission_text,

                "gps_distance":
                    round(
                        self.gps_distance,
                        2
                    )
            },

            "vehicle": {
                "active":
                    self.vehicle_active,

                "speed":
                    round(
                        self.speed,
                        2
                    ),

                "max_speed":
                    self.max_speed,

                "fuel":
                    round(
                        self.fuel,
                        2
                    )
            },

            "world": {
                "weather":
                    self.weather,

                "time":
                    round(
                        self.game_time,
                        2
                    )
            },

            "radio": {
                "active":
                    self.radio_on,

                "station":
                    self.radio_station
            },

            "interaction":
                self.interaction_text,

            "minimap":
                self.minimap(),

            "touch":
                self.touch_controls()
        }

    # =================================================
    # TEST
    # =================================================

def test():

    hud = HUDSystem(
        1280,
        720
    )

    print()
    print(
        "SKADOSH HUD SYSTEM"
    )
    print(
        "------------------"
    )

    hud.set_player(
        health=92,
        money=100000,
        level=3,
        xp=1450
    )

    hud.set_vehicle(
        active=True,
        speed=67,
        fuel=83
    )

    hud.set_mission(
        "Welcome to SKADOSH",
        "Drive to the city centre",
        1250
    )

    hud.set_world(
        "CLEAR",
        14.5
    )

    hud.set_radio(
        True,
        "SKADOSH FM"
    )

    hud.set_interaction(
        "Press E to interact"
    )

    data = hud.build()

    print()
    print(
        "Landscape:",
        data["screen"]["landscape"]
    )

    print(
        "Resolution:",
        data["screen"]["width"],
        "x",
        data["screen"]["height"]
    )

    print(
        "Health:",
        data["player"]["health"]
    )

    print(
        "Money:",
        data["player"]["money"]
    )

    print(
        "Level:",
        data["player"]["level"]
    )

    print(
        "Mission:",
        data["mission"]["name"]
    )

    print(
        "GPS:",
        data["mission"]["gps_distance"]
    )

    print(
        "Vehicle:",
        data["vehicle"]["active"]
    )

    print(
        "Speed:",
        data["vehicle"]["speed"]
    )

    print(
        "Fuel:",
        data["vehicle"]["fuel"]
    )

    print(
        "Weather:",
        data["world"]["weather"]
    )

    print(
        "Radio:",
        data["radio"]["station"]
    )

    print(
        "Touch controls:",
        len(data["touch"])
    )

    print()
    print(
        "SKADOSH HUD SYSTEM OK"
    )


if __name__ == "__main__":
    test()
