import sorts
import math
import pandas as pd
import numpy as np
import pygame

pygame.init()

N = 50  # global variable representing array size
MIN = 1
MAX = 101  # exclusive

# RETURNS: a randomly generated array of integers
#          such that range = valRange and size = n
def generate_array():
    randArray = np.random.randint(low=MIN, high=MAX, size=N)
    return randArray


class Visualizer:

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GRADS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]

    FONT = pygame.font.SysFont("arial", 20)
    LARGE_FONT = pygame.font.SysFont("arial", 40)

    BACKGROUND_COLOR = WHITE

    SIDE_PADDING = 100
    TOP_PADDING = 150

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")

    def create_values(self):
        # generate array randomly
        self.values = generate_array()
        self.minimum = 0
        self.maximum = max(self.values)

        self.blockWidth = round((self.width - self.SIDE_PADDING) / len(self.values))
        self.blockHeight = math.floor(
            (self.height - self.TOP_PADDING) / (self.maximum - self.minimum)
        )
        self.startingX = self.SIDE_PADDING // 2


def draw(visualizer):
    visualizer.window.fill(visualizer.BACKGROUND_COLOR)

    controls = visualizer.FONT.render(
        "R - Reset | A - Ascending | D - Descending", 1, visualizer.BLACK
    )
    visualizer.window.blit(
        controls, (visualizer.width / 2 - controls.get_width() / 2, 45)
    )

    sortType = visualizer.FONT.render(
        "I - Insertion Sort | B - Bubble Sort", 1, visualizer.BLACK
    )
    visualizer.window.blit(
        sortType, (visualizer.width / 2 - sortType.get_width() / 2, 75)
    )

    draw_values(visualizer)
    pygame.display.update()


def draw_values(visualizer):
    values = visualizer.values

    for i, value in enumerate(values):
        x = visualizer.startingX + (i * visualizer.blockWidth)
        y = visualizer.height - ((value - visualizer.minimum) * visualizer.blockHeight)
        color = visualizer.GRADS[i % 3]

        pygame.draw.rect(
            visualizer.window, color, (x, y, visualizer.blockWidth, visualizer.height)
        )


def main():
    running = True
    clock = pygame.time.Clock()

    visualizer = Visualizer(800, 600)
    visualizer.create_values()

    while running:
        clock.tick(20)
        draw(visualizer)

        # visualizer.create_values()
        # time.sleep(0.1)

        for event in pygame.event.get():

            # check for quit event
            if event.type == pygame.QUIT:
                running = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                visualizer.create_values()

            if event.key == pygame.K_i:
                sorts.insertion_sort(visualizer)


if __name__ == "__main__":
    main()
