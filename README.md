## sichuanMojo
Built on the top of `pandas`, sichuanMojo is a grammar of data manipulation with data frame, providing a consistent a series of utility functions that help you solve the most common data manipulation challenges:

* `unite_col`: unite cols into one column
* `separate_col`: separate column by a pattern into individual column
* `groupby_col`: provide a summary table of a selected column which grouped by desired column(s)
* `groupby_across`: provide a summary table of a selected column with basic statistical infomation (min, max, sum, median) which grouped by desired column(s)
* `pivot_tb`: provide a pivot (count/frequency) table of a selected column which grouped by desired column(s)
* `pivot_rate`: provide a pivot (rate/percentage) table of a selected column which grouped by desired column(s)
* `simplify_network_df`: simplify the network dataframe from directed to undirecte

## Installation from github
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
```
pip install sichuanMojo
```
## Backgroud

The Sichuan province is pandas' hometown which explains the name of this library!



## Usage

```python
import sichuanMojo as sm
import pandas as pd

# test_dict as an example input
data = {'name':['Tom', 'nick', 'krish', 'jack', 'Mike','Jan'],
        'age':[20, 21, 19, 18, 21, 33],
       'group':['A','A', 'A', 'B', 'B', "B"],
       'major':['biology', 'english', 'biology', 'english', 'biology', 'biology'],
       'response':['good', 'good', 'ok', 'bad', 'bad','bad']}
 
# Create DataFrame
test_df= pd.DataFrame(data)
```

|    | name   |   age | group   | major   | response   |
|---:|:-------|------:|:--------|:--------|:-----------|
|  0 | Tom    |    20 | A       | biology | good       |
|  1 | nick   |    21 | A       | english | good       |
|  2 | krish  |    19 | A       | biology | ok         |
|  3 | jack   |    18 | B       | english | bad        |
|  4 | Mike   |    21 | B       | biology | bad        |


### unite cols into one column

Note: if arg output_json = True, output will be json format. Otherwise, output will be a data frame.

```python
sm.unite_col(test_df, unite_by = ["group", "major", "response"], pattern="; ", united_col_name="New_col", output_json=False)

```
|    | name   |   age | group   | major   | response   | New_col          |
|---:|:-------|------:|:--------|:--------|:-----------|:-----------------|
|  0 | Tom    |    20 | A       | biology | good       | A; biology; good |
|  1 | nick   |    21 | A       | english | good       | A; english; good |
|  2 | krish  |    19 | A       | biology | ok         | A; biology; ok   |
|  3 | jack   |    18 | B       | english | bad        | B; english; bad  |
|  4 | Mike   |    21 | B       | biology | bad        | B; biology; bad  |


### separate column by a pattern into individual column

Note: if arg output_json = True, output will be json format. Otherwise, output will be a data frame.

```python
# Test data
data2 = {'name':['Tom', 'nick', 'krish', 'jack', 'Mike'],
        'age':[20, 21, 19, 18, 21],
       'group':['A','A', 'A', 'B', 'B'],
       'major':['biology', 'english', 'biology', 'english', 'biology'],
       'date':['2022-01-13', '2022-06-23', '2022-03-12', '2022-08-23', '2022-09-13']}
 
# Create DataFrame
test_df2= pd.DataFrame(data2)

```

|    | name   |   age | group   | major   | date       |
|---:|:-------|------:|:--------|:--------|:-----------|
|  0 | Tom    |    20 | A       | biology | 2022-01-13 |
|  1 | nick   |    21 | A       | english | 2022-06-23 |
|  2 | krish  |    19 | A       | biology | 2022-03-12 |
|  3 | jack   |    18 | B       | english | 2022-08-23 |
|  4 | Mike   |    21 | B       | biology | 2022-09-13 |

```python
sm.separate_col(test_df2, sep_by="date", pattern="-", sep_to_names=["year", "month", "date"], output_json=False)

```
|    | name   |   age | group   | major   |   date |   year |   month |
|---:|:-------|------:|:--------|:--------|-------:|-------:|--------:|
|  0 | Tom    |    20 | A       | biology |     13 |   2022 |      01 |
|  1 | nick   |    21 | A       | english |     23 |   2022 |      06 |
|  2 | krish  |    19 | A       | biology |     12 |   2022 |      03 |
|  3 | jack   |    18 | B       | english |     23 |   2022 |      08 |
|  4 | Mike   |    21 | B       | biology |     13 |   2022 |      09 |


### provide a summary table of a selected column which grouped by desired column(s)

