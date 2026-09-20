from game import Player
from save_system import save_game, load_game
from character_system import CharacterSystem


player = Player()

characters = CharacterSystem()
characters.show_characters()

player.character = characters.select(1)
player.name = "SKADOSH Player"

player.add_money(10000)
player.add_xp(500)

save_file = save_game(player, 1)

print()
print("SAVE CREATED")
print("File:", save_file)

loaded = load_game(1)

print()
print("LOADED SAVE")
print("============")
print("Player:", loaded["name"])
print("Character:", loaded["character"])
print("Money:", f"${loaded['money']:,}")
print("Level:", loaded["level"])
print("XP:", loaded["xp"])

print()
print("SAVE SYSTEM OK")
