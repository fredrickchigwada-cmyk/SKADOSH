from dataclasses import dataclass


@dataclass
class InputState:

    accelerate: bool = False
    brake: bool = False

    steer_left: bool = False
    steer_right: bool = False

    handbrake: bool = False

    enter_exit: bool = False
    horn: bool = False
    radio: bool = False
    map: bool = False
    interact: bool = False
    pause: bool = False

    joystick_x: float = 0.0
    joystick_y: float = 0.0

    def reset_actions(self):

        self.enter_exit = False
        self.horn = False
        self.radio = False
        self.map = False
        self.interact = False
        self.pause = False

    @property
    def throttle(self):

        if self.accelerate:
            return 1.0

        if self.joystick_y < -0.2:
            return min(
                1.0,
                abs(self.joystick_y)
            )

        return 0.0

    @property
    def brake_amount(self):

        if self.brake:
            return 1.0

        if self.joystick_y > 0.2:
            return min(
                1.0,
                self.joystick_y
            )

        return 0.0

    @property
    def steering(self):

        if self.steer_left:
            return -1.0

        if self.steer_right:
            return 1.0

        if abs(self.joystick_x) > 0.2:
            return self.joystick_x

        return 0.0


class KeyboardControls:

    KEY_ACTIONS = {

        "W": "accelerate",
        "UP": "accelerate",

        "S": "brake",
        "DOWN": "brake",

        "A": "steer_left",
        "LEFT": "steer_left",

        "D": "steer_right",
        "RIGHT": "steer_right",

        "SPACE": "handbrake",

        "F": "enter_exit",
        "H": "horn",
        "R": "radio",
        "M": "map",
        "E": "interact",
        "ESC": "pause",
    }

    def __init__(self):
        self.state = InputState()

    def key_down(self, key):

        action = self.KEY_ACTIONS.get(key)

        if action is None:
            return

        if action in (
            "enter_exit",
            "horn",
            "radio",
            "map",
            "interact",
            "pause",
        ):

            setattr(
                self.state,
                action,
                True
            )

        else:

            setattr(
                self.state,
                action,
                True
            )

    def key_up(self, key):

        action = self.KEY_ACTIONS.get(key)

        if action is None:
            return

        if action in (
            "enter_exit",
            "horn",
            "radio",
            "map",
            "interact",
            "pause",
        ):
            return

        setattr(
            self.state,
            action,
            False
        )

    def get_state(self):
        return self.state


class TouchControls:

    def __init__(self):
        self.state = InputState()

    def joystick(
        self,
        x,
        y
    ):

        self.state.joystick_x = max(
            -1.0,
            min(1.0, x)
        )

        self.state.joystick_y = max(
            -1.0,
            min(1.0, y)
        )

    def button_down(self, button):

        if button == "ACCELERATE":
            self.state.accelerate = True

        elif button == "BRAKE":
            self.state.brake = True

        elif button == "LEFT":
            self.state.steer_left = True

        elif button == "RIGHT":
            self.state.steer_right = True

        elif button == "HANDBRAKE":
            self.state.handbrake = True

        elif button == "ENTER":
            self.state.enter_exit = True

        elif button == "HORN":
            self.state.horn = True

        elif button == "RADIO":
            self.state.radio = True

        elif button == "MAP":
            self.state.map = True

        elif button == "INTERACT":
            self.state.interact = True

        elif button == "PAUSE":
            self.state.pause = True

    def button_up(self, button):

        if button == "ACCELERATE":
            self.state.accelerate = False

        elif button == "BRAKE":
            self.state.brake = False

        elif button == "LEFT":
            self.state.steer_left = False

        elif button == "RIGHT":
            self.state.steer_right = False

        elif button == "HANDBRAKE":
            self.state.handbrake = False

    def get_state(self):
        return self.state


class ControlManager:

    def __init__(self):

        self.keyboard = KeyboardControls()
        self.touch = TouchControls()

        self.mode = "KEYBOARD"

    def use_keyboard(self):
        self.mode = "KEYBOARD"

    def use_touch(self):
        self.mode = "TOUCH"

    def get_state(self):

        if self.mode == "TOUCH":
            return self.touch.get_state()

        return self.keyboard.get_state()
