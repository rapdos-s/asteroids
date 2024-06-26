from database import Database
from game import Game

if __name__ == "__main__":
    print("🚀 ABC | 42 Asteroids 🌑")

    npcs: list[str] = [
        "KAREN",
        "CAIO",
        "TUCA",
        "MARVIN",
        "FERNAO",
        "FERNANDA",
        "LUCAS",
        "KIM",
        "MARCEL",
        "MAURICIO",
    ]

    database: Database = Database()

    for npc in npcs:
        database.delete_player(npc)
    for npc in npcs:
        if database.read_player(npc) is None:
            database.create_player(npc)

    # # player: str = database.read_player("KAREN")
    # # database.update_player("KAREN", "KAKÁ")
    # # database.delete_player("KAKÁ")

    database.show_all_tables()
    database.select_all_players()
    # database.commit()

    # game: Game = Game()
    # game.run()

    print("🌌 Everything is done, Bye!")
