import pytest
import requests

def test_create_roles_list_pos(role_url, test_roles_list, clean_role, clean_book):

    response = requests.post(role_url, data=test_roles_list)
    assert response.status_code, 201# check status code

    body = response.json()
    print(body)
    print(test_roles_list)
    test_roles_list['id'] = body['id']

    if body != test_roles_list:
        test_roles_list['book'] = body['book']
        test_roles_list['level'] = body['level']
        print(test_roles_list)
        for key,val in body.items():
            assert body[key]==test_roles_list[key]
    else:
        assert body==test_roles_list

    res = requests.get(role_url + str(body["id"]))  # check that item present in book's list
    assert res.status_code, 200
    clean_role.append(body['id'])
    print(clean_role)
    clean_book.append(body['book'])
    print(clean_book)

def test_create_roles_negative(role_url,test_roles_list_negative,clean_book):

    print(test_roles_list_negative)
    responce = requests.post(role_url, data=test_roles_list_negative)
    print(responce.json())
    assert responce.status_code, 400  # check status code
    clean_book.append(test_roles_list_negative['book'])
    print(clean_book)


