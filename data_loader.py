import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "game_data.json"


def load_game_data():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    data = load_game_data()

    print("SKADOSH DATA TEST")
    print("=================")
    print("Game:", data["game"]["name"])
    print("Characters:", len(data["characters"]))
    print("Weapons:", len(data["weapons"]))
    print("Vehicles:", len(data["vehicles"]))
    print("Maps:", len(data["maps"]))
    print("Businesses:", len(data["businesses"]))
    print("Game modes:", len(data["game_modes"]))
    print("DATA SYSTEM OK")
