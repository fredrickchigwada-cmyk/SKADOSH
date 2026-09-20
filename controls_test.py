from controls import ControlManager


def main():

    print("SKADOSH CONTROL SYSTEM TEST")
    print("===========================")

    controls = ControlManager()

    # -------------------------
    # KEYBOARD TEST
    # -------------------------

    print()
    print("Testing keyboard...")

    controls.use_keyboard()

    controls.keyboard.key_down("W")

    state = controls.get_state()

    print(
        "Throttle:",
        state.throttle
    )

    controls.keyboard.key_down("D")

    print(
        "Steering:",
        state.steering
    )

    controls.keyboard.key_down("SPACE")

    print(
        "Handbrake:",
        state.handbrake
    )

    controls.keyboard.key_up("W")
    controls.keyboard.key_up("D")
    controls.keyboard.key_up("SPACE")

    # -------------------------
    # TOUCH TEST
    # -------------------------

    print()
    print("Testing touch controls...")

    controls.use_touch()

    controls.touch.joystick(
        0.75,
        -0.80
    )

    state = controls.get_state()

    print(
        "Joystick X:",
        state.joystick_x
    )

    print(
        "Joystick Y:",
        state.joystick_y
    )

    print(
        "Touch throttle:",
        round(state.throttle, 2)
    )

    print(
        "Touch steering:",
        round(state.steering, 2)
    )

    controls.touch.button_down(
        "HORN"
    )

    print(
        "Horn:",
        state.horn
    )

    controls.touch.button_down(
        "MAP"
    )

    print(
        "Map:",
        state.map
    )

    print()
    print("CONTROL SYSTEM OK")


if __name__ == "__main__":
    main()
