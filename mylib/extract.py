"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well
"""

import os
import requests


def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/master/murder_2016/murder_2015_final.csv",
    file_path="data/murder_2015_final.csv",
):
    """ "Extract a url to a file path"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Fetch the content from the URL
    response = requests.get(url)

    # Check for valid response status
    if response.status_code == 200:
        # Save the content to the specified file path
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"File successfully downloaded to {file_path}")
    else:
        print(f"Failed to retrieve the file. HTTP Status Code: {response.status_code}")

    return file_path
