import pytest
import requests
import json


@pytest.fixture(scope="session")
def book_url():
    s = 'http://pulse-rest-testing.herokuapp.com/books/'
    return s


# test book to delete_book
test_book = {"title": "Unittest tutorial", "author": "InnaK"}

# test books item:
#create_book_list_pos = [{"title": "Djerelo", "author": "Ann Read"},  # usual book (positive case)
 #                       {"id": 1, "title": "Unittest tutorial", "author": "InnaK"},
                        # book with id (book should create with id that api will create)
#                        {"title": "1234567890q@#$%^&*()_+ []{}:;'§!<>", "author": "1234567890q@#$%^&*()_+ []{}:;'§!<>"}
                        # field contains spesial symbols
#                        ]
# list of title(just for readable test name)
create_book_list_pos=[]

def read_book_list():
    with open("book_create.json",'r') as file:
        list_book = file.read()
        #print(list_book)
        parsed_string = json.loads(list_book)
        for i in parsed_string['create_book_list_pos']:
            create_book_list_pos.append(i)
        return create_book_list_pos

create_book_list_pos = read_book_list()

id_to_report = [str(book['title']) for book in create_book_list_pos]

# list with negative test data
create_book_list_negative = [{"title": "", "author": ""},
                             {"author": "InnaK"},
                             {"title": "Eat,pray,love"}]

# list which contains all bondary values to titale filed
titles = []
for i in range(49, 52):  # you can variate to max len here
    s = str(i) + "s" * (i - 2)
    titles.append(s)

# book's/roles list which should  be deleted (teardown)
book_to_delete = []
role_to_delete = []

#
update_info = [{"title": "Djerelo", "author": "Ann Read"},
               {"title": "Lullaby"},
               {"id": 1}]


# paramatrize fixture to test create book by create_book_list
@pytest.fixture(params=create_book_list_pos, ids=id_to_report)
def book_create(book_url, request):
    book = request.param
    yield book


# fixture to create boundary value to test max len of field(from titles)
@pytest.fixture(params=titles)
def test_boundary(request):
    field = request.param
    yield field


# fixture to test create list book_negative
@pytest.fixture(params=create_book_list_negative, ids=["empty fields", "Only author", "Only title"])
def book_create_negativ(book_url, request):
    book = request.param
    yield book


# fixture like teardown
@pytest.fixture
def clean_book(book_url):
    yield book_to_delete
    for id in book_to_delete:
        r = requests.delete(book_url + str(id))


# fixture create book to test delete/update function
@pytest.fixture(scope="session")
def add_test_book(book_url):
    r = requests.post(book_url, data=test_book)
    print(test_book)
    book_id = r.json()['id']  # id just created book for test
    assert r.status_code, 201

    responce_id = requests.get(book_url + str(book_id))
    assert responce_id.status_code, 200
    book = responce_id.json()
    return book


# paramatrize fixture to test data to update function
@pytest.fixture(params=update_info, ids=["all_filed_updated", "update_title", "update_id"])
def update_book(request):
    update_book = request.param
    yield update_book


@pytest.fixture
def update_book_negative():
    return {"title": "", "author": ""}


# ______________________________________________________________________________________________
@pytest.fixture
def role_url():
    return "http://pulse-rest-testing.herokuapp.com/roles/"


def id_book():

    r = requests.post('http://pulse-rest-testing.herokuapp.com/books/', data=test_book)
    id = r.json()['id']
    return id

def create_role_list(id_book):

    role_list = [{"name": "Albus Dambldor", "type": "Wizzard", "level": 1, "book": id_book()},
                {"id": 300, "name": "Gandalf", "type": "Maya", "level": 1, "book": id_book()},
                {"name": "Volan de Mort", "type": "Lord", "level": 1.0, "book": id_book()},
                 {"name": "Gandalf", "type": "Maya"}]
    return role_list

role_list = create_role_list(id_book)

# paramatrize fixture to role test positive
@pytest.fixture(params=role_list, ids=["positive", 'with id', 'float level', 'only required fields'])
def test_roles_list(request):
    role = request.param
    yield role

role_list_negative = [{"type": "Lord", "level": 1, "book": id_book()},
                      {"name": "Volan de Mort", "level": 1, "book": id_book()},
                      {"name": "", "type": "", "level": None, "book": None},
                      {"name": "Volan de Mort", "type": "Lord", "level": 1, "book": (-1000000)},
                      {"name": "Volan de Mort", "type": "Lord", "level": 1, "book": "l"}
                      ]

#role_list.clear()
#role_list_negative.clear()
@pytest.fixture(params=role_list_negative,
                ids=["without name", 'without type', 'all empty', 'not exist book', 'book link is string'])
def test_roles_list_negative(request):
    role = request.param
    yield role


# fixture like teardown for roles items
#@pytest.fixture
#def clean_book(book_url):
#    yield book_to_delete
##    for id in book_to_delete:
 #       r = requests.delete(book_url + str(id))

# fixture like teardown for book items
@pytest.fixture
def clean_role(role_url):
    yield role_to_delete
    for id in role_to_delete:
        r = requests.delete(role_url + str(id))

@pytest.fixture
def test_role():
    test_role = {"name": "Albus Dambldor", "type": "Wizzard", "level": 1, "book": id_book()}
    r = requests.post('http://pulse-rest-testing.herokuapp.com/roles/', data=test_role)
    return r.json()

update_role_list = [{"name": "Gandalf", "type": "Maya","level":1},
                    {"id":1}
                    ]
@pytest.fixture(params=update_role_list,ids=["update_name_type_level",'update_id'])
def update_role(request):
    role = request.param
    yield role

update_role_negative =[{"name": "", "type": "", "level": None, "book": None},
                      {"name": "Volan de Mort", "type": "Lord", "level": 1, "book": (-1000000)}]

@pytest.fixture(params=update_role_negative,ids=['empty','update_book'])
def update_role_negative(request):
    role = request.param
    yield role




