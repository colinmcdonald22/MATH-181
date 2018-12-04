import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


GREEN_HEX = '#99FF99'
RED_HEX = '#F88379'


def compute_nth_riemann_sum(n: int, func: str, a: float, b: float, endpoint_method: str) -> tuple:
    delta_x = (b - a) / n  # Used as a step value, defined as commonly used in class
    sum = 0  # Tracks total value of the sum
    rectangles = []  # Keeps a history of the area we've summed. This is used purely for visualization

    # Python's range isn't inclusive of the end variable so add one (so the last value is n)
    for i in range(1, n + 1):
        # xᵢ = a + iΔx
        x_i_minus_1 = a + ((i - 1) * delta_x)
        x_i = a + (i * delta_x)

        # Determine what point to evaluate f at
        if endpoint_method == "Left":
            sample_point = x_i_minus_1
        elif endpoint_method == "Right":
            sample_point = x_i
        elif endpoint_method == "Middle":
            sample_point = (x_i_minus_1 + x_i) / 2
        else:
            raise ArithmeticError("Unknown sampling method " + endpoint_method)

        # Evaluate f(xᵢ*) (where xᵢ* = sample_point as chosen above)
        # (We use the fact Python is a dynamic language to simply evaluate the function as code)
        f_at_sample = eval(func, {"x": sample_point})

        # Multiply by Δx and sum (doing this in a loop is equal to sigma notation)
        sum += f_at_sample * delta_x

        # Store the coordinates of the area we calculated the area of to visualize later
        # (The data is ordered like this so it can be passed directly into matplotlib)
        rectangles.append((
            (x_i_minus_1, 0),
            delta_x,
            f_at_sample
        ))

    return sum, delta_x, rectangles


def plot_riemann_sum(n: int, func: str, a: float, b: float, sum: float, delta_x: float, rectangles: list):
    # Evenly distributes 500 points between a and b, evaluates
    # func at each point, and plots the results
    x = np.linspace(a, b, num=500)
    y = eval(func)

    plt.plot(x, y)

    # Plot the rectangles (whose areas we summed to produce the Riemann sum)
    for rectangle in rectangles:
        plt.gca().add_patch(
            patches.Rectangle(
                *rectangle,
                # Positive area (y > 0) is green, negative area is red
                color=GREEN_HEX if rectangle[2] > 0 else RED_HEX
            )
        )

    # Draw a box at the top left showing the actual sum and the value of delta x
    plt.gca().text(
        0.05,
        0.95,
        r"$S_{" + str(n) + "} = " + str(round(sum, 3)) + "$"  # Some nice LaTeX to subscript
        "\n"
        "Δx = " + str(round(delta_x, 3)),
        transform=plt.gca().transAxes,
        fontsize=12,
        verticalalignment="top",
        bbox={
            "boxstyle": "round",
            "facecolor": "wheat",
            "alpha": 0.7
        }
    )

    plt.xlim(a, b)  # Fixes an issue where the graph would cut out the first and last rectangle
    plt.show()


def main() -> None:
    func = "-x^2 + 3".replace("^", "**")
    n = 5
    a = 0.5
    b = 6.7
    endpoint_method = "Left"

    sum, delta_x, rectanges = compute_nth_riemann_sum(n, func, a, b, endpoint_method)
    plot_riemann_sum(n, func, a, b, sum, delta_x, rectanges)


if __name__ == '__main__':
    main()
