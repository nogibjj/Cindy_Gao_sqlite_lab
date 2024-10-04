"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well

food dataset
"""

import requests


def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/master/murder_2016/murder_2015_final.csv",
    file_path="../data/murder_2015_final.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
