import pytest
import requests

from py_api.conftest import book_url


def test_create_book_pos():
    response = requests.post(book_url, data=new_book)

    assert response.status_code, 201 # check status code
    body = response.json()

    new_book["id"] = body["id"] # add to json id book
    assert new_book, body

    res = requests.get(book_url + str(body["id"]))#check that item present in book's list
    assert res.status_code, 200
    book_ids.append(body["id"])

