import requests

url="https://quotes.toscrape.com/"

headers= {
    "User-Agent": "MyLearningBot/1.0 (class project; contact: rkkbeto@gmail.com)"
}

response=requests.get(url, headers=headers, timeout=10)

print(response)
print(response.status_code)
#print(response.content) 
