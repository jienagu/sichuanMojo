import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sichuanMojo.tidy_pd import separate_col
import pandas as pd
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


data = {'name': ['Tom', 'nick', 'krish', 'jack', 'Mike'],
        'age': [20, 21, 19, 18, 21],
        'group': ['A', 'A', 'A', 'B', 'B'],
        'major': ['biology', 'english', 'biology', 'english', 'biology'],
        'date': ['2022-01-13', '2022-06-23', '2022-03-12', '2022-08-23', '2022-09-13']}

# Create DataFrame
test_df = pd.DataFrame(data)


def test_separate_col():
    assert separate_col(test_df, sep_by="date", pattern="-",
        sep_to_names=["year", "month", "date"], output_json=True) == [{'name': 'Tom', 'age': 20, 'group': 'A', 'major': 'biology', 'date': '13', 'year': '2022', 'month': '01'}, {'name': 'nick', 'age': 21, 'group': 'A', 'major': 'english', 'date': '23', 'year': '2022', 'month': '06'}, {'name': 'krish', 'age': 19, 'group': 'A', 'major': 'biology', 'date': '12', 'year': '2022', 'month': '03'}, {'name': 'jack', 'age': 18, 'group': 'B', 'major': 'english', 'date': '23', 'year': '2022', 'month': '08'}, {'name': 'Mike', 'age': 21, 'group': 'B', 'major': 'biology', 'date': '13', 'year': '2022', 'month': '09'}], "Should be [{'name': 'Tom', 'age': 20, 'group': 'A', 'major': 'biology', 'date': '13', 'year': '2022', 'month': '01'}, {'name': 'nick', 'age': 21, 'group': 'A', 'major': 'english', 'date': '23', 'year': '2022', 'month': '06'}, {'name': 'krish', 'age': 19, 'group': 'A', 'major': 'biology', 'date': '12', 'year': '2022', 'month': '03'}, {'name': 'jack', 'age': 18, 'group': 'B', 'major': 'english', 'date': '23', 'year': '2022', 'month': '08'}, {'name': 'Mike', 'age': 21, 'group': 'B', 'major': 'biology', 'date': '13', 'year': '2022', 'month': '09'}]!"


if __name__ == "__main__":
    test_separate_col()
    print("test_separate_col() passed")
