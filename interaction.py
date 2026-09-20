from locations import create_location_manager


INTERACTION_DISTANCE = 120


class InteractionSystem:

    def __init__(self, game):

        self.game = game

        self.locations = (
            create_location_manager()
        )

        self.current_location = None
        self.inside_location = False

    # ==================================================
    # FIND NEAREST LOCATION
    # ==================================================

    def nearest_location(self):

        return self.locations.nearest(
            self.game.player_x,
            self.game.player_y
        )

    # ==================================================
    # FIND INTERACTABLE LOCATION
    # ==================================================

    def get_interactable(self):

        nearby = self.locations.nearby(
            self.game.player_x,
            self.game.player_y,
            INTERACTION_DISTANCE
        )

        if not nearby:
            return None

        for location in nearby:

            if (
                location.interactive
                and location.unlocked
            ):
                return location

        return None

    # ==================================================
    # ENTER LOCATION
    # ==================================================

    def enter(self):

        location = self.get_interactable()

        if location is None:
            return False

        self.current_location = location
        self.inside_location = True

        return True

    # ==================================================
    # EXIT LOCATION
    # ==================================================

    def exit(self):

        if not self.inside_location:
            return False

        self.inside_location = False
        self.current_location = None

        return True

    # ==================================================
    # LOCATION ACTION
    # ==================================================

    def action(self):

        location = self.current_location

        if location is None:
            return {
                "success": False,
                "message": "No location selected."
            }

        location_type = (
            location.location_type
        )

        # -------------------------------
        # SHOP
        # -------------------------------

        if location_type == "SHOP":

            return {
                "success": True,
                "action": "OPEN_SHOP",
                "message":
                    f"Welcome to {location.name}"
            }

        # -------------------------------
        # GARAGE
        # -------------------------------

        if location_type == "GARAGE":

            return {
                "success": True,
                "action": "OPEN_GARAGE",
                "message":
                    "Garage ready."
            }

        # -------------------------------
        # RESTAURANT
        # -------------------------------

        if location_type == "RESTAURANT":

            return {
                "success": True,
                "action": "OPEN_RESTAURANT",
                "message":
                    "Welcome to the restaurant."
            }

        # -------------------------------
        # HOSPITAL
        # -------------------------------

        if location_type == "HOSPITAL":

            return {
                "success": True,
                "action": "HEAL",
                "message":
                    "Medical services available."
            }

        # -------------------------------
        # SCHOOL
        # -------------------------------

        if location_type == "SCHOOL":

            return {
                "success": True,
                "action": "SCHOOL",
                "message":
                    f"Welcome to {location.name}"
            }

        # -------------------------------
        # BUSINESS
        # -------------------------------

        if location_type == "BUSINESS":

            return {
                "success": True,
                "action": "BUSINESS",
                "message":
                    f"Business location: {location.name}"
            }

        # -------------------------------
        # PROPERTY
        # -------------------------------

        if location_type == "PROPERTY":

            return {
                "success": True,
                "action": "PROPERTY",
                "message":
                    f"Property: {location.name}"
            }

        # -------------------------------
        # RACE
        # -------------------------------

        if location_type == "RACE":

            return {
                "success": True,
                "action": "RACE",
                "message":
                    f"Race location: {location.name}"
            }

        # -------------------------------
        # VIP
        # -------------------------------

        if location_type == "VIP":

            return {
                "success": True,
                "action": "VIP",
                "message":
                    "VIP area entered."
            }

        # -------------------------------
        # MISSION
        # -------------------------------

        if location_type == "MISSION":

            return {
                "success": True,
                "action": "MISSION",
                "message":
                    "Mission hub available."
            }

        # -------------------------------
        # AIRPORT
        # -------------------------------

        if location_type == "AIRPORT":

            return {
                "success": True,
                "action": "AIRPORT",
                "message":
                    "Airport services available."
            }

        # -------------------------------
        # FAST TRAVEL
        # -------------------------------

        if location_type == "FAST_TRAVEL":

            return {
                "success": True,
                "action": "FAST_TRAVEL",
                "message":
                    "Fast travel available."
            }

        return {
            "success": True,
            "action": "INTERACT",
            "message":
                f"Interacting with {location.name}"
        }

    # ==================================================
    # STATUS
    # ==================================================

    def status(self):

        nearby = self.get_interactable()

        return {
            "nearby": (
                nearby.name
                if nearby
                else None
            ),
            "inside": self.inside_location,
            "current": (
                self.current_location.name
                if self.current_location
                else None
            )
        }
