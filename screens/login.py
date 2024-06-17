import pygame


class Login:
    def __init__(
        self: object, win: pygame.Surface, screen_width: int, screen_height: int
    ) -> None:
        self.win: pygame.Surface = win
        self.screen_width: int = screen_width
        self.screen_height: int = screen_height

        font: pygame.font.Font = pygame.font.Font(None, 32)
        screen_text: str = f"LOGIN SCREEN"
        text: pygame.Surface = font.render(screen_text, True, (255, 255, 255))
        text_rect: pygame.Rect = text.get_rect()
        text_rect.center = (142, 142)
        self.win.blit(text, text_rect)

        pygame.display.update()
