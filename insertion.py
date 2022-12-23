from visualizer import draw
import time

def insertion_sort(visualizer):
    values = visualizer.values

    for i in range(1, len(values)):
        element = values[i]
        j = i-1

        while j >= 0 and element < values[j]:
            values[j+1] = values[j]
            j = j - 1
        
        # place chosen element after the element just smaller than it
        values[j+1] = element

        visualizer.values = values
        draw(visualizer)
        time.sleep(0.1)

    return values



