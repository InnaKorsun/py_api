import pytest
import requests

def test_delete_role_positive(role_url,test_role,clean_book):

    role_id = test_role['id']
    print(test_role)
    r = requests.delete(role_url + str(role_id))
    assert r.status_code, 204  # check that book deleted(by status code)

    responce_get = requests.get(role_url + str(role_url))
    assert responce_get.status_code, 404  # check that book doen't present in list
    clean_book.append(test_role['book'])
    print(clean_book)


def test_delete_role_negative(role_url):

    r = requests.delete(role_url + str(0))  # try delete book with d which doesn;t exist
    assert r.status_code, 404  # check that book deleted(by status code)