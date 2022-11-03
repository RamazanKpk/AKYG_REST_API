import requests
URL = "http://127.0.0.1:5000/movie"

name = input("> ")
#GET Process
responseGet = requests.get (URL + f"?title={name}")
getOut = responseGet.json()
#POST Process
payload = {'name':'history', 'details':[]}
responsePost = requests.request("POST",url="http://127.0.0.1:5000/movie", json=payload)
postOut = responsePost.json()
#DELETE Process
delete = {'name':'action'}
responseDelete = requests.request("DELETE", url="http://127.0.0.1:5000/movie/action", json=delete)
deleteOut = responseDelete.text
print(postOut,"\n")
print(deleteOut,"\n")
print(getOut,"\n")