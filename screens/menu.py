import pygame

LOGIN: int = 0
MAIN_MENU: int = 1
PLAY: int = 2
HIGHSCORES: int = 3
PROFILE: int = 4
LOGOUT: int = 5
QUIT: int = 6
GAME_OVER: int = 7


class Menu:
    def __init__(
        self: object,
        win: pygame.Surface,
        screen_width: int,
        assets_dir: str,
        framerate: int,
    ) -> None:
        self.win: pygame.Surface = win
        self.screen_width: int = screen_width
        self.assets_dir: str = assets_dir
        self.framerate = framerate

        self.border: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_border.png"
        )
        self.background: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/full_background.png"
        )
        self.main_menu_play_selected: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_play_selected.png"
        )
        self.main_menu_highscore_selected: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_highscore_selected.png"
        )
        self.main_menu_profile_selected: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_profile_selected.png"
        )
        self.main_menu_logout_selected: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_logout_selected.png"
        )
        self.main_menu_quit_selected: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_quit_selected.png"
        )

        self.background_image_width: int = self.background.get_width()

        self.menu_background_offset: int = 0

        self.menu_state: int = PLAY

    def run(self: object) -> int:
        selected: bool = False

        clock: pygame.time.Clock = pygame.time.Clock()
        while not selected:
            clock.tick(self.framerate)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.keep_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.menu_state -= 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.menu_state += 1
                    elif event.key == pygame.K_RETURN:
                        selected = True
                    elif event.key == pygame.K_ESCAPE:
                        selected = True
                        self.menu_state = QUIT

            if self.menu_state < PLAY:
                self.menu_state = QUIT
            elif self.menu_state > QUIT:
                self.menu_state = PLAY

            self.draw()

        return self.menu_state

    def draw(self: object) -> None:
        self.win.blit(self.background, (self.menu_background_offset, 0))
        self.win.blit(
            self.background,
            (self.menu_background_offset + self.background_image_width, 0),
        )

        if self.menu_state == PLAY:
            self.win.blit(self.main_menu_play_selected, (0, 0))
        elif self.menu_state == HIGHSCORES:
            self.win.blit(self.main_menu_highscore_selected, (0, 0))
        elif self.menu_state == PROFILE:
            self.win.blit(self.main_menu_profile_selected, (0, 0))
        elif self.menu_state == LOGOUT:
            self.win.blit(self.main_menu_logout_selected, (0, 0))
        elif self.menu_state == QUIT:
            self.win.blit(self.main_menu_quit_selected, (0, 0))

        self.win.blit(self.border, (0, 0))

        pygame.display.update()

        self.menu_background_offset -= 1
        if self.menu_background_offset < 0 - self.background_image_width:
            self.menu_background_offset = 0
