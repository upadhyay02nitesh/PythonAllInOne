# Json = Javascript object notation
#  mainly used for storing and transfering da between browser and server

# print("Example")

# convert dict to json format

import json 

d={
    'Name':"Ashwani Kumar Dwivedi",
    'Position':'Not It Engineer(S.D.A)',
    'Location':'Noida'}

print(type(d))

f=json.dumps(d)
print("Json",f)
print(type(f))



#Covert json format to dict
import json
js='{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
d=json.loads(js)
print(d)
print(type(d))

# Read data from json file from sample.json 

# input=={
#     "firstName": "Rack",
#     "lastName": "Jackon",
#     "gender": "man",
#     "age": 24,
#     "address": {
#         "streetAddress": "126",
#         "city": "San Jone",
#         "state": "CA",
#         "postalCode": "394221"
#     },
#     "phoneNumbers": [
#         { "type": "home", "number": "7383627627" }
#     ]
# }

# OutPut==firstName Rack
# lastName Jackon
# gender man
# age 24
# streetAddress 126
# city San Jone
# state CA
# postalCode 394221
# type home
# number 7383627627

import json
with open("sample.json",mode='r') as f:
    data=f.read()
    final=json.loads(data)
    # print(final)
    for i,j in final.items():
        if type(j) is dict:
            for m,n in j.items():
                print(m,n)
        elif type(j) is list:
            for s in j:
                if type(s) is dict:
                    for m,n in s.items():
                        print(m,n)
                else:
                    print(i,s)

        else:
            print(i,j)

# Create Writing Data IN Json File

import json 
d={
    'Name':'Kalu',
    "Age":'Two Years'}

with open("sample2.json",mode='w') as f:
    json.dump(d,f)
    print("Writing in json file completed !!")