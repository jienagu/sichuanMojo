import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sichuanMojo.tidy_pd import groupby_across
import pandas as pd
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


data = {'name':['Tom', 'nick', 'krish', 'jack', 'Mike','Jan'],
        'age':[20, 21, 19, 18, 21, 33],
       'group':['A','A', 'A', 'B', 'B', "B"],
       'major':['biology', 'english', 'biology', 'english', 'biology', 'biology'],
       'response':['good', 'good', 'ok', 'bad', 'bad','bad']}

# Create DataFrame
test_df = pd.DataFrame(data)


def test_groupby_across():
    assert groupby_across(test_df, ["group"], summmarize_at="age", operation=None, output_json = True) == [{'group': 'A', 'age_min': 19, 'age_max': 21, 'age_sum': 60, 'age_median': 20.0}, {'group': 'B', 'age_min': 18, 'age_max': 33, 'age_sum': 72, 'age_median': 21.0}], "Should be [{'group': 'A', 'age_min': 19, 'age_max': 21, 'age_sum': 60, 'age_median': 20.0}, {'group': 'B', 'age_min': 18, 'age_max': 33, 'age_sum': 72, 'age_median': 21.0}]!"


if __name__ == "__main__":
    test_groupby_across()
    print("test_groupby_across() passed")
