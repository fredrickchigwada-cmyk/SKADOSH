from missions import Mission, MissionManager, GPS


def main():
    print("SKADOSH MISSION & GPS TEST")
    print("==========================")

    manager = MissionManager()

    mission = Mission(
        mission_id="VIP_CONVOY",
        title="VIP Convoy",
        mission_type="VIP",
        start_x=1000,
        start_y=1000,
        target_x=3000,
        target_y=3500,
        objectives=[
            "Meet the VIP.",
            "Enter the vehicle.",
            "Drive to the destination.",
            "Protect the convoy.",
            "Reach the safe zone.",
        ],
        reward_money=15000,
        reward_xp=500,
        reputation_type="VIP",
        reputation_reward=10,
    )

    manager.add(mission)

    print("Mission added:", mission.title)

    started = manager.start("VIP_CONVOY")

    print("Mission started:", started)

    player_x = 1200
    player_y = 1300

    status = manager.get_active_status(
        player_x,
        player_y
    )

    print()
    print("MISSION STATUS")
    print("Title:", status["title"])
    print("Objective:", status["objective"])
    print("Distance:", status["distance"])
    print("Reward: $", status["reward_money"])
    print("XP:", status["reward_xp"])

    gps = GPS()

    gps.set_destination(
        mission.target_x,
        mission.target_y
    )

    gps_status = gps.status(
        player_x,
        player_y
    )

    print()
    print("GPS STATUS")
    print("Active:", gps_status["active"])
    print("Distance:", gps_status["distance"])
    print("Direction:", gps_status["direction"])

    print()
    print("Advancing objectives...")

    for i in range(5):
        manager.advance()
        print(
            "Objective step:",
            i + 1
        )

    print()
    print("Mission completed:",
          mission.completed)

    print()
    print("MISSION & GPS SYSTEM OK")


if __name__ == "__main__":
    main()
