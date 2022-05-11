import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sichuanMojo.tidy_pd import groupby_col
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

def test_groupby_col():
    assert groupby_col(test_df, group_by = ["group", "major"], summmarize_at = "name", operator = "nunique", output_json = True) == [{'group': 'A', 'major': 'biology', 'name': 2}, {'group': 'A', 'major': 'english', 'name': 1}, {'group': 'B', 'major': 'biology', 'name': 2}, {'group': 'B', 'major': 'english', 'name': 1}], "Should be [{'group': 'A', 'major': 'biology', 'name': 2}, {'group': 'A', 'major': 'english', 'name': 1}, {'group': 'B', 'major': 'biology', 'name': 2}, {'group': 'B', 'major': 'english', 'name': 1}]!"


if __name__ == "__main__":
    test_groupby_col()
    print("test_groupby_col() passed")
