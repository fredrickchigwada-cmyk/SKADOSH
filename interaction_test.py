from skadosh_game import SKADOSHGame
from interaction import InteractionSystem


def main():

    print("SKADOSH INTERACTION TEST")
    print("=========================")

    game = SKADOSHGame()

    interaction = InteractionSystem(
        game
    )

    # Put player close to the mission hub
    game.world.player_x = 2500
    game.world.player_y = 2500

    location = (
        interaction.get_interactable()
    )

    print(
        "Nearest interactable:",
        location.name
        if location
        else "None"
    )

    entered = interaction.enter()

    print(
        "Entered:",
        entered
    )

    result = interaction.action()

    print(
        "Action:",
        result["action"]
    )

    print(
        "Message:",
        result["message"]
    )

    interaction.exit()

    print(
        "Exited:",
        not interaction.inside_location
    )

    # Test school
    school = interaction.locations.by_type(
        "SCHOOL"
    )[0]

    game.world.player_x = school.x
    game.world.player_y = school.y

    location = (
        interaction.get_interactable()
    )

    print()
    print(
        "School detected:",
        location.name
        if location
        else "None"
    )

    interaction.enter()

    school_result = (
        interaction.action()
    )

    print(
        "School action:",
        school_result["action"]
    )

    print()
    print("INTERACTION SYSTEM OK")


if __name__ == "__main__":
    main()
