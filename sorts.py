from visualizer import draw
import pygame


def draw_sort(visualizer, values, colorIndices):

    clearBackground = (
        visualizer.SIDE_PADDING // 2,
        visualizer.TOP_PADDING,
        visualizer.width - visualizer.SIDE_PADDING,
        visualizer.height - visualizer.TOP_PADDING,
    )

    pygame.draw.rect(visualizer.window, visualizer.BACKGROUND_COLOR, clearBackground)

    for i, value in enumerate(values):
        x = visualizer.startingX + (i * visualizer.blockWidth)
        y = visualizer.height - ((value - visualizer.minimum) * visualizer.blockHeight)
        color = visualizer.GRADS[i % 3]

        if i in colorIndices:
            color = colorIndices[i]

        pygame.draw.rect(
            visualizer.window, color, (x, y, visualizer.blockWidth, visualizer.height)
        )

    pygame.display.update()


def insertion_sort(visualizer):
    values = visualizer.values

    for i in range(1, len(values)):
        clock = pygame.time.Clock()

        element = values[i]

        while True:
            if not (i > 0 and element < values[i - 1]):
                break

            values[i] = values[i - 1]
            i = i - 1
            values[i] = element

            colorIndices = {i - 1: visualizer.RED, i: visualizer.GREEN}
            clock.tick(25)
            draw_sort(visualizer, values, colorIndices)

    return values


# bubble

# merge

# quick

# selection
