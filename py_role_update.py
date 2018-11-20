import pytest
import requests


def test_update_role_pos(role_url,test_role,update_role,clean_role, clean_book):

    r = requests.put(role_url + str(test_role['id']), data=update_role)
    assert r.status_code, 200  # check that book is updated(by status code)


    role_updated = r.json()
    print(role_updated)
    print(update_role)

    if role_updated != test_role:
        for key,val in update_role.items():
            assert role_updated[key]==update_role[key]
    else:
        assert role_updated==test_role

    clean_role.append(test_role['id'])
    clean_book.append(test_role['book'])

def test_update_neg(role_url,test_role,update_role_negative,clean_book,clean_role):

    r = requests.put(role_url + str(test_role["id"]), data=update_role_negative)
    assert r.status_code,400

    clean_role.append(test_role['id'])
    clean_book.append(test_role['book'])