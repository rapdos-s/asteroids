import pygame

LOGIN: int = 0
MAIN_MENU: int = 1
PLAY: int = 2
HIGHSCORES: int = 3
PROFILE: int = 4
QUIT: int = 5
GAME_OVER: int = 6

class Menu:
    def __init__(self: object, win: pygame.Surface, screen_width: int, assets_dir: str) -> None:
        self.win: pygame.Surface = win
        self.screen_width: int = screen_width
        self.assets_dir: str = assets_dir

        self.border: pygame.Surface = pygame.image.load(f"{self.assets_dir}/main_menu_border.png")
        self.background: pygame.Surface = pygame.image.load(f"{self.assets_dir}/full_background.png")
        self.main_menu_play_selected: pygame.Surface = pygame.image.load(f"{self.assets_dir}/main_menu_play_selected.png")
        self.main_menu_highscore_selected: pygame.Surface = pygame.image.load(f"{self.assets_dir}/main_menu_highscore_selected.png")
        self.main_menu_profile_selected: pygame.Surface = pygame.image.load(f"{self.assets_dir}/main_menu_profile_selected.png")
        self.main_menu_quit_selected: pygame.Surface = pygame.image.load(f"{self.assets_dir}/main_menu_quit_selected.png")

        self.background_image_width: int = self.background.get_width()

        self.menu_background_offset: int = 0

        self.menu_state: int = PLAY

    def run(self: object) -> None:
        self.draw()

    def draw(self: object) -> None:
        self.win.blit(self.background, (self.menu_background_offset, 0))
        self.win.blit(self.background, (self.menu_background_offset + self.background_image_width, 0))

        if self.menu_state == PLAY:
            self.win.blit(self.main_menu_play_selected, (0, 0))
        elif self.menu_state == HIGHSCORES:
            self.win.blit(self.main_menu_highscore_selected, (0, 0))
        elif self.menu_state == PROFILE:
            self.win.blit(self.main_menu_profile_selected, (0, 0))
        elif self.menu_state == QUIT:
            self.win.blit(self.main_menu_quit_selected, (0, 0))

        self.win.blit(self.border, (0, 0))

        pygame.display.update()

        self.menu_background_offset -= 1
        if self.menu_background_offset < 0 - self.background_image_width:
            self.menu_background_offset = 0