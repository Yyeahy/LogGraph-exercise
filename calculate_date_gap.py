#
# This class will calculate how many days between the first line date of file and the last line date.
#

import datetime


class CalculateDateGap():


    def date_to_timestamp(year, month, day):

        timestamp = datetime.datetime(int(year), int(month),int(day)) # make sure that the variables are all integer

        return timestamp


    def calculate_date(first_timestamp, last_timestamp):
        # this only calculate the days between two dates, not include the first date, that is the reason we have to plus one
        date_diff = (last_timestamp - first_timestamp).days + 1

        return(date_diff)
