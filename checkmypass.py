import requests
url = "https://api.pwnedpasswords.com/range/" + "008C7"
res= requests.get(url)
print(res)
