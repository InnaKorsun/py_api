import pytest
import requests


def test_update_book_pos(book_url,add_test_book,update_book,clean_book):
    r = requests.put(book_url + str(add_test_book['id']), data=update_book)
    assert r.status_code, 200  # check that book is updated(by status code)

    clean_book.append(add_test_book)
    book_updated = r.json()

    if book_updated != add_test_book:
        for key,val in update_book.items():
            assert book_updated[key]==update_book[key]
    else:
        assert book_updated==add_test_book

def test_update_neg(book_url,add_test_book,update_book_negative,clean_book):

    r = requests.put(book_url + str(add_test_book["id"]), data=update_book_negative)
    assert r.status_code,400
