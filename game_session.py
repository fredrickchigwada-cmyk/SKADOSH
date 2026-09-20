import time

from game_state import SKADOSHGameState


class SKADOSHSession:

    def __init__(self):

        self.game = SKADOSHGameState()

        self.running = True

        self.frame_count = 0

        self.total_time = 0.0

        self.fixed_delta = 1.0 / 30.0

        self.fps_target = 30

    # =================================================
    # INPUT
    # =================================================

    def input(self, commands):

        if not self.running:
            return

        self.game.world.engine.process_input(
            commands
        )

    # =================================================
    # UPDATE
    # =================================================

    def update(self, delta):

        if not self.running:
            return

        self.game.update(delta)

        self.total_time += delta

        self.frame_count += 1

    # =================================================
    # FRAME
    # =================================================

    def frame(self):

        return self.game.frame()

    # =================================================
    # SHUTDOWN
    # =================================================

    def stop(self):

        self.running = False

        print(
            "SKADOSH SESSION STOPPED"
        )

    # =================================================
    # STATUS
    # =================================================

    def status(self):

        data = self.frame()

        print()
        print(
            "======================================"
        )
        print(
            "       SKADOSH ACTIVE SESSION"
        )
        print(
            "======================================"
        )

        print(
            "Frame:",
            self.frame_count
        )

        print(
            "Session time:",
            round(
                self.total_time,
                2
            )
        )

        print(
            "Position:",
            round(
                self.game.world.engine.x,
                2
            ),
            round(
                self.game.world.engine.y,
                2
            )
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
            "Health:",
            data["player"]["health"]
        )

        print(
            "Money:",
            data["player"]["money"]
        )

        print(
            "Mission:",
            data["mission"]["name"]
        )

        print(
            "Weather:",
            data["world"]["weather"]
        )

        print(
            "Radio:",
            data["radio"]["active"]
        )

        print(
            "Map:",
            self.game.world.engine.map_open
        )

        print(
            "======================================"
        )


# =====================================================
# TEST SESSION
# =====================================================

def test():

    print()
    print(
        "======================================"
    )
    print(
        "      SKADOSH GAME SESSION"
    )
    print(
        "======================================"
    )

    session = SKADOSHSession()

    # -----------------------------------------------
    # INITIAL FRAME
    # -----------------------------------------------

    print()
    print(
        "Initialising player..."
    )

    session.update(
        session.fixed_delta
    )

    # -----------------------------------------------
    # ENTER VEHICLE
    # -----------------------------------------------

    print()
    print(
        "Entering vehicle..."
    )

    session.input({
        "enter_exit": True
    })

    session.update(
        session.fixed_delta
    )

    # -----------------------------------------------
    # DRIVE
    # -----------------------------------------------

    print()
    print(
        "Driving..."
    )

    for _ in range(30):

        session.input({
            "accelerate": True
        })

        session.update(
            session.fixed_delta
        )

    # -----------------------------------------------
    # TURN
    # -----------------------------------------------

    print()
    print(
        "Turning..."
    )

    for _ in range(10):

        session.input({
            "accelerate": True,
            "steer_right": True
        })

        session.update(
            session.fixed_delta
        )

    # -----------------------------------------------
    # BRAKE
    # -----------------------------------------------

    print()
    print(
        "Braking..."
    )

    for _ in range(5):

        session.input({
            "brake": True
        })

        session.update(
            session.fixed_delta
        )

    # -----------------------------------------------
    # HORN
    # -----------------------------------------------

    session.input({
        "horn": True
    })

    session.update(
        session.fixed_delta
    )

    # -----------------------------------------------
    # RADIO
    # -----------------------------------------------

    session.input({
        "radio": True
    })

    session.update(
        session.fixed_delta
    )

    # -----------------------------------------------
    # MAP
    # -----------------------------------------------

    session.input({
        "map": True
    })

    session.update(
        session.fixed_delta
    )

    # -----------------------------------------------
    # FINAL STATUS
    # -----------------------------------------------

    session.status()

    print()
    print(
        "Frames simulated:",
        session.frame_count
    )

    print(
        "Session time:",
        round(
            session.total_time,
            2
        ),
        "seconds"
    )

    print()
    print(
        "SKADOSH COMPLETE GAME SESSION OK"
    )


if __name__ == "__main__":

    test()
