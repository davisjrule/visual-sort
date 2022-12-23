from visualizer import draw
import pygame
import time


def draw_sort(visualizer, values):

    clearBackground = (visualizer.SIDE_PADDING//2, visualizer.TOP_PADDING, 
				  visualizer.width - visualizer.SIDE_PADDING, 
                  visualizer.height - visualizer.TOP_PADDING)
    
    pygame.draw.rect(visualizer.window, visualizer.BACKGROUND_COLOR, clearBackground)
    
    #visualizer.window.fill(visualizer.BACKGROUND_COLOR)

    for i, value in enumerate(values): 
        x = visualizer.startingX + (i * visualizer.blockWidth)
        y = visualizer.height - ((value - visualizer.minimum) * visualizer.blockHeight)
        color = visualizer.GRADS[i%3]

        pygame.draw.rect(visualizer.window, color, (x, y, visualizer.blockWidth, visualizer.height))
    
    pygame.display.update()
    

def insertion_sort(visualizer):
    values = visualizer.values

    for i in range(1, len(values)):
        clock = pygame.time.Clock()
        clock.tick(10)

        element = values[i]
        j = i-1

        while j >= 0 and element < values[j]:
            values[j+1] = values[j]
            j = j - 1
        
        # place chosen element after the element just smaller than it
        values[j+1] = element

        draw_sort(visualizer, values)
        #time.sleep(0.1)
        #pygame.display.update()

    return values



# bubble

# merge

# quick

# selection