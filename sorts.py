from visualizer import draw
import pygame

FRAME_RATE = 15

clock = pygame.time.Clock()


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
        element = values[i]

        while True:
            if not (i > 0 and element < values[i - 1]):
                break

            values[i] = values[i - 1]
            i = i - 1
            values[i] = element

            colorIndices = {i - 1: visualizer.RED, i: visualizer.GREEN}
            clock.tick(FRAME_RATE)
            draw_sort(visualizer, values, colorIndices)

    return values


# selection
def selection_sort(visualizer):
    values = visualizer.values

    for i in range(len(values)):

        # min element in remaining unsorted partition
        minInd = i
        for j in range(i + 1, len(values)):
            if values[minInd] > values[j]:
                minInd = j

            colorIndices = {j: visualizer.RED, minInd: visualizer.YELLOW}
            clock.tick(FRAME_RATE * 3)
            draw_sort(visualizer, values, colorIndices)

        # Swap the found minimum element with
        # the first element
        values[i], values[minInd] = values[minInd], values[i]
        colorIndices = {i: visualizer.GREEN}
        draw_sort(visualizer, values, colorIndices)
        clock.tick(FRAME_RATE // 4)

    return values


# bubble
def bubble_sort(visualizer):
    values = visualizer.values

    for i in range(len(values) - 1):
        for j in range(len(values) - 1 - i):
            firstVal = values[j]
            secondVal = values[j + 1]

            if firstVal > secondVal:
                values[j], values[j + 1] = values[j + 1], values[j]
                colorIndices = {j: visualizer.GREEN, j + 1: visualizer.RED}
                clock.tick(FRAME_RATE)
                draw_sort(visualizer, values, colorIndices)

    return values


# merge

# quick
