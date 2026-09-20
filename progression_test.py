from player_profile import PlayerProfile
from progression import ProgressionSystem


def main():

    print("SKADOSH PROGRESSION TEST")
    print("========================")

    player = PlayerProfile()

    progression = ProgressionSystem(
        player
    )

    print("Starting level:")
    print(player.level)

    print()
    print("Completing FIRST DRIVE...")

    result = progression.unlock_achievement(
        "FIRST_DRIVE"
    )

    print(
        "Achievement unlocked:",
        result
    )

    print(
        "Money:",
        player.money
    )

    print(
        "XP:",
        player.xp
    )

    print(
        "Driver reputation:",
        player.reputation["DRIVER"]
    )

    print(
        "Driver rank:",
        progression.reputation_level(
            "DRIVER"
        )
    )

    print()
    print("Testing reputation progression...")

    player.add_reputation(
        "RACER",
        50
    )

    print(
        "Racer reputation:",
        player.reputation["RACER"]
    )

    print(
        "Racer rank:",
        progression.reputation_level(
            "RACER"
        )
    )

    print()
    print("Testing unlock requirement...")

    unlocked = progression.can_unlock(
        "RACER",
        50
    )

    print(
        "Racer content unlocked:",
        unlocked
    )

    print()
    print("Progression status:")

    status = progression.status()

    print(
        "Level:",
        status["level"]
    )

    print(
        "XP:",
        status["xp"]
    )

    print(
        "Achievements:",
        status["achievements"]
    )

    print()
    print("PROGRESSION SYSTEM OK")


if __name__ == "__main__":
    main()
