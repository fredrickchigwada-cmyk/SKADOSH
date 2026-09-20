import time

from player_profile import PlayerProfile
from world import World
from npcs import NPCManager, TrafficManager
from missions import Mission, MissionManager, GPS
from progression import ProgressionSystem


class SKADOSHGame:

    def __init__(self):

        # -------------------------
        # PLAYER
        # -------------------------

        self.player = PlayerProfile()

        # -------------------------
        # WORLD
        # -------------------------

        self.world = World("Harare")

        # -------------------------
        # NPC SYSTEM
        # -------------------------

        self.npcs = NPCManager(
            self.world.width,
            self.world.height
        )

        self.npcs.spawn_crowd(50)

        # -------------------------
        # TRAFFIC
        # -------------------------

        self.traffic = TrafficManager(
            self.world.width
        )

        self.traffic.spawn_traffic(20)

        # -------------------------
        # MISSIONS
        # -------------------------

        self.missions = MissionManager()

        self.create_missions()

        # -------------------------
        # GPS
        # -------------------------

        self.gps = GPS()

        # -------------------------
        # PROGRESSION
        # -------------------------

        self.progression = ProgressionSystem(
            self.player
        )

        # -------------------------
        # GAME STATE
        # -------------------------

        self.running = True

        self.game_time = 0.0

    # ==================================================
    # MISSIONS
    # ==================================================

    def create_missions(self):

        intro = Mission(
            mission_id="INTRO_001",
            title="Welcome to SKADOSH",
            mission_type="INTRO",

            start_x=2500,
            start_y=2500,

            target_x=3000,
            target_y=3000,

            objectives=[
                "Explore the city.",
                "Visit the vehicle garage.",
                "Drive your first vehicle.",
                "Reach the destination.",
            ],

            reward_money=5000,
            reward_xp=500,

            reputation_type="CITIZEN",
            reputation_reward=10
        )

        race = Mission(
            mission_id="RACE_001",
            title="Harare Street Run",
            mission_type="RACING",

            start_x=1500,
            start_y=1500,

            target_x=4000,
            target_y=1500,

            objectives=[
                "Reach the race starting point.",
                "Start the race.",
                "Pass the checkpoints.",
                "Finish the race.",
            ],

            reward_money=10000,
            reward_xp=750,

            reputation_type="RACER",
            reputation_reward=15
        )

        vip = Mission(
            mission_id="VIP_001",
            title="VIP Convoy",
            mission_type="VIP",

            start_x=1000,
            start_y=1000,

            target_x=3500,
            target_y=3500,

            objectives=[
                "Meet the VIP.",
                "Enter the vehicle.",
                "Drive to the destination.",
                "Protect the convoy.",
                "Reach the safe zone.",
            ],

            reward_money=15000,
            reward_xp=1000,

            reputation_type="VIP",
            reputation_reward=20
        )

        self.missions.add(intro)
        self.missions.add(race)
        self.missions.add(vip)

    # ==================================================
    # MISSION CONTROL
    # ==================================================

    def start_mission(self, mission_id):

        result = self.missions.start(
            mission_id
        )

        if result:

            mission = self.missions.get(
                mission_id
            )

            self.gps.set_destination(
                mission.target_x,
                mission.target_y
            )

        return result

    def advance_mission(self):

        mission = self.missions.active_mission

        if mission is None:
            return False

        mission.advance()

        if mission.completed:

            self.player.complete_mission(
                mission.mission_id,
                mission.reward_money,
                mission.reward_xp,
                mission.reputation_type,
                mission.reputation_reward
            )

            self.gps.clear()

            return True

        return True

    # ==================================================
    # VEHICLES
    # ==================================================

    def spawn_vehicle(self, vehicle_class):

        return self.world.spawn_vehicle(
            vehicle_class
        )

    def enter_vehicle(self):

        if self.world.vehicle is None:
            return False

        return self.world.vehicle.enter()

    def exit_vehicle(self):

        if self.world.vehicle is None:
            return False

        return self.world.vehicle.exit()

    # ==================================================
    # WORLD UPDATE
    # ==================================================

    def update(
        self,
        throttle=0.0,
        brake=0.0,
        steering=0.0,
        dt=1 / 60
    ):

        if not self.running:
            return

        self.game_time += dt

        # Vehicle/world
        self.world.update(
            throttle,
            brake,
            steering,
            dt
        )

        # NPCs
        self.npcs.update(
            self.world.player_x,
            self.world.player_y,
            dt
        )

        # Traffic
        self.traffic.update(
            dt
        )

    # ==================================================
    # PLAYER POSITION
    # ==================================================

    @property
    def player_x(self):
        return self.world.player_x

    @property
    def player_y(self):
        return self.world.player_y

    # ==================================================
    # STATUS
    # ==================================================

    def status(self):

        mission = self.missions.active_mission

        mission_status = None

        if mission:

            mission_status = mission.status(
                self.player_x,
                self.player_y
            )

        return {
            "game": "SKADOSH",
            "player": self.player.status(),
            "world": self.world.status(),
            "npc_count": len(
                self.npcs.npcs
            ),
            "traffic_count": len(
                self.traffic.vehicles
            ),
            "mission": mission_status,
            "gps": self.gps.status(
                self.player_x,
                self.player_y
            ),
            "progression":
                self.progression.status(),
            "game_time":
                round(
                    self.game_time,
                    2
                )
        }


def run_demo():

    print()
    print("================================")
    print("       SKADOSH GAME ENGINE")
    print("================================")
    print()

    game = SKADOSHGame()

    print("Game:", "SKADOSH")
    print("Player:", game.player.name)
    print("Character:", game.player.character)
    print("Money: $", game.player.money)

    print()
    print("World:", game.world.name)
    print(
        "World size:",
        game.world.width,
        "x",
        game.world.height
    )

    print(
        "NPCs:",
        len(game.npcs.npcs)
    )

    print(
        "Traffic:",
        len(game.traffic.vehicles)
    )

    print()
    print("Starting intro mission...")

    started = game.start_mission(
        "INTRO_001"
    )

    print(
        "Mission started:",
        started
    )

    print()
    print("Running game simulation...")

    for _ in range(300):

        game.update(
            throttle=0.3,
            brake=0.0,
            steering=0.05,
            dt=1 / 60
        )

    print()
    print("GAME STATUS")
    print("-----------")

    status = game.status()

    print(
        "Player position:",
        round(game.player_x, 2),
        round(game.player_y, 2)
    )

    print(
        "Mission:",
        status["mission"]["title"]
        if status["mission"]
        else "None"
    )

    print(
        "GPS distance:",
        status["gps"]["distance"]
    )

    print(
        "NPCs:",
        status["npc_count"]
    )

    print(
        "Traffic:",
        status["traffic_count"]
    )

    print()
    print("SKADOSH GAME ENGINE OK")


if __name__ == "__main__":
    run_demo()
