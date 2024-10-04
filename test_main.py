"""
Tests of mylib goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import read_query, update_query, delete_query, sorting_Change


def test_extract():
    assert extract() == "../data/murder_2015_final.csv"


def test_load():
    assert load() == "Murder2015.db"


def test_readquery():
    assert read_query() == "Read Success"


def test_updatequery():
    assert update_query() == "Update Success"


def test_deletequery():
    assert delete_query() == "Delete Success"


def test_sortchange():
    assert sorting_Change() == "Sort Success"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_readquery()
    test_updatequery()
    test_deletequery()
    test_sortchange()
