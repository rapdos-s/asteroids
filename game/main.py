from database import Database
from game import Game

if __name__ == "__main__":
    print("🚀 ABC | 42 Asteroids 🌑")

    database: Database = Database()
    database.select_all_players()

    # game: Game = Game()
    # game.run()

    print("🌌 Everything is done, Bye!")
