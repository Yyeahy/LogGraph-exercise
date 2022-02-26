# LogGraph-exercise
This is the exercise I did for practising how to read the file then become the line graph.
#
## Install Pygal

I choose the Pygal to create the line graphs.
#
### Installation

```sh
$ pip install Pygal
```
#
## About Files
* [`Test.log`](https://github.com/Yyeahy/LogGraph-exercise/blob/main/Test.log) is the file I created to use for testing the final output.
   * Format of date writing in is based on the international standard ISO 8601.
* [`catch_credentials.py`](https://github.com/Yyeahy/LogGraph-exercise/blob/main/catch_credentials.py) is using the Regex module to filter out the key credentials out of the [`Test.log`](https://github.com/Yyeahy/LogGraph-exercise/blob/main/Test.log)
* [`calculate_date_gap.py`](https://github.com/Yyeahy/LogGraph-exercise/blob/main/calculate_date_gap.py) will calculate how many days between the first date and last date of the data.
* [`highest_lowest.py`](https://github.com/Yyeahy/LogGraph-exercise/blob/main/highest_lowest.py) will calculate the highest and lowest price for the same date.
* Finally,[`log_graph.py`](https://github.com/Yyeahy/LogGraph-exercise/blob/main/log_graph.py) reads the information obtained and draws a line graph with Pygal.
#
