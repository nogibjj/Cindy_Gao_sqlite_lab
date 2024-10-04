"""
Tests of mylib goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import read_query, update_query, delete_query, sorting_Change


def test_extract():
    results = extract()
    assert results is not None


def test_load():
    results = load()
    assert results is not None


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
