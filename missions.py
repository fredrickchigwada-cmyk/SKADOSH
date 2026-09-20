from dataclasses import dataclass, field
import math


@dataclass
class Mission:
    mission_id: str
    title: str
    mission_type: str
    start_x: float
    start_y: float
    target_x: float
    target_y: float

    objectives: list = field(default_factory=list)
    reward_money: int = 0
    reward_xp: int = 0
    reputation_type: str = "CITIZEN"
    reputation_reward: int = 0

    current_objective: int = 0
    active: bool = False
    completed: bool = False

    def start(self):
        if self.completed:
            return False

        self.active = True
        self.current_objective = 0
        return True

    def current_objective_text(self):
        if not self.objectives:
            return "No objective"

        if self.current_objective >= len(self.objectives):
            return "Mission complete"

        return self.objectives[self.current_objective]

    def advance(self):
        if not self.active:
            return False

        self.current_objective += 1

        if self.current_objective >= len(self.objectives):
            self.completed = True
            self.active = False

        return True

    def distance_to_target(self, player_x, player_y):
        return math.hypot(
            self.target_x - player_x,
            self.target_y - player_y
        )

    def status(self, player_x, player_y):
        return {
            "id": self.mission_id,
            "title": self.title,
            "type": self.mission_type,
            "active": self.active,
            "completed": self.completed,
            "objective": self.current_objective_text(),
            "distance": round(
                self.distance_to_target(
                    player_x,
                    player_y
                ),
                2
            ),
            "reward_money": self.reward_money,
            "reward_xp": self.reward_xp,
        }


class MissionManager:
    def __init__(self):
        self.missions = {}
        self.active_mission = None

    def add(self, mission):
        self.missions[mission.mission_id] = mission

    def get(self, mission_id):
        return self.missions.get(mission_id)

    def start(self, mission_id):
        mission = self.get(mission_id)

        if mission is None:
            return False

        if self.active_mission:
            return False

        if mission.start():
            self.active_mission = mission
            return True

        return False

    def advance(self):
        if self.active_mission is None:
            return False

        mission = self.active_mission

        mission.advance()

        if mission.completed:
            self.active_mission = None

        return True

    def get_active_status(self, player_x, player_y):
        if self.active_mission is None:
            return None

        return self.active_mission.status(
            player_x,
            player_y
        )


class GPS:
    def __init__(self):
        self.destination_x = None
        self.destination_y = None

    def set_destination(self, x, y):
        self.destination_x = x
        self.destination_y = y

    def clear(self):
        self.destination_x = None
        self.destination_y = None

    def distance(self, player_x, player_y):
        if self.destination_x is None:
            return None

        return math.hypot(
            self.destination_x - player_x,
            self.destination_y - player_y
        )

    def direction(self, player_x, player_y):
        if self.destination_x is None:
            return None

        dx = self.destination_x - player_x
        dy = self.destination_y - player_y

        if abs(dx) > abs(dy):
            return "EAST" if dx > 0 else "WEST"

        return "SOUTH" if dy > 0 else "NORTH"

    def status(self, player_x, player_y):
        if self.destination_x is None:
            return {
                "active": False,
                "distance": None,
                "direction": None
            }

        return {
            "active": True,
            "distance": round(
                self.distance(
                    player_x,
                    player_y
                ),
                2
            ),
            "direction": self.direction(
                player_x,
                player_y
            )
        }
