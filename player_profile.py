from dataclasses import dataclass, field
from economy import Economy, Inventory


@dataclass
class PlayerProfile:
    name: str = "SKADOSH Player"
    character: str = "Tyson"

    level: int = 1
    xp: int = 0

    economy: Economy = field(
        default_factory=lambda: Economy(100000)
    )

    inventory: Inventory = field(
        default_factory=Inventory
    )

    vehicles: list = field(default_factory=list)
    properties: list = field(default_factory=list)
    businesses: list = field(default_factory=list)

    completed_missions: list = field(
        default_factory=list
    )

    achievements: list = field(
        default_factory=list
    )

    reputation: dict = field(
        default_factory=lambda: {
            "CITIZEN": 0,
            "DRIVER": 0,
            "RACER": 0,
            "BUSINESS": 0,
            "VIP": 0,
            "EXPLORER": 0,
        }
    )

    def add_money(self, amount, reason="income"):
        self.economy.add_money(
            amount,
            reason
        )

    def spend_money(self, amount, reason="expense"):
        return self.economy.spend_money(
            amount,
            reason
        )

    @property
    def money(self):
        return self.economy.money

    def add_xp(self, amount):
        self.xp += amount

        level_up_count = 0

        while self.xp >= self.level * 1000:
            self.xp -= self.level * 1000
            self.level += 1
            level_up_count += 1

        return level_up_count

    def add_reputation(
        self,
        reputation_type,
        amount
    ):
        if reputation_type not in self.reputation:
            self.reputation[reputation_type] = 0

        self.reputation[reputation_type] += amount

    def complete_mission(
        self,
        mission_id,
        reward_money,
        reward_xp,
        reputation_type,
        reputation_reward
    ):
        if mission_id in self.completed_missions:
            return False

        self.completed_missions.append(
            mission_id
        )

        self.add_money(
            reward_money,
            f"Mission {mission_id}"
        )

        self.add_xp(
            reward_xp
        )

        self.add_reputation(
            reputation_type,
            reputation_reward
        )

        return True

    def add_vehicle(self, vehicle_name):
        if vehicle_name not in self.vehicles:
            self.vehicles.append(
                vehicle_name
            )

    def add_property(self, property_name):
        if property_name not in self.properties:
            self.properties.append(
                property_name
            )

    def add_business(self, business_name):
        if business_name not in self.businesses:
            self.businesses.append(
                business_name
            )

    def unlock_achievement(self, achievement):
        if achievement not in self.achievements:
            self.achievements.append(
                achievement
            )

    def status(self):
        return {
            "name": self.name,
            "character": self.character,
            "money": self.money,
            "level": self.level,
            "xp": self.xp,
            "vehicles": self.vehicles,
            "properties": self.properties,
            "businesses": self.businesses,
            "missions": self.completed_missions,
            "achievements": self.achievements,
            "reputation": self.reputation,
            "inventory": self.inventory.status(),
        }
