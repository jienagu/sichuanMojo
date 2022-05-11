import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sichuanMojo.tidy_pd import pivot_rate
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

def test_pivot_rate():
    assert  pivot_rate(test_df, group_by=["major", "group"], summmarize_at="response", output_json = True, na_fill=0)== [{'major': 'biology', 'group': 'A', 'response_count_bad': 0.0, 'response_count_good': 1.0, 'response_count_ok': 1.0, 'response_perc_bad': 0.0, 'response_perc_good': 50.0, 'response_perc_ok': 50.0}, {'major': 'biology', 'group': 'B', 'response_count_bad': 2.0, 'response_count_good': 0.0, 'response_count_ok': 0.0, 'response_perc_bad': 100.0, 'response_perc_good': 0.0, 'response_perc_ok': 0.0}, {'major': 'english', 'group': 'A', 'response_count_bad': 0.0, 'response_count_good': 1.0, 'response_count_ok': 0.0, 'response_perc_bad': 0.0, 'response_perc_good': 100.0, 'response_perc_ok': 0.0}, {'major': 'english', 'group': 'B', 'response_count_bad': 1.0, 'response_count_good': 0.0, 'response_count_ok': 0.0, 'response_perc_bad': 100.0, 'response_perc_good': 0.0, 'response_perc_ok': 0.0}], "Should be [{'major': 'biology', 'group': 'A', 'response_count_bad': 0.0, 'response_count_good': 1.0, 'response_count_ok': 1.0, 'response_perc_bad': 0.0, 'response_perc_good': 50.0, 'response_perc_ok': 50.0}, {'major': 'biology', 'group': 'B', 'response_count_bad': 2.0, 'response_count_good': 0.0, 'response_count_ok': 0.0, 'response_perc_bad': 100.0, 'response_perc_good': 0.0, 'response_perc_ok': 0.0}, {'major': 'english', 'group': 'A', 'response_count_bad': 0.0, 'response_count_good': 1.0, 'response_count_ok': 0.0, 'response_perc_bad': 0.0, 'response_perc_good': 100.0, 'response_perc_ok': 0.0}, {'major': 'english', 'group': 'B', 'response_count_bad': 1.0, 'response_count_good': 0.0, 'response_count_ok': 0.0, 'response_perc_bad': 100.0, 'response_perc_good': 0.0, 'response_perc_ok': 0.0}]!"


if __name__ == "__main__":
    test_pivot_rate()
    print("test_pivot_rate() passed")
