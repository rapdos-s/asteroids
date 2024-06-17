import pygame

from screens.resources.player import Player

ANTIALIAS: bool = True
WHITE_COLOR: tuple = (255, 255, 255)
BLACK_COLOR: tuple = (0, 0, 0)

SCORE_FONT_SIZE: int = 25
SCORE_X: int = 100
SCORE_Y: int = 50

PLAYER_INITAL_X: int = 100
PLAYER_INITAL_Y: int = 100


class Play:
    def __init__(
        self: object, win: pygame.Surface, assets_dir: str, framerate: int
    ) -> None:
        self.win: pygame.Surface = win
        self.assets_dir: str = assets_dir
        self.framerate = framerate

        self.background: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/background.png"
        )
        self.game_over_image: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/game_over.png"
        )
        self.main_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/Adventure_ReQuest.ttf", SCORE_FONT_SIZE
        )

        self.player: Player = Player(
            PLAYER_INITAL_X,
            PLAYER_INITAL_Y,
            640,
            640,
            self.assets_dir,
        )

        self.score: int = 0

    def run(self: object) -> int:
        clock: pygame.time.Clock = pygame.time.Clock()
        keep_running: bool = True

        while keep_running:
            clock.tick(self.framerate)
            self.draw()

        return 6  # QUIT

    def draw(self: object) -> None:
        self.draw_background()
        self.draw_player()
        self.draw_score()
        self.draw_game_over()

        pygame.display.update()

    def draw_background(self: object) -> None:
        self.win.blit(self.background, (0, 0))

    def draw_player(self: object) -> None:
        self.player.draw(self.win)

    def draw_score(self: object) -> None:
        score_text: str = f"Score: {self.score}"

        text: pygame.Surface = self.main_font.render(score_text, ANTIALIAS, WHITE_COLOR)

        self.win.blit(text, (SCORE_X, SCORE_Y))
        self.score += 1

    def draw_game_over(self: object) -> None:
        if self.score > 50:
            self.win.blit(self.game_over_image, (0, 0))
