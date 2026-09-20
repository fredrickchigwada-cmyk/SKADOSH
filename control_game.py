from controls import ControlManager
from skadosh_game import SKADOSHGame
from movement import MovementSystem


class ControlDrivenGame:

    def __init__(self):

        self.game = SKADOSHGame()
        self.controls = ControlManager()

        self.movement = MovementSystem(
            world_width=5000,
            world_height=5000
        )

        self.running = True
        self.paused = False

        self.in_vehicle = False
        self.radio_on = False
        self.map_open = False

        self.vehicle_speed = 0.0

        # Try to locate player from the existing engine
        self.player = getattr(
            self.game,
            "player",
            None
        )

        # Fallback to world player
        if self.player is None:

            world = getattr(
                self.game,
                "world",
                None
            )

            if world is not None:

                self.player = getattr(
                    world,
                    "player",
                    None
                )

        # Starting coordinates
        self.x = 2500.0
        self.y = 2500.0

        if self.player is not None:

            if hasattr(self.player, "x"):
                self.x = self.player.x

            if hasattr(self.player, "y"):
                self.y = self.player.y

    # --------------------------------------------------
    # POSITION
    # --------------------------------------------------

    def sync_player_position(self):

        if self.player is not None:

            if hasattr(self.player, "x"):
                self.player.x = self.x

            if hasattr(self.player, "y"):
                self.player.y = self.y

    # --------------------------------------------------
    # INPUT
    # --------------------------------------------------

    def process_input(self, commands):

        if commands.get("pause"):

            self.paused = not self.paused

            print(
                "PAUSED"
                if self.paused
                else
                "RESUMED"
            )

            return

        if self.paused:
            return

        # ------------------------------------------------
        # ENTER / EXIT
        # ------------------------------------------------

        if commands.get("enter_exit"):

            self.in_vehicle = not self.in_vehicle

            if self.in_vehicle:

                print("ENTERED VEHICLE")

            else:

                self.vehicle_speed = 0.0

                print("EXITED VEHICLE")

        # ------------------------------------------------
        # RADIO
        # ------------------------------------------------

        if commands.get("radio"):

            self.radio_on = not self.radio_on

            print(
                "RADIO:",
                "ON"
                if self.radio_on
                else
                "OFF"
            )

        # ------------------------------------------------
        # MAP
        # ------------------------------------------------

        if commands.get("map"):

            self.map_open = not self.map_open

            print(
                "MAP:",
                "OPEN"
                if self.map_open
                else
                "CLOSED"
            )

        # ------------------------------------------------
        # HORN
        # ------------------------------------------------

        if commands.get("horn"):

            if self.in_vehicle:

                print("HORN: BEEP BEEP")

            else:

                print(
                    "You need to be inside a vehicle."
                )

        # ------------------------------------------------
        # INTERACTION
        # ------------------------------------------------

        if commands.get("interact"):

            print(
                "INTERACTION REQUESTED"
            )

        # ------------------------------------------------
        # MOVEMENT
        # ------------------------------------------------

        if self.in_vehicle:

            self.update_vehicle(
                commands
            )

        else:

            self.update_on_foot(
                commands
            )

    # --------------------------------------------------
    # ON FOOT
    # --------------------------------------------------

    def update_on_foot(self, commands):

        self.x, self.y = self.movement.move_on_foot(
            self.x,
            self.y,
            commands
        )

        self.sync_player_position()

    # --------------------------------------------------
    # VEHICLE
    # --------------------------------------------------

    def update_vehicle(self, commands):

        self.x, self.y, self.vehicle_speed = (
            self.movement.update_vehicle(
                self.x,
                self.y,
                self.vehicle_speed,
                commands
            )
        )

        self.sync_player_position()

    # --------------------------------------------------
    # STATUS
    # --------------------------------------------------

    def status(self):

        print()
        print(
            "===== SKADOSH GAME STATUS ====="
        )

        print(
            "Position:",
            round(self.x, 2),
            round(self.y, 2)
        )

        print(
            "Vehicle:",
            self.in_vehicle
        )

        print(
            "Vehicle speed:",
            round(
                self.vehicle_speed,
                2
            )
        )

        print(
            "Radio:",
            self.radio_on
        )

        print(
            "Map:",
            self.map_open
        )

        print(
            "Paused:",
            self.paused
        )

        print(
            "Distance travelled:",
            round(
                self.movement.distance_travelled,
                2
            )
        )

        print(
            "World:",
            self.movement.world_width,
            "x",
            self.movement.world_height
        )

        print(
            "=============================="
        )


# ======================================================
# TEST
# ======================================================

def test():

    engine = ControlDrivenGame()

    print()
    print(
        "SKADOSH CONTROL + MOVEMENT ENGINE"
    )
    print(
        "----------------------------------"
    )

    engine.status()

    # -----------------------------------------------
    # WALK
    # -----------------------------------------------

    print()
    print("Walking forward...")

    for _ in range(5):

        engine.process_input({
            "accelerate": True
        })

    engine.status()

    # -----------------------------------------------
    # ENTER VEHICLE
    # -----------------------------------------------

    print()
    print("Entering vehicle...")

    engine.process_input({
        "enter_exit": True
    })

    # -----------------------------------------------
    # ACCELERATE
    # -----------------------------------------------

    print()
    print("Accelerating vehicle...")

    for _ in range(10):

        engine.process_input({
            "accelerate": True
        })

    engine.status()

    # -----------------------------------------------
    # TURN
    # -----------------------------------------------

    print()
    print("Turning right...")

    for _ in range(5):

        engine.process_input({
            "accelerate": True,
            "steer_right": True
        })

    engine.status()

    # -----------------------------------------------
    # BRAKE
    # -----------------------------------------------

    print()
    print("Braking...")

    for _ in range(3):

        engine.process_input({
            "brake": True
        })

    engine.status()

    # -----------------------------------------------
    # HANDBRAKE
    # -----------------------------------------------

    print()
    print("Handbrake...")

    engine.process_input({
        "handbrake": True
    })

    # -----------------------------------------------
    # HORN
    # -----------------------------------------------

    print()
    print("Horn...")

    engine.process_input({
        "horn": True
    })

    # -----------------------------------------------
    # RADIO
    # -----------------------------------------------

    print()
    print("Radio...")

    engine.process_input({
        "radio": True
    })

    # -----------------------------------------------
    # MAP
    # -----------------------------------------------

    print()
    print("Map...")

    engine.process_input({
        "map": True
    })

    engine.status()

    print()
    print(
        "SKADOSH CONTROL + MOVEMENT OK"
    )


if __name__ == "__main__":
    test()
