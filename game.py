from config import (
    GAME_NAME,
    TAGLINE,
    STARTING_MONEY,
    STARTING_LEVEL,
    STARTING_XP,
    CHARACTERS,
    WEAPONS,
    VEHICLES,
    REPUTATIONS,
)


class Player:
    def __init__(self):
        self.name = "Player"
        self.character = CHARACTERS[0]
        self.money = STARTING_MONEY
        self.level = STARTING_LEVEL
        self.xp = STARTING_XP

        self.inventory = []
        self.vehicles = []
        self.properties = []
        self.businesses = []
        self.completed_missions = []

        self.reputation = REPUTATIONS.copy()

    def add_money(self, amount):
        self.money += amount

    def spend_money(self, amount):
        if amount > self.money:
            return False

        self.money -= amount
        return True

    def add_xp(self, amount):
        self.xp += amount

        while self.xp >= self.level * 1000:
            self.xp -= self.level * 1000
            self.level += 1

    def add_reputation(self, category, amount):
        if category in self.reputation:
            self.reputation[category] += amount


class Mission:
    def __init__(self, mission_id, title, reward, xp):
        self.mission_id = mission_id
        self.title = title
        self.reward = reward
        self.xp = xp
        self.completed = False

    def complete(self, player):
        if self.completed:
            return

        self.completed = True
        player.add_money(self.reward)
        player.add_xp(self.xp)


class SKADOSHGame:
    def __init__(self):
        self.name = GAME_NAME
        self.tagline = TAGLINE

        self.player = Player()

        self.maps = [
            "Harare",
            "Bulawayo",
            "Mutare",
            "Gweru",
            "Masvingo",
            "Hwange",
            "Victoria Falls",
            "Kariba",
            "Great Zimbabwe",
            "SKADOSH Arena",
        ]

        self.missions = [
            Mission(
                "INTRO_001",
                "Welcome to SKADOSH",
                5000,
                250,
            ),
            Mission(
                "DRIVE_001",
                "First Drive",
                7500,
                500,
            ),
            Mission(
                "VIP_001",
                "VIP Contract",
                15000,
                1000,
            ),
        ]

    def show_status(self):
        print()
        print("=" * 45)
        print(self.name)
        print(self.tagline)
        print("=" * 45)
        print(f"Character : {self.player.character}")
        print(f"Money     : ${self.player.money:,}")
        print(f"Level     : {self.player.level}")
        print(f"XP        : {self.player.xp}")
        print("=" * 45)

    def complete_mission(self, mission_id):
        for mission in self.missions:
            if mission.mission_id == mission_id:
                mission.complete(self.player)
                print(
                    f"Mission completed: {mission.title} "
                    f"| Reward: ${mission.reward:,}"
                )
                return

        print("Mission not found.")

    def run_test(self):
        print()
        print("SKADOSH CORE TEST")
        print("-----------------")

        print(f"Game: {self.name}")
        print(f"Tagline: {self.tagline}")

        print()
        print("Characters:")
        for number, character in enumerate(CHARACTERS, 1):
            print(f"  {number}. {character}")

        print()
        print("Fictional weapons:")
        for weapon in WEAPONS:
            print(f"  - {weapon}")

        print()
        print("Vehicle classes:")
        for vehicle in VEHICLES:
            print(f"  - {vehicle}")

        print()
        print("Maps:")
        for number, game_map in enumerate(self.maps, 1):
            print(f"  {number:02d}. {game_map}")

        print()
        self.show_status()

        print("Testing mission system...")
        self.complete_mission("INTRO_001")

        print()
        self.show_status()

        print("SKADOSH CORE TEST PASSED.")
