import math


class Camera:
    def __init__(
        self,
        screen_width=1280,
        screen_height=720
    ):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.x = 2500.0
        self.y = 2500.0

        self.zoom = 1.0

    def follow(self, x, y):
        self.x = x
        self.y = y

    def world_to_screen(self, world_x, world_y):

        screen_x = (
            world_x - self.x
        ) * self.zoom + (
            self.screen_width / 2
        )

        screen_y = (
            world_y - self.y
        ) * self.zoom + (
            self.screen_height / 2
        )

        return screen_x, screen_y


class RendererObject:

    def __init__(
        self,
        object_id,
        object_type,
        x,
        y,
        rotation=0.0
    ):
        self.object_id = object_id
        self.object_type = object_type

        self.x = x
        self.y = y

        self.rotation = rotation


class WorldRenderer:

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

        self.camera = Camera(
            screen_width,
            screen_height
        )

        self.objects = []

        self.weather = "CLEAR"

        self.game_time = 12.0

        self.daylight = 1.0

    # =================================================
    # OBJECT MANAGEMENT
    # =================================================

    def add_object(
        self,
        object_id,
        object_type,
        x,
        y,
        rotation=0.0
    ):

        obj = RendererObject(
            object_id,
            object_type,
            x,
            y,
            rotation
        )

        self.objects.append(obj)

        return obj

    def clear_objects(self):

        self.objects.clear()

    # =================================================
    # CAMERA
    # =================================================

    def update_camera(
        self,
        player_x,
        player_y
    ):

        self.camera.follow(
            player_x,
            player_y
        )

    # =================================================
    # WEATHER
    # =================================================

    def set_weather(
        self,
        weather
    ):

        self.weather = weather

    # =================================================
    # DAY / NIGHT
    # =================================================

    def set_time(
        self,
        game_time
    ):

        self.game_time = game_time % 24.0

        # Approximate daylight cycle

        angle = (
            (self.game_time - 6.0)
            / 12.0
        ) * math.pi

        self.daylight = max(
            0.15,
            math.sin(angle)
        )

    # =================================================
    # WORLD → SCREEN
    # =================================================

    def visible_objects(self):

        visible = []

        for obj in self.objects:

            sx, sy = (
                self.camera.world_to_screen(
                    obj.x,
                    obj.y
                )
            )

            # Basic screen visibility

            if (
                -100 <= sx <=
                self.screen_width + 100
                and
                -100 <= sy <=
                self.screen_height + 100
            ):

                visible.append({
                    "id": obj.object_id,
                    "type": obj.object_type,
                    "screen_x": round(sx, 2),
                    "screen_y": round(sy, 2),
                    "rotation": obj.rotation
                })

        return visible

    # =================================================
    # HUD DATA
    # =================================================

    def hud(self, player):

        return {
            "money": getattr(
                player,
                "money",
                100000
            ),

            "health": getattr(
                player,
                "health",
                100
            ),

            "character": getattr(
                player,
                "character",
                "Tyson"
            ),

            "screen_width":
                self.screen_width,

            "screen_height":
                self.screen_height,

            "landscape":
                self.landscape,

            "weather":
                self.weather,

            "time":
                round(
                    self.game_time,
                    2
                ),

            "daylight":
                round(
                    self.daylight,
                    2
                )
        }

    # =================================================
    # FRAME DATA
    # =================================================

    def frame(self, player):

        px = getattr(
            player,
            "x",
            self.camera.x
        )

        py = getattr(
            player,
            "y",
            self.camera.y
        )

        self.update_camera(
            px,
            py
        )

        return {
            "camera": {
                "x": round(
                    self.camera.x,
                    2
                ),
                "y": round(
                    self.camera.y,
                    2
                ),
                "zoom": self.camera.zoom
            },

            "objects":
                self.visible_objects(),

            "hud":
                self.hud(player)
        }


# =====================================================
# TEST
# =====================================================

class TestPlayer:

    def __init__(self):

        self.x = 2500.0
        self.y = 2500.0

        self.money = 100000

        self.health = 100

        self.character = "Tyson"


def test():

    print()
    print(
        "SKADOSH RENDERER ARCHITECTURE"
    )
    print(
        "-----------------------------"
    )

    renderer = WorldRenderer(
        1280,
        720
    )

    player = TestPlayer()

    print(
        "Resolution:",
        renderer.screen_width,
        "x",
        renderer.screen_height
    )

    print(
        "Landscape:",
        renderer.landscape
    )

    # Player

    renderer.add_object(
        "player",
        "player",
        2500,
        2500
    )

    # Vehicle

    renderer.add_object(
        "vehicle_001",
        "vehicle",
        2550,
        2500
    )

    # NPCs

    renderer.add_object(
        "npc_001",
        "npc",
        2450,
        2480
    )

    renderer.add_object(
        "npc_002",
        "npc",
        2600,
        2550
    )

    # School

    renderer.add_object(
        "mwashita_academy",
        "school",
        2700,
        2700
    )

    # Shop

    renderer.add_object(
        "shop_001",
        "shop",
        2300,
        2500
    )

    # Mission

    renderer.add_object(
        "mission_001",
        "mission",
        3000,
        3000
    )

    renderer.set_weather(
        "CLEAR"
    )

    renderer.set_time(
        14.0
    )

    frame = renderer.frame(
        player
    )

    print()
    print(
        "Camera:",
        frame["camera"]
    )

    print(
        "Visible objects:",
        len(frame["objects"])
    )

    for obj in frame["objects"]:

        print(
            obj["type"],
            "->",
            obj["screen_x"],
            obj["screen_y"]
        )

    print()
    print(
        "HUD:",
        frame["hud"]
    )

    print()
    print(
        "RENDERER ARCHITECTURE OK"
    )


if __name__ == "__main__":
    test()
