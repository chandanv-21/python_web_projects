import requests
import json
URL="http://127.0.0.1:8000/student_api/"

def get_data(id=None):
    data={'id':id}
    if id is not None:
        data={'id':id}
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data, headers=headers)
    data= r.json()
    print(data)

get_data(1)

def post_data():
    data={"name":"Manish",
          "roll":111,
          "city":"Ranchi"}
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data,headers=headers)
    ndata=r.json()
    print(ndata)
# post_data()
# print("Hello worldcd..")
def update_data():
    data={
        'id':4,
        'city':'VNS'
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data,headers=headers)
    data=r.json()
    print(data)

# update_data()

def delete_data():
    data={
        'id':5
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data,headers=headers)
    data=r.json()
    print(data)
# delete_data()