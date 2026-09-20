from config import CHARACTERS


class CharacterSystem:
    def __init__(self):
        self.characters = CHARACTERS

    def show_characters(self):
        print()
        print("SKADOSH CHARACTER SELECT")
        print("========================")

        for number, character in enumerate(self.characters, 1):
            print(f"{number:02d}. {character}")

    def select(self, number):
        if 1 <= number <= len(self.characters):
            return self.characters[number - 1]

        raise ValueError("Invalid character number.")
