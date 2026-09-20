from live_world import LiveWorld
from hud import HUDSystem


class SKADOSHGameState:

    def __init__(self):

        self.world = LiveWorld()

        self.hud = HUDSystem(
            1280,
            720
        )

        self.running = True

    # ==============================================
    # PLAYER
    # ==============================================

    def update_player_hud(self):

        profile = getattr(
            self.world.engine.game,
            "player",
            None
        )

        money = 100000
        level = 1
        xp = 0

        if profile is not None:

            money = getattr(
                profile,
                "money",
                money
            )

            level = getattr(
                profile,
                "level",
                level
            )

            xp = getattr(
                profile,
                "xp",
                xp
            )

        self.hud.set_player(
            health=self.world.health,
            money=money,
            level=level,
            xp=xp
        )

    # ==============================================
    # VEHICLE
    # ==============================================

    def update_vehicle_hud(self):

        self.hud.set_vehicle(
            active=self.world.engine.in_vehicle,
            speed=abs(
                self.world.engine.vehicle_speed
            ),
            fuel=self.world.fuel
        )

    # ==============================================
    # MISSION
    # ==============================================

    def update_mission_hud(self):

        self.hud.set_mission(
            self.world.active_mission,
            "Follow the GPS to your destination",
            self.world.gps_distance
        )

    # ==============================================
    # WORLD
    # ==============================================

    def update_world_hud(self):

        self.hud.set_world(
            self.world.weather,
            self.world.game_time
        )

    # ==============================================
    # RADIO
    # ==============================================

    def update_radio_hud(self):

        self.hud.set_radio(
            self.world.engine.radio_on,
            "SKADOSH FM"
        )

    # ==============================================
    # INTERACTION
    # ==============================================

    def update_interaction_hud(self):

        if self.world.engine.map_open:

            self.hud.set_interaction(
                "MAP OPEN"
            )

        else:

            self.hud.set_interaction(
                ""
            )

    # ==============================================
    # UPDATE HUD
    # ==============================================

    def update_hud(self):

        self.update_player_hud()

        self.update_vehicle_hud()

        self.update_mission_hud()

        self.update_world_hud()

        self.update_radio_hud()

        self.update_interaction_hud()

    # ==============================================
    # UPDATE GAME
    # ==============================================

    def update(self, delta=1.0):

        self.world.update(delta)

        self.update_hud()

    # ==============================================
    # FRAME
    # ==============================================

    def frame(self):

        return self.hud.build()


def test():

    print()
    print(
        "SKADOSH GAME STATE"
    )
    print(
        "------------------"
    )

    game = SKADOSHGameState()

    # Enter vehicle
    game.world.engine.process_input({
        "enter_exit": True
    })

    # Drive
    for _ in range(5):

        game.world.engine.process_input({
            "accelerate": True
        })

        game.update(1.0)

    # Radio
    game.world.engine.process_input({
        "radio": True
    })

    game.update(1.0)

    # Map
    game.world.engine.process_input({
        "map": True
    })

    game.update(1.0)

    data = game.frame()

    print()
    print(
        "PLAYER"
    )

    print(
        "Money:",
        data["player"]["money"]
    )

    print(
        "Health:",
        data["player"]["health"]
    )

    print(
        "Level:",
        data["player"]["level"]
    )

    print()
    print(
        "VEHICLE"
    )

    print(
        "Active:",
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

    print()
    print(
        "WORLD"
    )

    print(
        "Weather:",
        data["world"]["weather"]
    )

    print(
        "Time:",
        data["world"]["time"]
    )

    print()
    print(
        "MISSION"
    )

    print(
        "Name:",
        data["mission"]["name"]
    )

    print(
        "GPS:",
        data["mission"]["gps_distance"]
    )

    print()
    print(
        "RADIO"
    )

    print(
        "Active:",
        data["radio"]["active"]
    )

    print(
        "Station:",
        data["radio"]["station"]
    )

    print()
    print(
        "TOUCH HUD"
    )

    print(
        "Controls:",
        len(data["touch"])
    )

    print()
    print(
        "SKADOSH GAME STATE OK"
    )


if __name__ == "__main__":
    test()
