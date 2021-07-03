import requests

header = 'Content-Type: application/json'
address = 'http://localhost:8098/buckets/s15151'
key = '/keys/Writers'

Kubo = {
	'name':'Tite Kubo', 'from':'Japan', 'born':'26-06-1977', 'notable work':'Bleach'
	}

Kuang = {
	'name':'Rebecca F.Kuang', 'from':'China', 'born':'29-05-1996', 'notable work':'The Poppy War'
	}

put1 = requests.put(address + key, json = Kubo)
print("Create document. DB response: ", put1.status_code)

get1 = requests.get(address + key, header)
print("Read document. DB response: ", get1.status_code)
print("Print document: ", get1.json())

put2 = requests.put(address + key, json = Kuang)
print("Add data to document. DB response: ", put2.status_code)

get2 = requests.get(address + key, header)
print("Read document once again. DB response: ", get2.status_code)
print("Print document: ", get2.json())

del1 = requests.delete(address + key)
print("Delete document. DB response: ", del1.status_code)

get3 = requests.get(address + key, header)
print("Read document one last time. DB response: ", get3.status_code)
print("Print document: ", get3.json())