import requests
import json
import sys
import yaml

redis_env = sys.argv[1].lower()

if redis_env == 'dev':
    redis_url = 'https://dev-endpoint/v1/roles'
elif redis_env == 'uat'
    redis_url = 'https://uat-endpoint/v1/roles'
elif redis_env == 'perf'
    redis_url = 'https://perf-endpoint/v1/roles'
elif redis_env == 'prod'
    redis_url = 'https://prod-endpoint/v1/roles'

# response = requests.get("http://api.open-notify.org/astros.json")
# print(response)
# print(response.content()) # Return the raw bytes of the data payload
# response.text() # Return a string representation of the data payload
# response.json() # This m
response = requests.get(redis_url)
print(response)

with open(r'roles.yaml') as file:
    roles_list = yaml.full_load(file)
    add_list = roles
    delete_list = 
    for env, role in roles_list.items():
        print(env, ":", role)

        if role in response:
            print('It exists already')
        else:
            print('Delete it')


query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
# print(response.json())

post_response = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(post_response)

put_response = requests.put('https://httpbin.org/put', data = {'key':'value1'})
print(put_response)

print(response.headers["date"])

requests.get(
  'https://api.github.com/user', 
auth=HTTPBasicAuth('username', 'password')
)

my_headers = {'Authorization' : 'Bearer {access_token}'}
response = requests.get('http://httpbin.org/headers', headers=my_headers)

try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    if (response.status_code == 200):
        print("The request was a success!")
    # Code here will only run if the request is successful
    elif (response.status_code == 404:
        print("Result not found!")
except requests.exceptions.HTTPError as errorh:
    print(errorh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:        
    print(err)


dev:
    - role-1
    - role-2
    - role-3
    - role-4
    - role-5
qa:
    - role-1
    - role-2
    - role-3
    - role-4
    - role-5

perf:
    - role-1
    - role-2
    - role-3
    - role-4
    - role-5
prod: 
    - role-1
    - role-2
    - role-3
    - role-4
    - role-5        