Note: if arg `output_json = True`, output will be json format. Otherwise, output will be a data frame. 

*operator should be one of mean, sum, min, max, median, unique, count, nunique*

```python
sm.groupby_col(test_df, group_by = ["group", "major"], summmarize_at = "name", operator = "nunique", output_json = True)
#returns [{'group': 'A', 'major': 'biology', 'name': 2},
# {'group': 'A', 'major': 'english', 'name': 1},
# {'group': 'B', 'major': 'biology', 'name': 2},
# {'group': 'B', 'major': 'english', 'name': 1}]

```
```python
sm.groupby_col(test_df, group_by = ["group", "major"], summmarize_at = "name", operator = "nunique")
```
|    | group   | major   |   name |
|---:|:--------|:--------|-------:|
|  0 | A       | biology |      2 |
|  1 | A       | english |      1 |
|  2 | B       | biology |      2 |
|  3 | B       | english |      1 |

### provide a summary table of a selected column with basic statistical infomation (min, max, sum, median) which grouped by desired column(s)

Note: if arg output_json = True, output will be json format. Otherwise, output will be a data frame.

```python
sm.groupby_across(test_df, ["group", "major"], summmarize_at="age", operation=None, output_json = False)
```

|    | group   | major   |   age_min |   age_max |   age_sum |   age_median |
|---:|:--------|:--------|----------:|----------:|----------:|-------------:|
|  0 | A       | biology |        19 |        20 |        39 |         19.5 |
|  1 | A       | english |        21 |        21 |        21 |         21   |
|  2 | B       | biology |        21 |        33 |        54 |         27   |
|  3 | B       | english |        18 |        18 |        18 |         18   |

### provide a pivot (count/frequency) table of a selected column which grouped by desired column(s)

Note: if arg output_json = True, output will be json format. Otherwise, output will be a data frame.

```python
sm.pivot_tb(test_df, group_by=["group", "major"], summmarize_at="response", operation="count", output_json = False, na_fill=0)
```
|    | group   | major   |   bad |   good |   ok |
|---:|:--------|:--------|------:|-------:|-----:|
|  0 | A       | biology |     0 |      1 |    1 |
|  1 | A       | english |     0 |      1 |    0 |
|  2 | B       | biology |     2 |      0 |    0 |
|  3 | B       | english |     1 |      0 |    0 |


### provide a pivot (rate/percentage) table of a selected column which grouped by desired column(s)

Note: if arg output_json = True, output will be json format. Otherwise, output will be a data frame.

```python
sm.pivot_rate(test_df, group_by=["major", "group"], summmarize_at="response", output_json = False, na_fill=0)
```

|    | major   | group   |   response_count_bad |   response_count_good |   response_count_ok |   response_perc_bad |   response_perc_good |   response_perc_ok |
|---:|:--------|:--------|---------------------:|----------------------:|--------------------:|--------------------:|---------------------:|-------------------:|
|  0 | biology | A       |                    0 |                     1 |                   1 |                   0 |                   50 |                 50 |
|  1 | biology | B       |                    2 |                     0 |                   0 |                 100 |                    0 |                  0 |
|  2 | english | A       |                    0 |                     1 |                   0 |                   0 |                  100 |                  0 |
|  3 | english | B       |                    1 |                     0 |                   0 |                 100 |                    0 |                  0 |

### provide an easy way to simplify network data frame from directed to undirected
        
Note: if arg `keep = "last"`, output dataframe will keep the last row of duplicated rows. if arg `keep = "first"`, output dataframe will keep the first row of duplicated rows. 


```python
data = {'from':['Tom', 'Jack', 'Jen', 'Sam'],
'overlap':[20, 21, 19, 18],
'to':['Jack','Tom', 'Emily', 'John']}

test_df= pd.DataFrame(data)

```
|    | from   |   overlap | to    |
|---:|:-------|----------:|:------|
|  0 | Tom    |        20 | Jack  |
|  1 | Jack   |        21 | Tom   |
|  2 | Jen    |        19 | Emily |
|  3 | Sam    |        18 | John  |

In the test_df, we have duplicated Tom <--> Jack pairs. 

```python
sm.simplify_network_df(test_df, from_col = "from", to_col = "to", keep = "first")
```
|    | from   |   overlap | to    |
|---:|:-------|----------:|:------|
|  0 | Tom    |        20 | Jack  |
|  2 | Jen    |        19 | Emily |
|  3 | Sam    |        18 | John  |

We can see output only keeps one Tom <--> Jack pair. 