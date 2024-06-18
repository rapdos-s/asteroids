import psycopg2

# from game import Game


def database_shenanigans() -> None:
    print("💾 Setting up psycopg2 connection")

    # Configuração de acesso ao Banco, deve ser feito depois via .env
    db_name: str = "db_asteroids"
    db_user: str = "marvin"
    db_password: str = "F0rty_Tw0"
    db_host: str = "localhost"

    # Conexão com o Banco
    db_connection: psycopg2.connect = psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=db_host
    )

    # Cursor do banco de dados
    db_cursor: psycopg2._psycopg.cursor = db_connection.cursor()

    # Criação das tabelas
    db_cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            name VARCHAR(5) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS leaderboard (
            id SERIAL PRIMARY KEY,
            player_id INT REFERENCES players(id),
            score INT NOT NULL,
            time_played TIMESTAMP NOT NULL
        );
        CREATE TABLE IF NOT EXISTS score_history (
            id SERIAL PRIMARY KEY,
            player_id INT REFERENCES players(id),
            score INT NOT NULL,
            time_played TIMESTAMP NOT NULL
        );
        CREATE TABLE IF NOT EXISTS achievements (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            description TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS player_achievements (
            id SERIAL PRIMARY KEY,
            player_id INT REFERENCES players(id),
            achievement_id INT REFERENCES achievements(id),
            date_earned TIMESTAMP NOT NULL
        );
        """
    )

    # teste inserindo um player
    db_cursor.execute(
        """
        INSERT INTO players (name) VALUES ('duck');
        """
    )

    # teste inserindo um score
    db_cursor.execute(
        """
        INSERT INTO leaderboard (player_id, score, time_played) VALUES (1, 100, '2021-09-07 00:00:00');
        """
    )

    # consultando os dados
    db_cursor.execute(
        """
        SELECT players.name, leaderboard.score, leaderboard.time_played
        FROM players
        JOIN leaderboard ON players.id = leaderboard.player_id;
        """
    )
    player_name: str = db_cursor.fetchone()[0]
    player_score: int = db_cursor.fetchone()[1]
    player_score_date: str = db_cursor.fetchone()[2]
    print(f"Player: {player_name} | Score: {player_score} | Date: {player_score_date}")

    # Commit das alterações
    db_connection.commit()

    # Fechamento da conexão
    db_cursor.close()
    db_connection.close()

    print("💾 Database is ready!")


if __name__ == "__main__":
    print("🚀 ABC | 42 Asteroids 🌑")

    database_shenanigans()

    # game: Game = Game()

    # print("🎮 Asteroids' game is ready!")
    # game.run()

    print("🌌 Everything is done, Bye!")
