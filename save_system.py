import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SAVE_DIR = BASE_DIR / "saves"


def save_game(player, slot=1):
    SAVE_DIR.mkdir(parents=True, exist_ok=True)

    save_file = SAVE_DIR / f"save_{slot}.json"

    data = {
        "name": player.name,
        "character": player.character,
        "money": player.money,
        "level": player.level,
        "xp": player.xp,
        "inventory": player.inventory,
        "vehicles": player.vehicles,
        "properties": player.properties,
        "businesses": player.businesses,
        "completed_missions": player.completed_missions,
        "reputation": player.reputation
    }

    with save_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    return save_file


def load_game(slot=1):
    save_file = SAVE_DIR / f"save_{slot}.json"

    if not save_file.exists():
        return None

    with save_file.open("r", encoding="utf-8") as file:
        return json.load(file)
