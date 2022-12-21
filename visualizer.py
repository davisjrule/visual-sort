import pandas as pd
import numpy as np
import plotly.express as px

n = 10   # global variable representing array size
valRange = 10

# RETURNS: a randomly generated array of integers
#          such that range = valRange and size = n
def generate_array():
    randArray = np.random.randint(low=1, high=valRange, size=n)
    return randArray


def main():
    array = generate_array()
    indices = list(range(0, n))
    fig = px.bar(x=indices, y=array).update_layout(
                 xaxis_title="index", yaxis_title="value")
    fig.show()


if __name__ == "__main__":
    main()