# LogGraph-exercise
This is the exercise I did for practising how to read the file then become the line graph.
#
## Install Pygal

I choose the Pygal to create the line graphs.
#
### Installation

```sh
$ pip install pygal
```
#
## About Files
* `Test.log` is the file I created to use for testing the final output.
   * Format of date writing in is based on the international standard ISO 8601.
* `catch_credentials.py` is using the Regex module to filter out the key credentials out of the `Test.log`
* `calculate_date_gap.py` will calcule how many days between the first date and last date of the data.
* `highest_lowest.py` will calculate the highest and lowest price for the same date.
* Finally,`log_graph.py` reads the information obtained and draws a line graph with Pygal.
#
