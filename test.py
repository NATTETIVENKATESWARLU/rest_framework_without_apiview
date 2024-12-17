import requests
import json,time

BASE_URL="http://127.0.0.1:8000/"
END_POINT="json/"

print("get method started")

def get_methos(id=None):
    d={}
    if id is not None:
        d={
            "id":id
        }
    
    req=requests.get(BASE_URL + END_POINT,data=json.dumps(d))
    print(req.status_code)
    print(req.json())



get_methos()
time.sleep(8)
print("post method started")


def create_user():
    dct={
        "eno":4,
        "ename":"ravi",
        "esal":20000,
        "eaddress":"kadapa"
    }

    req=requests.post(BASE_URL + END_POINT,data=json.dumps(dct))
    print(req.status_code)
    print(req.json())

create_user()

time.sleep(8)
print("put method started")

def update_resours(id=None):
    dict={
        "id":id,
        "ename":"venkat",
        "esal":50000,
    }
    reqs=requests.put(BASE_URL + END_POINT,data=json.dumps(dict))
    print(reqs.status_code)
    print(reqs.json())

update_resours(4)
time.sleep(8)
print("delete method started")

def delete_resours(id=None):
    data={
        "id":id
    }
    
    reqs=requests.delete(BASE_URL + END_POINT,data=json.dumps(data))
    print(reqs.status_code)
    print(reqs.json())

delete_resours(4)