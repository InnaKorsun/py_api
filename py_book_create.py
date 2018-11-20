import pytest
import requests


def test_create_books_list_pos(book_url, book_create,clean_book):

    response = requests.post(book_url, data=book_create)
    assert response.status_code, 201  # check status code

    body = response.json()
    book_create["id"] = body["id"]  # add to json id book
    assert book_create, body

    res = requests.get(book_url + str(body["id"]))  # check that item present in book's list
    assert res.status_code, 200

    clean_book.append(body['id'])

def test_max_lenght_field(book_url,test_boundary,clean_book):

    book  = {"title": test_boundary, "author": "InnaK"}
    if test_boundary.startswith("49") or test_boundary.startswith("50"):  # check if title contain 49 or 50 symbol  - book should created
        response = requests.post(book_url, data=book)
        assert response.status_code, 201

        body = response.json()
        res = requests.get(book_url + str(body['id']))  # check that item present in book's list
        assert res.status_code, 200

        clean_book.append(body['id'])
    else:
        response = requests.post(book_url, data=book)  # check if title contain 51 symbol s - book shouldn't created
        assert response.status_code, 400


def test_create_book_negative(book_url,book_create_negativ):

    response = requests.post(book_url, data=book_create_negativ)  # check if title contain 51 symbol s - book shouldn't created
    assert response.status_code, 400

