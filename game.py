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
        main_menu_border: pygame.Surface,
        main_menu_none_selected: pygame.Surface,
        main_menu_play_selected: pygame.Surface,
        main_menu_highscore_selected: pygame.Surface,
        main_menu_profile_selected: pygame.Surface,
        main_menu_quit_selected: pygame.Surface,
        main_font: pygame.font.Font,
    ) -> None:

        PLAYER_INITAL_X: int = DISPLAY_WIDTH // 2
        PLAYER_INITAL_Y: int = DISPLAY_HEIGHT // 2

        self.background_image: pygame.Surface = background_image
        self.player_rocket: pygame.Surface = player_rocket
        self.game_over_image: pygame.Surface = game_over

        self.menu_background: pygame.Surface = menu_background
        self.main_menu_border: pygame.Surface = main_menu_border
        self.main_menu_none_selected: pygame.Surface = main_menu_none_selected
        self.main_menu_play_selected: pygame.Surface = main_menu_play_selected
        self.main_menu_highscore_selected: pygame.Surface = main_menu_highscore_selected
        self.main_menu_profile_selected: pygame.Surface = main_menu_profile_selected
        self.main_menu_quit_selected: pygame.Surface = main_menu_quit_selected

        self.menu_background_offset: int = 0

        self.main_font: pygame.font.Font = main_font

        self.screen_width: int = DISPLAY_WIDTH
        self.screen_height: int = DISPLAY_HEIGHT
        self.framerate: int = FRAMERATE

        self.keep_running: bool = True
        self.game_over: bool = False
        self.state: int = MAIN_MENU
        self.menu_state: int = PLAY

        self.score: int = 0

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

            keys: pygame.key = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.keep_running = False
            # if keys[pygame.K_BACKSPACE]:
            #     self.player.kill()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.keep_running = False
                if self.state == MAIN_MENU:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            self.menu_state -= 1
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            self.menu_state += 1
                        elif event.key == pygame.K_p:
                            self.state = PLAY
                        elif event.key == pygame.K_h:
                            self.state = HIGHSCORES
                        elif event.key == pygame.K_f:
                            self.state = PROFILE
                        elif event.key == pygame.K_q:
                            self.keep_running = False
                        elif (
                            event.key == pygame.K_RETURN or event.key == pygame.K_SPACE
                        ):
                            self.state = self.menu_state
                    if self.menu_state < PLAY:
                        self.menu_state = QUIT
                    elif self.menu_state > QUIT:
                        self.menu_state = PLAY

                if not self.player.alive():
                    self.keep_running = False
                    self.game_over = True

            if self.state == MAIN_MENU:
                self.draw_main_menu()
            elif self.state == PLAY:
                self.draw_play()

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
        self.win.blit(resized_image, (0, self.menu_background_offset))
        self.win.blit(
            resized_image, (0, self.menu_background_offset - self.screen_height)
        )
        self.win.blit(self.main_menu_border, (0, 0))
        if self.menu_state == PLAY:
            self.win.blit(self.main_menu_play_selected, (0, 0))
        elif self.menu_state == HIGHSCORES:
            self.win.blit(self.main_menu_highscore_selected, (0, 0))
        elif self.menu_state == PROFILE:
            self.win.blit(self.main_menu_profile_selected, (0, 0))
        elif self.menu_state == QUIT:
            self.win.blit(self.main_menu_quit_selected, (0, 0))

        pygame.display.update()
        self.menu_background_offset += 1
        if self.menu_background_offset > self.screen_height:
            self.menu_background_offset = 0

    def draw_play(self: object) -> None:
        self.win.blit(self.background_image, (0, 0))

        self.player.draw(self.win)
        self.draw_score()

        if self.game_over:
            self.game_over_screen()

        pygame.display.update()

    def game_over_screen(self: object) -> None:
        self.win.blit(self.game_over_image, (0, 0))

    def draw_score(self: object) -> None:
        score_text: str = f"Score: {self.score}"

        text: pygame.Surface = self.main_font.render(score_text, ANTIALIAS, WHITE_COLOR)
        text_rect: pygame.Rect = text.get_rect()
        text_rect.center = (SCORE_X, SCORE_Y)

        self.win.blit(text, text_rect)
        self.score += 1
