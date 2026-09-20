from npcs import NPCManager, TrafficManager


def main():
    print("SKADOSH NPC & TRAFFIC TEST")
    print("===========================")

    width = 5000
    height = 5000

    npcs = NPCManager(width, height)

    print("Spawning NPC population...")
    npcs.spawn_crowd(50)

    print("NPCs:", len(npcs.npcs))

    player_x = 2500
    player_y = 2500

    print()
    print("Updating NPC world...")

    for _ in range(60):
        npcs.update(
            player_x,
            player_y,
            1 / 60
        )

    nearby = npcs.nearby(
        player_x,
        player_y,
        500
    )

    print("NPCs near player:", len(nearby))

    if nearby:
        npc = nearby[0]

        print()
        print("Example NPC:")
        print("ID:", npc.npc_id)
        print("Name:", npc.name)
        print("Role:", npc.role)
        print(
            "Position:",
            round(npc.x, 2),
            round(npc.y, 2)
        )

    print()
    print("Spawning traffic...")

    traffic = TrafficManager(width)
    traffic.spawn_traffic(20)

    print("Traffic vehicles:", len(traffic.vehicles))

    for _ in range(60):
        traffic.update(1 / 60)

    print("Traffic simulation running.")

    print()
    print("NPC & TRAFFIC SYSTEM OK")


if __name__ == "__main__":
    main()
