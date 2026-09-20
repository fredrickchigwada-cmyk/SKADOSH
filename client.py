import time

from game_session import SKADOSHSession
from renderer import WorldRenderer


class SKADOSHClient:

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    def __init__(self):

        self.session = SKADOSHSession()

        self.renderer = WorldRenderer(
            self.SCREEN_WIDTH,
            self.SCREEN_HEIGHT
        )

        self.screen = "MAIN_MENU"

        self.running = True

        self.selected_character = "Tyson"

        self.menu_items = [
            "PLAY",
            "WORLD",
            "CHARACTERS",
            "GARAGE",
            "BUSINESSES",
            "MISSIONS",
            "VIP CITY",
            "MULTIPLAYER",
            "SETTINGS"
        ]

        self.selected_menu = 0

        self.touch_buttons = {}

        self.create_touch_layout()

        self.create_world_objects()

    # =================================================
    # TOUCH LAYOUT
    # =================================================

    def create_touch_layout(self):

        w = self.SCREEN_WIDTH
        h = self.SCREEN_HEIGHT

        self.touch_buttons = {

            "JOYSTICK": {
                "x": 110,
                "y": h - 120,
                "radius": 75
            },

            "ACCELERATE": {
                "x": w - 100,
                "y": h - 110,
                "radius": 55
            },

            "BRAKE": {
                "x": w - 220,
                "y": h - 90,
                "radius": 48
            },

            "HANDBRAKE": {
                "x": w - 330,
                "y": h - 90,
                "radius": 42
            },

            "INTERACT": {
                "x": w - 70,
                "y": 100,
                "radius": 38
            },

            "MAP": {
                "x": w - 170,
                "y": 80,
                "radius": 35
            },

            "RADIO": {
                "x": w - 260,
                "y": 80,
                "radius": 35
            },

            "PAUSE": {
                "x": w - 50,
                "y": 35,
                "radius": 25
            }
        }

    # =================================================
    # WORLD OBJECTS
    # =================================================

    def create_world_objects(self):

        self.renderer.clear_objects()

        self.renderer.add_object(
            "player",
            "player",
            2500,
            2500
        )

        self.renderer.add_object(
            "vehicle_001",
            "vehicle",
            2550,
            2500
        )

        self.renderer.add_object(
            "mwashita_academy",
            "school",
            2700,
            2700
        )

        self.renderer.add_object(
            "shop_001",
            "shop",
            2300,
            2500
        )

        self.renderer.add_object(
            "garage_001",
            "garage",
            2200,
            2600
        )

        self.renderer.add_object(
            "restaurant_001",
            "restaurant",
            2800,
            2400
        )

        self.renderer.add_object(
            "hospital_001",
            "hospital",
            2900,
            2600
        )

        self.renderer.add_object(
            "mission_001",
            "mission",
            3000,
            3000
        )

    # =================================================
    # SCREEN TRANSITION
    # =================================================

    def change_screen(self, screen):

        valid_screens = [
            "MAIN_MENU",
            "WORLD",
            "CHARACTERS",
            "GARAGE",
            "BUSINESSES",
            "MISSIONS",
            "VIP_CITY",
            "MULTIPLAYER",
            "SETTINGS",
            "PAUSE"
        ]

        if screen not in valid_screens:

            return False

        self.screen = screen

        return True

    # =================================================
    # MENU
    # =================================================

    def select_menu(self, index):

        if index < 0:
            index = 0

        if index >= len(self.menu_items):
            index = len(self.menu_items) - 1

        self.selected_menu = index

    def activate_menu(self):

        item = self.menu_items[
            self.selected_menu
        ]

        mapping = {

            "PLAY":
                "WORLD",

            "WORLD":
                "WORLD",

            "CHARACTERS":
                "CHARACTERS",

            "GARAGE":
                "GARAGE",

            "BUSINESSES":
                "BUSINESSES",

            "MISSIONS":
                "MISSIONS",

            "VIP CITY":
                "VIP_CITY",

            "MULTIPLAYER":
                "MULTIPLAYER",

            "SETTINGS":
                "SETTINGS"
        }

        destination = mapping[item]

        self.change_screen(
            destination
        )

        return destination

    # =================================================
    # PLAY
    # =================================================

    def start_game(self):

        self.change_screen(
            "WORLD"
        )

        return True

    # =================================================
    # PAUSE
    # =================================================

    def pause(self):

        self.change_screen(
            "PAUSE"
        )

    def resume(self):

        self.change_screen(
            "WORLD"
        )

    # =================================================
    # UPDATE
    # =================================================

    def update(self, delta):

        if self.screen == "WORLD":

            self.session.update(
                delta
            )

            # Update player render object

            player_obj = None

            for obj in self.renderer.objects:

                if obj.object_id == "player":

                    player_obj = obj

                    break

            if player_obj is not None:

                player_obj.x = (
                    self.session.game.world.engine.x
                )

                player_obj.y = (
                    self.session.game.world.engine.y
                )

            self.renderer.set_weather(
                self.session.game.world.weather
            )

            self.renderer.set_time(
                self.session.game.world.game_time
            )

    # =================================================
    # INPUT
    # =================================================

    def input(self, command):

        if command == "PLAY":

            self.start_game()

            return

        if command == "PAUSE":

            if self.screen == "WORLD":

                self.pause()

            elif self.screen == "PAUSE":

                self.resume()

            return

        if self.screen != "WORLD":

            return

        commands = {

            "ACCELERATE":
                {"accelerate": True},

            "BRAKE":
                {"brake": True},

            "LEFT":
                {"steer_left": True},

            "RIGHT":
                {"steer_right": True},

            "HANDBRAKE":
                {"handbrake": True},

            "ENTER":
                {"enter_exit": True},

            "HORN":
                {"horn": True},

            "RADIO":
                {"radio": True},

            "MAP":
                {"map": True},

            "INTERACT":
                {"interact": True}
        }

        if command in commands:

            self.session.input(
                commands[command]
            )

    # =================================================
    # FRAME
    # =================================================

    def frame(self):

        if self.screen == "WORLD":

            data = self.session.frame()

            player = self.session.game.world.engine

            render_frame = self.renderer.frame(
                player
            )

            return {
                "screen": self.screen,
                "render": render_frame,
                "hud": data
            }

        return {
            "screen": self.screen,
            "menu": self.menu_items,
            "selected": self.selected_menu,
            "character": self.selected_character,
            "touch": self.touch_buttons
        }


