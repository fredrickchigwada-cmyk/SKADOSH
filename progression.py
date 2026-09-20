from dataclasses import dataclass


REPUTATION_TYPES = [
    "CITIZEN",
    "DRIVER",
    "RACER",
    "BUSINESS",
    "VIP",
    "EXPLORER",
]


@dataclass
class Achievement:
    achievement_id: str
    name: str
    description: str
    reward_money: int
    reward_xp: int
    reputation_type: str = "CITIZEN"
    reputation_reward: int = 0


ACHIEVEMENTS = {
    "FIRST_DRIVE": Achievement(
        "FIRST_DRIVE",
        "FIRST DRIVE",
        "Drive your first vehicle.",
        1000,
        100,
        "DRIVER",
        5
    ),

    "ROAD_KING": Achievement(
        "ROAD_KING",
        "ROAD KING",
        "Complete 10 driving missions.",
        5000,
        500,
        "DRIVER",
        20
    ),

    "RACER": Achievement(
        "RACER",
        "RACER",
        "Complete your first race.",
        2500,
        250,
        "RACER",
        10
    ),

    "EXPLORER": Achievement(
        "EXPLORER",
        "EXPLORER",
        "Visit 10 different locations.",
        3000,
        300,
        "EXPLORER",
        15
    ),

    "BIG_SPENDER": Achievement(
        "BIG_SPENDER",
        "BIG SPENDER",
        "Spend $50,000.",
        5000,
        500,
        "BUSINESS",
        10
    ),

    "TYCOON": Achievement(
        "TYCOON",
        "TYCOON",
        "Own 3 businesses.",
        15000,
        1000,
        "BUSINESS",
        30
    ),

    "VIP": Achievement(
        "VIP",
        "VIP",
        "Complete your first VIP mission.",
        10000,
        750,
        "VIP",
        25
    ),

    "SKADOSH_LEGEND": Achievement(
        "SKADOSH_LEGEND",
        "SKADOSH LEGEND",
        "Reach level 25.",
        50000,
        5000,
        "CITIZEN",
        50
    ),
}


class ProgressionSystem:

    def __init__(self, player):
        self.player = player

    def unlock_achievement(self, achievement_id):
        achievement = ACHIEVEMENTS.get(
            achievement_id
        )

        if achievement is None:
            return False

        if achievement_id in self.player.achievements:
            return False

        self.player.achievements.append(
            achievement_id
        )

        self.player.add_money(
            achievement.reward_money,
            f"Achievement: {achievement.name}"
        )

        self.player.add_xp(
            achievement.reward_xp
        )

        self.player.add_reputation(
            achievement.reputation_type,
            achievement.reputation_reward
        )

        return True

    def reputation_level(self, reputation_type):
        value = self.player.reputation.get(
            reputation_type,
            0
        )

        if value >= 100:
            return "LEGEND"
        elif value >= 75:
            return "ELITE"
        elif value >= 50:
            return "EXPERT"
        elif value >= 25:
            return "RISING"
        elif value > 0:
            return "BEGINNER"

        return "UNKNOWN"

    def can_unlock(self, reputation_type, required):
        return self.player.reputation.get(
            reputation_type,
            0
        ) >= required

    def status(self):
        reputation = {}

        for rep_type in REPUTATION_TYPES:
            reputation[rep_type] = {
                "value": self.player.reputation.get(
                    rep_type,
                    0
                ),
                "rank": self.reputation_level(
                    rep_type
                )
            }

        return {
            "level": self.player.level,
            "xp": self.player.xp,
            "money": self.player.money,
            "achievements": len(
                self.player.achievements
            ),
            "reputation": reputation,
        }
