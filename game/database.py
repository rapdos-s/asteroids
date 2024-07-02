from dotenv import load_dotenv
from constants import *

import psycopg2
import os


class Database:
    """
        Classe Database é responsável por estabelecer uma conexão com um banco de dados PostgreSQL.
    """
    def __init__(self: object):
        """
            Método construtor que inicializa uma conexão com o banco de dados PostgreSQL utilizando as credenciais carregadas de um arquivo .env
            :param self: Instância da classe Database
        """
        print("💾 Database connection opened.")
        load_dotenv()

        self.database_name: str = os.getenv("POSTGRES_DB")
        self.database_user: str = os.getenv("POSTGRES_USER")
        self.database_password: str = os.getenv("POSTGRES_PASSWORD")
        self.database_host: str = os.getenv("POSTGRES_HOST")
        self.database_port: str = os.getenv("POSTGRES_PORT")

        self.database_connection: psycopg2.connect = psycopg2.connect(
            dbname=self.database_name,
            user=self.database_user,
            password=self.database_password,
            host=self.database_host,
            port=self.database_port,
        )

        self.database_cursor: psycopg2._psycopg.cursor = (
            self.database_connection.cursor()
        )

    def __del__(self: object) -> None:
        """
            Método destrutor que fecha a conexão com o banco de dados PostgreSQL.

            Args:
                Instância da classe Database

            Returns:
                None: Este método não retorna nada.
        """
        # self.commit()
        self.database_cursor.close()
        self.database_connection.close()
        print("💾 Database connection closed.")

    def commit(self: object) -> None:
        """
            Método que realiza o commit de uma transação no banco de dados.

            Args:
                Instância da classe Database

            Returns:
                None: Este método não retorna nada.
        """
        self.database_connection.commit()

    # CRUD players #############################################################
    def create_player(self: object, player_name: str) -> None:
        """
        Insere um novo jogador no banco de dados.

        Args:
            player_name (str): O nome do jogador a ser inserido.

        Returns:
            None: Este método não retorna nada.
        """
        self.database_cursor.execute(
            f"INSERT INTO players (player_name) VALUES ('{player_name}') ON CONFLICT DO NOTHING;"
        )


    def read_player_by_id(self: object, player_id: int) -> str:
        """
        Lê um jogador do banco de dados pelo ID.
        
        Args:
            player_id (int): O ID do jogador a ser lido.

        Returns:
            str: Uma string contendo as informações do jogador.
        """
        self.database_cursor.execute(f"SELECT * FROM players WHERE id = {player_id};")
        player = self.database_cursor.fetchone()

        return player

    def read_player_by_name(self: object, player_name: str) -> str:
        """
        Lê um jogador do banco de dados pelo nome.

        Args:
            player_name (str): O nome do jogador a ser lido.

        Returns:
            str: Uma string contendo as informações do jogador.
        """
        self.database_cursor.execute(
            f"SELECT * FROM players WHERE player_name = '{player_name}';"
        )
        player = self.database_cursor.fetchone()

        return player

    def update_player_by_id(self: object, player_id: int, new_player_name: str) -> None:
        """
        Atualiza um jogador no banco de dados pelo ID.

        Args:
            player_id (int): O ID do jogador a ser atualizado.
            new_player_name (str): O novo nome do jogador.

        Returns:
            None: Este método não retorna nada.
        """
        self.database_cursor.execute(
            f"UPDATE players SET player_name = '{new_player_name}' WHERE id = {player_id};"
        )

    def update_player_by_name(
        self: object, player_name: str, new_player_name: str
    ) -> None:
        """
        Atualiza um jogador no banco de dados pelo nome.

        Args:
            player_name (str): O nome do jogador a ser atualizado.
            new_player_name (str): O novo nome do jogador.

        Returns:
            None: Este método não retorna nada.
        """
        self.database_cursor.execute(
            f"UPDATE players SET player_name = '{new_player_name}' WHERE player_name = '{player_name}';"
        )

    def delete_player_by_id(self: object, player_id: int) -> None:
        """
        Deleta um jogador do banco de dados pelo ID.

        Args:
            player_id (int): O ID do jogador a ser deletado.

        Returns:
            None: Este método não retorna nada.
        """
        self.database_cursor.execute(f"DELETE FROM players WHERE id = {player_id};")


    """
    Deleta um jogador do banco de dados pelo nome.

    Args:
        player_name (str): O nome do jogador a ser deletado.

    Returns:
        None: Este método não retorna nada.
    """
    def delete_player_by_name(self: object, player_name: str) -> None:
        self.database_cursor.execute(
            f"DELETE FROM players WHERE player_name = '{player_name}';"
        )

    # Selects ##################################################################

    """
    Seleciona todos os jogadores do banco de dados.

    Returns:
        None: Este método não retorna nada.
    """
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

    """
    Seleciona todos os jogadores do banco de dados.

    Returns:
        None: Este método não retorna nada.
    """
    def select_all_players(self: object) -> None:
        self.database_cursor.execute("SELECT * FROM players;")
        players = self.database_cursor.fetchall()
        for player in players:
            print(player)

    """
    Seleciona todos os jogadores do banco de dados.
    
    Returns:
        None: Este método não retorna nada.
    """
    def select_all_leaderboard(self: object) -> None:
        self.database_cursor.execute("SELECT * FROM leaderboard;")
        leaderboard = self.database_cursor.fetchall()
        for score in leaderboard:
            print(score)

    """
    Seleciona todos os jogadores do banco de dados.

    Returns:
        None: Este método não retorna nada.
    """
    def select_all_score_history(self: object) -> None:
        self.database_cursor.execute("SELECT * FROM score_history;")
        score_history = self.database_cursor.fetchall()
        for score in score_history:
            print(score)

    """
    Seleciona todos os jogadores do banco de dados.

    Returns:
        None: Este método não retorna nada.
    """
    def select_all_achievements(self: object) -> None:
        self.database_cursor.execute("SELECT * FROM achievements ORDER BY id;")
        achievements = self.database_cursor.fetchall()
        for achievement in achievements:
            print(achievement)

    """
    Seleciona todos os jogadores do banco de dados.

    Returns:
        None: Este método não retorna nada.
    """
    def select_all_player_achievements(self: object) -> None:
        self.database_cursor.execute("SELECT * FROM player_achievements;")
        player_achievements = self.database_cursor.fetchall()
        for player_achievement in player_achievements:
            print(player_achievement)
