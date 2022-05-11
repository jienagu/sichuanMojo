import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sichuanMojo.tidy_pd import pivot_tb
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


def test_pivot_tb():
    assert pivot_tb(test_df, group_by=["group", "major"], summmarize_at="response", operation="count", output_json = True, na_fill=0) == [{'group': 'A', 'major': 'biology', 'bad': 0.0, 'good': 1.0, 'ok': 1.0}, {'group': 'A', 'major': 'english', 'bad': 0.0, 'good': 1.0, 'ok': 0.0}, {'group': 'B', 'major': 'biology', 'bad': 2.0, 'good': 0.0, 'ok': 0.0}, {'group': 'B', 'major': 'english', 'bad': 1.0, 'good': 0.0, 'ok': 0.0}], "Should be [{'group': 'A', 'major': 'biology', 'bad': 0.0, 'good': 1.0, 'ok': 1.0}, {'group': 'A', 'major': 'english', 'bad': 0.0, 'good': 1.0, 'ok': 0.0}, {'group': 'B', 'major': 'biology', 'bad': 2.0, 'good': 0.0, 'ok': 0.0}, {'group': 'B', 'major': 'english', 'bad': 1.0, 'good': 0.0, 'ok': 0.0}]!"


if __name__ == "__main__":
    test_pivot_tb()
    print("test_pivot_tb() passed")
