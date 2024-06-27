from database import Database
from game import Game

if __name__ == "__main__":
    print("🚀 ABC | 42 Asteroids 🌑")

    database: Database = Database()

    database.select_all_players()
    print(
        "################################################################################"
    )
    print("DELETE")
    database.delete_player_by_id(1)
    database.delete_player_by_name("CAIO")

    print(
        "################################################################################"
    )
    database.select_all_players()

    # game: Game = Game()
    # game.run()

    print("🌌 Everything is done, Bye!")
