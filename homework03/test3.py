import pygame
import sys


def terminate():
    pygame.quit()
    sys.exit()


class MainWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('XD')

    def render(self, radius):

        pygame.draw.circle(self.screen, pygame.Color((100, 100, 100)), (int(self.width) // 2, int(self.height) // 2),
                           radius)

    def run(self):
        running = True
        fps = 100
        pygame.init()
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((255, 255, 255))
            a = 0
            b = 100
            c = 1
            for i in range(a, b, c):
                if i != 99:
                    a, b, c = 0, 100, 1

                if i == 99:
                    a, b, c = 100, 0, -1

                self.render(1 + i)
                pygame.display.flip()
                clock.tick(fps)

        terminate()


if __name__ == '__main__':
    width = 600
    height = 400
    window = MainWindow(width, height)
    window.run()