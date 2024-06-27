from database import Database
from game import Game

if __name__ == "__main__":
    print("🚀 ABC | 42 Asteroids 🌑")

    database: Database = Database()

    print(
        "################################################################################"
    )
    database.select_all_players()
    print(
        "################################################################################"
    )
    database.select_all_leaderboard()
    print(
        "################################################################################"
    )
    database.select_all_score_history()
    print(
        "################################################################################"
    )
    database.select_all_achievements()
    print(
        "################################################################################"
    )
    database.select_all_player_achievements()

    # game: Game = Game()
    # game.run()

    print("🌌 Everything is done, Bye!")
