import numpy as np
from catch_credentials import FilterInformation
from calculate_date_gap import CalculateDateGap as cdg


def highest_lowest_price():
    line_length, log_array , first_date, last_date = FilterInformation().catch_key_info()
    date_diff = cdg.calculate_date(first_date, last_date)
    date_price = []
    date = []

    highest_p = np.empty((date_diff ,) ,dtype = float)
    lowest_p = np.empty((date_diff ,) ,dtype = float)
    j = 0
    comparison_date = log_array[0][0]
    date.append(str(int(comparison_date)))
    for i in range(line_length):
        if log_array[i][0] == comparison_date:
            date_price.append(log_array[i][1])
            highest_price = max(date_price)
            lowest_price = min(date_price)
            highest_p[j] = highest_price
            lowest_p[j] = lowest_price
        elif log_array[i][0] != comparison_date:

            comparison_date = log_array[i][0]
            j += 1
            date_price.clear()
            date.append(str(int(comparison_date)))

    return highest_p, lowest_p, date
