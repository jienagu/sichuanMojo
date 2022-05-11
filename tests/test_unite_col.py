import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sichuanMojo.tidy_pd import unite_col
import pandas as pd

data = {'name':['Tom', 'nick', 'krish', 'jack', 'Mike','Jan'],
        'age':[20, 21, 19, 18, 21, 33],
       'group':['A','A', 'A', 'B', 'B', "B"],
       'major':['biology', 'english', 'biology', 'english', 'biology', 'biology'],
       'response':['good', 'good', 'ok', 'bad', 'bad','bad']}
 
# Create DataFrame
test_df= pd.DataFrame(data)

def test_unite_col():
    assert unite_col(test_df, 
        unite_by = ["group", "major", "response"], pattern="; ", 
        united_col_name="New_col", output_json=True) == [{'name': 'Tom', 'age': 20, 'group': 'A', 'major': 'biology', 'response': 'good', 'New_col': 'A; biology; good'}, {'name': 'nick', 'age': 21, 'group': 'A', 'major': 'english', 'response': 'good', 'New_col': 'A; english; good'}, {'name': 'krish', 'age': 19, 'group': 'A', 'major': 'biology', 'response': 'ok', 'New_col': 'A; biology; ok'}, {'name': 'jack', 'age': 18, 'group': 'B', 'major': 'english', 'response': 'bad', 'New_col': 'B; english; bad'}, {'name': 'Mike', 'age': 21, 'group': 'B', 'major': 'biology', 'response': 'bad', 'New_col': 'B; biology; bad'}, {'name': 'Jan', 'age': 33, 'group': 'B', 'major': 'biology', 'response': 'bad', 'New_col': 'B; biology; bad'}], "Should be [{'name': 'Tom', 'age': 20, 'group': 'A', 'major': 'biology', 'response': 'good', 'New_col': 'A; biology; good'}, {'name': 'nick', 'age': 21, 'group': 'A', 'major': 'english', 'response': 'good', 'New_col': 'A; english; good'}, {'name': 'krish', 'age': 19, 'group': 'A', 'major': 'biology', 'response': 'ok', 'New_col': 'A; biology; ok'}, {'name': 'jack', 'age': 18, 'group': 'B', 'major': 'english', 'response': 'bad', 'New_col': 'B; english; bad'}, {'name': 'Mike', 'age': 21, 'group': 'B', 'major': 'biology', 'response': 'bad', 'New_col': 'B; biology; bad'}, {'name': 'Jan', 'age': 33, 'group': 'B', 'major': 'biology', 'response': 'bad', 'New_col': 'B; biology; bad'}]!"


if __name__ == "__main__":
    test_unite_col()
    print("test_unite_col() passed")
