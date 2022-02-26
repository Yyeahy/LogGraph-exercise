#
# This class will take the key varialbes form the file
#

import re
import numpy as np
from calculate_date_gap import CalculateDateGap as cdg


class FilterInformation():

    def __init__(self, file_name="./Test.log"):
        self.file = file_name


    def catch_key_info(self):
        with open(self.file) as f:
            self.line_informations = f.readlines()
            self.line_length = len(self.line_informations)
            self.log_info = np.full((self.line_length, 2),0.00)
            i = 0
            for line_info in self.line_informations:

                cut_year_out = re.search("\d{4}(?=-)", line_info).group()
                cut_month_out = re.search("(?<=-).*(?=-)", line_info).group()
                cut_day_out = re.search("\d{2}(?=T)", line_info).group()

                if i == 0:
                    self.first_date = cdg.date_to_timestamp(cut_year_out, cut_month_out, cut_day_out)
                elif i == self.line_length - 1:
                    self.last_date = cdg.date_to_timestamp(cut_year_out, cut_month_out, cut_day_out)

                date = float(cut_year_out + cut_month_out + cut_day_out)
                self.log_info[i][0] = date
                cut_price_out = float(re.search("(?<=] ).*", line_info).group())
                self.log_info[i][1] = cut_price_out

                i += 1

        return self.line_length, self.log_info, self.first_date, self.last_date
