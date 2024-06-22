from dotenv import load_dotenv
from constants import *

import psycopg2
import os


class Database:
    def __init__(self: object):
        print("💾 Database connection opened.")
        load_dotenv()

        self.database_name: str = os.getenv("DATABASE_NAME")
        self.database_user: str = os.getenv("DATABASE_USER")
        self.database_password: str = os.getenv("DATABASE_PASSWORD")
        self.database_host: str = os.getenv("DATABASE_HOST")

        self.database_connection: psycopg2.connect = psycopg2.connect(
            dbname=self.database_name,
            user=self.database_user,
            password=self.database_password,
            host=self.database_host,
        )

        self.database_cursor: psycopg2._psycopg.cursor = (
            self.database_connection.cursor()
        )

        self.create_table(
            "players",
            f"id SERIAL PRIMARY KEY, name VARCHAR({PLAYERS_NAME_MAX_LENGTH}) NOT NULL",
        )
        self.create_table(
            "leaderboard",
            "id SERIAL PRIMARY KEY, player_id INT REFERENCES players(id) ON DELETE CASCADE, score INT NOT NULL, time_played TIMESTAMP NOT NULL",
        )
        self.create_table(
            "score_history",
            "id SERIAL PRIMARY KEY, player_id INT REFERENCES players(id) ON DELETE CASCADE, score INT NOT NULL, time_played TIMESTAMP NOT NULL",
        )
        self.create_table(
            "achievements",
            f"id SERIAL PRIMARY KEY, name VARCHAR({ACHIEVEMENTS_NAME_MAX_LENGTH}) NOT NULL, description TEXT NOT NULL",
        )
        self.create_table(
            "player_achievements",
            "id SERIAL PRIMARY KEY, player_id INT REFERENCES players(id) ON DELETE CASCADE, achievement_id INT REFERENCES achievements(id) ON DELETE CASCADE, date_earned TIMESTAMP NOT NULL",
        )

    def __del__(self: object):
        # self.commit()
        self.database_cursor.close()
        self.database_connection.close()
        print("💾 Database connection closed.")

    def commit(self: object) -> None:
        self.database_connection.commit()

    def create_table(self: object, table_name: str, columns: str) -> None:
        self.database_cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
        )

    def create_player(self: object, name: str) -> None:
        self.database_cursor.execute(
            f"INSERT INTO players (name) VALUES ('{name}') ON CONFLICT DO NOTHING;"
        )

    def read_player(self: object, name: str) -> str:
        self.database_cursor.execute(f"SELECT * FROM players WHERE name = '{name}';")
        player = self.database_cursor.fetchone()

        return player

    def update_player(self: object, name: str, new_name: str) -> None:
        self.database_cursor.execute(
            f"UPDATE players SET name = '{new_name}' WHERE name = '{name}';"
        )

    def delete_player(self: object, name: str) -> None:
        self.database_cursor.execute(f"DELETE FROM players WHERE name = '{name}';")

    def select_all_players(self: object) -> None:
        self.database_cursor.execute("SELECT * FROM players;")
        players = self.database_cursor.fetchall()
        for player in players:
            print(player)

    def show_all_tables(self: object) -> None:
        self.database_cursor.execute(
            """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public';
            """
        )
        tables = self.database_cursor.fetchall()
        for table in tables:
            print(table[0])
