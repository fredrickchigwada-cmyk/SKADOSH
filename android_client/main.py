from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

import os
import sys

# Allow Android client to access the SKADOSH engine
PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

try:
    from client import SKADOSHClient
except Exception:
    SKADOSHClient = None


class WorldBackground(Widget):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        with self.canvas:

            Color(
                0.015,
                0.02,
                0.04,
                1
            )

            self.background = Rectangle(
                pos=self.pos,
                size=self.size
            )

            Color(
                0.08,
                0.12,
                0.18,
                1
            )

            self.city = Rectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.update_graphics,
            size=self.update_graphics
        )

    def update_graphics(self, *args):

        self.background.pos = self.pos
        self.background.size = self.size

        self.city.pos = (
            self.x,
            self.y + self.height * 0.18
        )

        self.city.size = (
            self.width,
            self.height * 0.82
        )


class SKADOSHAndroidClient(FloatLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.game = None

        if SKADOSHClient is not None:

            try:
                self.game = SKADOSHClient()
            except Exception as error:

                print(
                    "Engine connection:",
                    error
                )

        self.current_screen = "MAIN_MENU"

        self.build_main_menu()

    # ================================================
    # BACKGROUND
    # ================================================

    def add_background(self):

        self.background = WorldBackground()

        self.add_widget(
            self.background
        )

    # ================================================
    # MAIN MENU
    # ================================================

    def build_main_menu(self):

        self.clear_widgets()

        self.add_background()

        title = Label(
            text="SKADOSH",
            font_size="54sp",
            bold=True,
            size_hint=(1, None),
            height=90,
            pos_hint={
                "center_x": 0.5,
                "top": 0.90
            }
        )

        self.add_widget(title)

        tagline = Label(
            text="BORN IN ZIMBABWE. BUILT FOR THE WORLD.",
            font_size="16sp",
            size_hint=(1, None),
            height=40,
            pos_hint={
                "center_x": 0.5,
                "top": 0.80
            }
        )

        self.add_widget(tagline)

        buttons = [
            ("PLAY", self.start_game),
            ("CHARACTERS", self.characters),
            ("GARAGE", self.garage),
            ("MISSIONS", self.missions),
            ("VIP CITY", self.vip_city),
            ("MULTIPLAYER", self.multiplayer),
            ("SETTINGS", self.settings)
        ]

        start_y = 0.62

        for index, (text, action) in enumerate(buttons):

            button = Button(
                text=text,
                font_size="18sp",
                size_hint=(None, None),
                size=(250, 52),
                pos_hint={
                    "center_x": 0.5,
                    "top": start_y - index * 0.075
                }
            )

            button.bind(
                on_press=action
            )

            self.add_widget(
                button
            )

    # ================================================
    # WORLD
    # ================================================

    def start_game(self, *args):

        self.current_screen = "WORLD"

        if self.game:

            try:
                self.game.start_game()
            except Exception as error:

                print(
                    "Game start:",
                    error
                )

        self.build_world()

    def build_world(self):

        self.clear_widgets()

        self.add_background()

        title = Label(
            text="SKADOSH WORLD",
            font_size="28sp",
            bold=True,
            size_hint=(1, None),
            height=60,
            pos_hint={
                "center_x": 0.5,
                "top": 0.96
            }
        )

        self.add_widget(title)

        money = Label(
            text="$100,000",
            font_size="20sp",
            size_hint=(None, None),
            size=(180, 50),
            pos_hint={
                "x": 0.02,
                "top": 0.96
            }
        )

        self.money_label = money

        self.add_widget(
            money
        )

        # Mission

        mission = Label(
            text="MISSION: Welcome to SKADOSH",
            font_size="17sp",
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={
                "x": 0.02,
                "top": 0.88
            }
        )

        self.mission_label = mission

        self.add_widget(
            mission
        )

        # Minimap

        minimap = Widget(
            size_hint=(None, None),
            size=(170, 170),
            pos_hint={
                "right": 0.98,
                "top": 0.95
            }
        )

        with minimap.canvas:

            Color(
                0.02,
                0.02,
                0.02,
                0.85
            )

            RoundedRectangle(
                pos=minimap.pos,
                size=minimap.size,
                radius=[20]
            )

        self.add_widget(
            minimap
        )

        # Controls

        self.add_world_controls()

        Clock.schedule_interval(
            self.update_game,
            1 / 30
        )

    # ================================================
    # TOUCH CONTROLS
    # ================================================

    def add_world_controls(self):

        controls = [

            ("◀", "LEFT", 0.08, 0.12),

            ("▶", "RIGHT", 0.23, 0.12),

            ("▲", "ACCELERATE", 0.88, 0.22),

            ("▼", "BRAKE", 0.88, 0.10),

            ("F", "ENTER", 0.76, 0.12),

            ("H", "HORN", 0.66, 0.12),

            ("R", "RADIO", 0.56, 0.12),

            ("M", "MAP", 0.46, 0.12),

            ("Ⅱ", "PAUSE", 0.95, 0.93)
        ]

        for text, command, x, y in controls:

            button = Button(
                text=text,
                font_size="18sp",
                size_hint=(None, None),
                size=(58, 58),
                pos_hint={
                    "x": x,
                    "y": y
                }
            )

            button.bind(
                on_press=lambda instance,
                command=command:
                self.send_command(command)
            )

            self.add_widget(
                button
            )

    # ================================================
    # ENGINE COMMAND
    # ================================================

    def send_command(self, command):

        if self.game is None:
            return

        try:

            self.game.input(
                command
            )

        except Exception as error:

            print(
                "Command:",
                error
            )

    # ================================================
    # GAME UPDATE
    # ================================================

    def update_game(self, delta):

        if self.current_screen != "WORLD":
            return

        if self.game is None:
            return

        try:

            self.game.update(
                delta
            )

            frame = self.game.frame()

            hud = frame.get(
                "hud",
                {}
            )

            player = hud.get(
                "player",
                {}
            )

            if "money" in player:

                self.money_label.text = (
                    "$"
                    + str(
                        player["money"]
                    )
                )

        except Exception as error:

            print(
                "Update:",
                error
            )

    # ================================================
    # OTHER MENUS
    # ================================================

    def characters(self, *args):

        self.simple_screen(
            "CHARACTERS",
            "10 PLAYABLE CHARACTERS\n\n"
            "TYSON\n"
            "HUMOROUS JACK\n"
            "ORACLE\n"
            "BARBAROUS BULL\n"
            "DAVEN\n"
            "NOVA\n"
            "ZURI\n"
            "AMARA\n"
            "NYX\n"
            "KIRA"
        )

    def garage(self, *args):

        self.simple_screen(
            "GARAGE",
            "VEHICLES\n\n"
            "SPORTS CAR\n"
            "SUPERCAR\n"
            "SUV\n"
            "SEDAN\n"
            "TAXI\n"
            "BUS\n"
            "TRUCK\n"
            "LUXURY\n"
            "OFF-ROAD\n"
            "MOTORBIKE\n"
            "HOVER VEHICLE"
        )

    def missions(self, *args):

        self.simple_screen(
            "MISSIONS",
            "MISSION HUB\n\n"
            "DELIVERY\n"
            "RACING\n"
            "ESCORT\n"
            "EXPLORATION\n"
            "RESCUE\n"
            "VIP\n"
            "TREASURE\n"
            "SURVIVAL"
        )

    def vip_city(self, *args):

        self.simple_screen(
            "VIP CITY",
            "VIP CITY\n\n"
            "LUXURY EVENTS\n"
            "BUSINESS MISSIONS\n"
            "CHARITY EVENTS\n"
            "VIP CONTRACTS\n"
            "CONVOY EVENTS"
        )

    def multiplayer(self, *args):

        self.simple_screen(
            "MULTIPLAYER",
            "SKADOSH MULTIPLAYER\n\n"
            "LOCAL WI-FI\n"
            "HOTSPOT\n"
            "ONLINE SERVER\n"
            "TEAM CHAT\n"
            "VOICE SYSTEM"
        )

    def settings(self, *args):

        self.simple_screen(
            "SETTINGS",
            "GRAPHICS\n"
            "AUDIO\n"
            "CONTROLS\n"
            "GAMEPLAY\n"
            "LANGUAGE\n"
            "MINIMAP\n"
            "VIBRATION"
        )

    # ================================================
    # GENERIC SCREEN
    # ================================================

    def simple_screen(self, title_text, body):

        self.clear_widgets()

        self.add_background()

        title = Label(
            text=title_text,
            font_size="34sp",
            bold=True,
            size_hint=(1, None),
            height=70,
            pos_hint={
                "center_x": 0.5,
                "top": 0.90
            }
        )

        self.add_widget(
            title
        )

        content = Label(
            text=body,
            font_size="18sp",
            halign="center",
            valign="middle",
            size_hint=(0.8, 0.55),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.48
            }
        )

        self.add_widget(
            content
        )

        back = Button(
            text="BACK",
            size_hint=(None, None),
            size=(180, 55),
            pos_hint={
                "center_x": 0.5,
                "y": 0.05
            }
        )

        back.bind(
            on_press=lambda x:
            self.build_main_menu()
        )

        self.add_widget(
            back
        )


class SKADOSHApp(App):

    def build(self):

        self.title = "SKADOSH"

        # Landscape target
        try:

            Window.size = (
                1280,
                720
            )

        except Exception:
            pass

        return SKADOSHAndroidClient()


if __name__ == "__main__":

    SKADOSHApp().run()
