import requests
import json

url = 'https://github.com/InnaKorsun/py_api/blob/master/book_create.json'
def create_book():
    with open("book_create.json",'r') as file:
        list_book = file.read()
        #print(list_book)
        parsed_string = json.loads(list_book)
        for i in parsed_string['create_book_list_pos']:
            print(i)

#r = requests.get(url)
#print(r.json())
#create_book()

create_book_list_pos=[]

def read_book_list():
    with open("book_create.json",'r') as file:
        list_book = file.read()
        print(list_book)
        parsed_string = json.loads(list_book)
        for i in parsed_string['create_book_list_pos']:
            create_book_list_pos.append(i)
        return create_book_list_pos

create_book_list_pos=read_book_list()
print(create_book_list_pos)