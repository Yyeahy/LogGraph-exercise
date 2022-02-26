import pygal
import numpy as np
from pygal.style import NeonStyle
from highest_lowest import highest_lowest_price



def print_points():
    highest_p,lowest_p ,x_value = highest_lowest_price()
    price_max = max(highest_p)
    x = range(0, len(x_value))
    y = highest_p
    y_range = np.arange(0, price_max + price_max * 0.1)

    line_chart = pygal.Line(height=250,style=NeonStyle)
    line_chart.title = "Daily Highest & Lowest BTC"

    line_chart.x_title = "Date"
    line_chart.y_title = "Price"

    line_chart.x_labels = x_value
    line_chart.add("higest price", highest_p)
    line_chart.add("lowest price", lowest_p)

    line_chart.render_to_file("test.svg")

print_points()
