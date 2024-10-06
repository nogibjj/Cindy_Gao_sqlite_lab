# Python Script interacting with SQL Database
## Requirements:

* Connect to a SQL database
* Perform CRUD operations
* Write at least two different SQL queries

## Project Structure:

- **.devcontainer**: Sets up a consistent development environment across different machines.
- **.github/workflows**: Defines automated workflows for CI/CD tasks.
- **Makefile**: Manages tasks like installing dependencies, formatting code, linting, and testing.
- **requirements**: Lists the Python packages required by the project.
- **main.py**: Contains the main code and functions for `query.py`.
- **test_main.py**: Contains test cases for `mylib`.
- **README.md**: Provides documentation and information for the project.
- **data**: Contains extracted dataset CSV file: `murder_2015_final.csv`.
- **mylib**: Contains:
  - `extract.py`: Extracts a dataset from a URL.
  - `query.py`: Contains functions including read query, update query, delete query, and sort the change columns.
  - `transform_load.py`: Loads the transformed data into a SQLite database table using Python's `sqlite3` module.

```plaintext
Cindy_Gao_sqlite_lab/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
├── data/
│   └── murder_2015_final.csv
├── main.py
├── mylib/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── query_log.md
├── requirements.txt
├── setup.sh
└── test_main.py
```


## Raw Data:
https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/murder_2016/murder_2015_final.csv <br><br>
The dataset presents the numbers of murders in 2014 and 2015, grouped by different cities in the US. <br><br>
Here is a screenshot of the extracted database using SQLite: <br><br>
![image](https://github.com/user-attachments/assets/b55b826a-483c-4b21-99b6-8b5da535364e)

![image](https://github.com/user-attachments/assets/9afdf2b2-dafa-48d2-83ba-5eece83f1fe4)





