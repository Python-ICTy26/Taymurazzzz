import pygame
import sys


def terminate():
    pygame.quit()
    sys.exit()


class MainWindow:
    def __init__(self, width, height, radius):
        self.width = width
        self.height = height
        self.radius = radius

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('XD')

    def render(self):

        pygame.draw.circle(self.screen, pygame.Color((100, 100, 100)), (int(self.width) // 2, int(self.height) // 2), radius)

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
            self.render()
            pygame.display.flip()
            clock.tick(fps)
        terminate()


if __name__ == '__main__':
    width = 600
    height = 400
    radius = 1
    window = MainWindow(width, height, radius)
    window.run()





