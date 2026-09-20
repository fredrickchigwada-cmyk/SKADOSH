from player_profile import PlayerProfile


def main():
    print("SKADOSH PLAYER PROFILE TEST")
    print("===========================")

    player = PlayerProfile()

    print("Player:", player.name)
    print("Character:", player.character)
    print("Starting money: $", player.money)

    print()
    print("Adding vehicle...")
    player.add_vehicle("Supercar")

    print("Adding property...")
    player.add_property("SKADOSH Apartment")

    print("Adding business...")
    player.add_business("SKADOSH Garage")

    print()
    print("Completing mission...")

    player.complete_mission(
        mission_id="INTRO_001",
        reward_money=5000,
        reward_xp=500,
        reputation_type="CITIZEN",
        reputation_reward=10
    )

    print("Money: $", player.money)
    print("XP:", player.xp)
    print("Level:", player.level)

    print()
    print("Adding inventory...")

    player.inventory.add(
        "food_pack",
        3
    )

    player.inventory.add(
        "med_kit",
        2
    )

    print(
        "Inventory:",
        player.inventory.status()
    )

    print()
    print("Unlocking achievement...")

    player.unlock_achievement(
        "FIRST DRIVE"
    )

    print(
        "Achievements:",
        player.achievements
    )

    print()
    print("Reputation:")
    for key, value in player.reputation.items():
        print(
            key,
            ":",
            value
        )

    print()
    print("PLAYER PROFILE SYSTEM OK")


if __name__ == "__main__":
    main()
