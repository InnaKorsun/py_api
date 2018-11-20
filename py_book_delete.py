import pytest
import requests

def test_delete_book_positive(book_url,add_test_book):
    book_id = add_test_book

    r = requests.delete(book_url + str(book_id))
    assert r.status_code, 204  # check that book deleted(by status code)

    responce_get = requests.get(book_url + str(book_id))
    assert responce_get.status_code, 404  # check that book doen't present in list

def test_delete_book_negative(book_url,add_test_book):
    r = requests.delete(book_url + str(add_test_book["id"] + 10000))  # try delete book with d which doesn;t exist
    assert r.status_code, 404  # check that book deleted(by status code)