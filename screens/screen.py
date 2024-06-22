import pygame
import pygame.gfxdraw

from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT


class Screen:
    def draw_rounded_rect(
        self: object,
        win: pygame.Surface,
        x: int,
        y: int,
        width: int,
        height: int,
        radius: int,
        color: tuple,
        alpha: int,
    ) -> None:
        surface: pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)

        pygame.gfxdraw.aacircle(surface, radius, radius, radius, color)
        pygame.gfxdraw.aacircle(surface, width - radius, radius, radius, color)
        pygame.gfxdraw.aacircle(surface, radius, height - radius, radius, color)
        pygame.gfxdraw.aacircle(surface, width - radius, height - radius, radius, color)

        pygame.gfxdraw.filled_circle(surface, radius, radius, radius, color)
        pygame.gfxdraw.filled_circle(surface, width - radius, radius, radius, color)
        pygame.gfxdraw.filled_circle(surface, radius, height - radius, radius, color)
        pygame.gfxdraw.filled_circle(
            surface, width - radius, height - radius, radius, color
        )

        pygame.draw.rect(surface, color, (radius, 0, width - 2 * radius, height))
        pygame.draw.rect(surface, color, (0, radius, width, height - 2 * radius))

        surface.set_alpha(alpha)

        rect: pygame.Rect = surface.get_rect()
        rect.topleft = (x, y)

        self.win.blit(surface, rect)

    def draw_achievements(
        self: object, icon: str, title: str, description: str
    ) -> None:
        # print(f"🎨 icon file: {icon}")
        # print(f"🏆 {title}: {description}")

        width: int = 200
        height: int = 50
        x: int = DISPLAY_WIDTH - width - 10
        y: int = DISPLAY_HEIGHT - height - 10
        radius: int = 10
        color: tuple = (0, 0, 0)
        alpha: int = 128

        self.draw_rounded_rect(self.win, x, y, width, height, radius, color, alpha)
