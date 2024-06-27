import pygame

from constants import *
from screens.screen import Screen

# from database import Database


class Login(Screen):
    def __init__(
        self: object,
        win: pygame.Surface,
        assets_dir: str,
        framerate: int,
    ) -> None:
        self.win: pygame.Surface = win
        self.assets_dir: str = assets_dir
        self.framerate: int = framerate
        self.user_text: str = ""
        self.input_box = pygame.Rect(280, 285, 200, 40)
        # self.database: Database = Database()

        self.background: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/full_background.png"
        )
        self.background_square: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/background_square.png"
        )
        self.astronaut: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/astronauta.png"
        )
        self.main_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/Adventure_ReQuest.ttf", 49
        )
        self.contratados_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 19
        )
        self.name_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 32
        )
        self.input_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 32
        )

        self.background_image_width: int = self.background.get_width()

        self.menu_background_offset: int = 0

    def run(self: object) -> int:
        input_active = True
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return QUIT
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return QUIT

            #         if event.type == pygame.KEYDOWN and input_active:
            #             if event.key == pygame.K_RETURN:
            #                 print(f"Texto inserido: {self.user_text}")
            #                 if len(self.user_text):
            #                     # if self.database.read_player(self.user_text) is None:
            #                     #     self.database.create_player(self.user_text)
            #                     #     self.database.commit()
            #                     input_active = False  # Sai do modo de entrada
            #                     self.user_text = ""
            #                     running = False
            #             elif event.key == pygame.K_BACKSPACE:
            #                 self.user_text = self.user_text[
            #                     :-1
            #                 ]  # Remove o último caractere
            #             else:
            #                 if len(self.user_text) < 8:
            #                     self.user_text += event.unicode
            if running:
                self.draw()

        return MAIN_MENU

    def draw(self: object) -> None:
        self.background_square.set_alpha(75)
        self.win.blit(self.background, (self.menu_background_offset, 0))
        self.win.blit(
            self.background,
            (self.menu_background_offset + self.background_image_width, 0),
        )
        self.win.blit(self.background_square, (0, 0))
        self.win.blit(self.astronaut, (0, 430))

        rect_width: int = 359
        rect_height: int = 260
        rect_radius: int = 20
        rect_x: int = self.win.get_width() // 2 - rect_width // 2
        rect_y: int = 140
        rect_color: tuple = BLUE
        rect_alpha: int = 183

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

        self.draw_border()
        self.draw_contratados()
        self.draw_input()

        pygame.display.update()

    def draw_border(self: object) -> None:
        login_text: str = "ABC | 42"
        login_text2: str = "Asteroids"
        name_text: str = "Name:"

        text: pygame.Surface = self.main_font.render(login_text, True, (255, 255, 0, 1))
        text2: pygame.Surface = self.main_font.render(
            login_text2, True, (255, 255, 0, 1)
        )
        text3: pygame.Surface = self.name_font.render(
            name_text, True, (255, 255, 250, 250)
        )

        self.win.blit(text, (215, 150))
        self.win.blit(text2, (186, 200))
        self.win.blit(text3, (180, 292))

    def draw_contratados(self: object) -> None:
        text: str = "#CONTRATADOS"

        text: pygame.Surface = self.contratados_font.render(text, True, WHITE)
        self.win.blit(text, (50, 35))

    def draw_input(self: object) -> None:
        text_surface = self.input_font.render(self.user_text, True, WHITE)
        self.win.blit(text_surface, (286, 288))

        # Desenha a caixa de input
        pygame.draw.rect(self.win, (255, 255, 255), self.input_box, 2)