# =====================================================
# TEST
# =====================================================

def test():

    print()
    print(
        "======================================"
    )
    print(
        "       SKADOSH VISUAL CLIENT"
    )
    print(
        "======================================"
    )

    client = SKADOSHClient()

    print()
    print(
        "Resolution:",
        client.SCREEN_WIDTH,
        "x",
        client.SCREEN_HEIGHT
    )

    print(
        "Landscape:",
        client.SCREEN_WIDTH
        >=
        client.SCREEN_HEIGHT
    )

    print()
    print(
        "MAIN MENU"
    )

    for item in client.menu_items:

        print(
            "-",
            item
        )

    # Start game

    print()
    print(
        "Starting game..."
    )

    client.input(
        "PLAY"
    )

    # Enter vehicle

    client.input(
        "ENTER"
    )

    # Drive

    for _ in range(10):

        client.input(
            "ACCELERATE"
        )

        client.update(
            1.0 / 30.0
        )

    # Turn

    for _ in range(5):

        client.input(
            "RIGHT"
        )

        client.update(
            1.0 / 30.0
        )

    # Radio

    client.input(
        "RADIO"
    )

    client.update(
        1.0 / 30.0
    )

    frame = client.frame()

    print()
    print(
        "CURRENT SCREEN:",
        frame["screen"]
    )

    print(
        "PLAYER POSITION:",
        round(
            client.session.game.world.engine.x,
            2
        ),
        round(
            client.session.game.world.engine.y,
            2
        )
    )

    print(
        "VEHICLE:",
        frame["hud"]["vehicle"]["active"]
    )

    print(
        "SPEED:",
        frame["hud"]["vehicle"]["speed"]
    )

    print(
        "RADIO:",
        frame["hud"]["radio"]["active"]
    )

    print(
        "VISIBLE OBJECTS:",
        len(
            frame["render"]["objects"]
        )
    )

    print()
    print(
        "SKADOSH VISUAL CLIENT OK"
    )


if __name__ == "__main__":

    test()
