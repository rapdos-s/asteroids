import pygame

from player import Player

DISPLAY_WIDTH: int = 640
DISPLAY_HEIGHT: int = 640
FRAMERATE: int = 60

WHITE_COLOR: tuple = (255, 255, 255)
BLACK_COLOR: tuple = (0, 0, 0)

MAIN_MENU: int = 0
PLAY: int = 1
HIGHSCORES: int = 2
PROFILE: int = 3
QUIT: int = 4
GAME_OVER: int = 5

ANTIALIAS: bool = True

SCORE_X: int = 100
SCORE_Y: int = 50


class Game:
    def __init__(
        self: object,
        display_caption: str,
        background_image: pygame.Surface,
        player_rocket: pygame.Surface,
        game_over: pygame.Surface,
        menu_background: pygame.Surface,
        main_font: pygame.font.Font,
    ) -> None:

        PLAYER_INITAL_X: int = DISPLAY_WIDTH // 2
        PLAYER_INITAL_Y: int = DISPLAY_HEIGHT // 2

        self.background_image: pygame.Surface = background_image
        self.player_rocket: pygame.Surface = player_rocket
        self.game_over_image: pygame.Surface = game_over
        self.menu_background: pygame.Surface = menu_background

        self.menu_background_offset: int = 0

        self.main_font: pygame.font.Font = main_font

        self.screen_width: int = DISPLAY_WIDTH
        self.screen_height: int = DISPLAY_HEIGHT
        self.framerate: int = FRAMERATE

        self.keep_running: bool = True
        self.game_over: bool = False
        self.state: int = MAIN_MENU
        self.state = PLAY

        self.player: Player = Player(
            self.player_rocket,
            PLAYER_INITAL_X,
            PLAYER_INITAL_Y,
            self.screen_width,
            self.screen_height,
        )

        self.display_caption: str = display_caption
        pygame.display.set_caption(self.display_caption)

        self.win = pygame.display.set_mode((self.screen_width, self.screen_height))

    def run(self: object) -> None:
        print("🚀 Running Asteroids' game!")

        clock: pygame.time.Clock = pygame.time.Clock()
        while self.keep_running:
            clock.tick(self.framerate)

            # if not self.game_over:

            #     for bullet in self.player.bullets:
            #         bullet.move()

            keys: pygame.key = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.keep_running = False
            if keys[pygame.K_BACKSPACE]:
                self.player.kill()

                # self.player.shoot()  # This is a temporary solution to test the bullets

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.keep_running = False
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_SPACE:
                #         if not self.game_over:
                #             self.player.shoot()
                if not self.player.alive():
                    # self.keep_running = False
                    self.game_over = True

            if self.state == MAIN_MENU:
                self.draw_main_menu()
            elif self.state == PLAY:
                self.draw_play()
                if not self.game_over:
                    if keys[pygame.K_UP] or keys[pygame.K_w]:
                        self.player.move_forward()
                    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                        self.player.turn_left()
                    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                        self.player.turn_right()

        # [P] PLAY
        # [H] HIGHSCORES
        # [F] PROFILE
        # [Q] QUIT

        if self.game_over:
            print("💥 Game Over!")
        elif not self.keep_running:
            print("🏁 Game Closed.")
        else:
            print("❔ Game Ended with unknown reason!")

    def draw_main_menu(self: object) -> None:
        resized_image = pygame.transform.scale(
            self.menu_background, (self.screen_width, self.screen_height)
        )
        self.win.blit(resized_image, (self.menu_background_offset, 0))
        pygame.display.update()
        self.menu_background_offset -= 1

    def draw_play(self: object) -> None:
        self.win.blit(self.background_image, (0, 0))

        self.player.draw(self.win)
        self.draw_score()

        # for bullet in self.player.bullets:
        # bullet.draw(self.win)

        if self.game_over:
            self.game_over_screen()

        pygame.display.update()

    def game_over_screen(self: object) -> None:
        self.win.blit(self.game_over_image, (0, 0))

    def draw_score(self: object) -> None:
        foo: str = "Score: 0"

        text: pygame.Surface = self.main_font.render(foo, ANTIALIAS, WHITE_COLOR)
        text_rect: pygame.Rect = text.get_rect()
        text_rect.center = (SCORE_X, SCORE_Y)

        self.win.blit(text, text_rect)
