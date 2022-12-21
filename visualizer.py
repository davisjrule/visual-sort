import time
import pandas as pd
import numpy as np
import pygame
pygame.init()

N = 10   # global variable representing array size
MIN = 1
MAX = 10

# RETURNS: a randomly generated array of integers
#          such that range = valRange and size = n
def generate_array():
    randArray = np.random.randint(low=MIN, high=MAX, size=N)
    return randArray


class Visualizer: 
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BACKGROUND_COLOR = WHITE

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = generate_array()
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")


def draw(visualizer):
    visualizer.window.fill(visualizer.BACKGROUND_COLOR)

    pygame.display.update()


def main():
    running = True
    clock = pygame.time.Clock()

    visualizer = Visualizer(800, 600)

    while running:

        draw(visualizer)
        
        for event in pygame.event.get():

            # check for quit event
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()