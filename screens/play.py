import pygame

from screens.resources.player import Player
from screens.screen import Screen

LOGIN: int = 0
MAIN_MENU: int = 1
PLAY: int = 2
LEADERBOARD: int = 3
PROFILE: int = 4
LOGOUT: int = 5
QUIT: int = 6
GAME_OVER: int = 7

ANTIALIAS: bool = True
WHITE_COLOR: tuple = (255, 255, 255)
BLACK_COLOR: tuple = (0, 0, 0)

SCORE_TEXT: str = "Score: "
SCORE_FONT_SIZE: int = 25
SCORE_X: int = 42
SCORE_Y: int = 24
SCORE_COLOR: tuple = (242, 242, 142)

GAME_OVER_MESSAGE_TEXT: str = "Press space to continue..."
GAME_OVER_MESSAGE_FONT_SIZE: int = 25
GAME_OVER_MESSAGE_COLOR: tuple = (242, 242, 142)


class Play(Screen):
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

        self.score_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/Adventure_ReQuest.ttf", SCORE_FONT_SIZE
        )
        self.game_over_title_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/Adventure_ReQuest.ttf", SCORE_FONT_SIZE
        )
        self.game_over_message_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/Adventure_ReQuest.ttf", SCORE_FONT_SIZE
        )

        self.player: Player = Player(
            x=self.win.get_width() // 2,
            y=self.win.get_height() // 2,
            display_width=self.win.get_width(),
            display_height=self.win.get_height(),
            assets_dir=self.assets_dir,
        )

        self.score: int = 0
        self.game_over: bool = False

    def run(self: object) -> int:
        self.score = 0

        clock: pygame.time.Clock = pygame.time.Clock()
        keep_running: bool = True
        return_state: int = MAIN_MENU

        while keep_running:
            clock.tick(self.framerate)

            if self.game_over == False:
                self.player.check_movement()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_running = False
                    return_state = QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keep_running = False
                        return_state = MAIN_MENU
                    if event.key == pygame.K_SPACE:
                        if self.game_over == False:
                            self.player.shoot()

            for bullet in self.player.bullets:
                if bullet.off_screen(self.win):
                    self.player.bullets.pop(self.player.bullets.index(bullet))
                else:
                    bullet.move()

            if keep_running == True:
                self.draw()

        return return_state

    def draw(self: object) -> None:
        self.draw_background()
        self.draw_bullets()
        self.draw_player()
        self.draw_score()
        self.draw_game_over()

        pygame.display.update()

    def draw_background(self: object) -> None:
        self.win.blit(self.background, (0, 0))

    def draw_player(self: object) -> None:
        self.player.draw(self.win)

    def draw_bullets(self: object) -> None:
        for bullet in self.player.bullets:
            bullet.draw(self.win)

    def draw_score(self: object) -> None:
        score_text: str = f"{SCORE_TEXT}{self.score}"

        text: pygame.Surface = self.score_font.render(
            score_text, ANTIALIAS, WHITE_COLOR
        )

        self.win.blit(text, (SCORE_X, SCORE_Y))
        self.score += 1

    def draw_game_over(self: object) -> None:
        if self.score > 1000:
            self.game_over = True
            rect_width: int = 450
            rect_height: int = 230
            rect_radius: int = 20
            rect_x: int = self.win.get_width() // 2 - rect_width // 2
            rect_y: int = 250
            rect_color: tuple = (0, 0, 0)
            rect_alpha: int = 128

            self.draw_rounded_rect(
                self.win,
                rect_x,
                rect_y,
                rect_width,
                rect_height,
                rect_radius,
                rect_color,
                rect_alpha,
            )

            self.win.blit(self.game_over_image, (0, 0))

            message_text: str = GAME_OVER_MESSAGE_TEXT
            text: pygame.Surface = self.game_over_message_font.render(
                message_text, ANTIALIAS, GAME_OVER_MESSAGE_COLOR
            )
            message_x: int = self.win.get_width() // 2 - text.get_width() // 2
            message_y: int = 400
            self.win.blit(text, (message_x, message_y))
