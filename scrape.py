import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"

headers= {
    "User-Agent": "MyLearningBot/1.0 (class project; contact: rkkbeto@gmail.com)"
}

response=requests.get(url, headers=headers, timeout=10)

#print(response)
#print(response.status_code)
#print(response.content) 

soup=BeautifulSoup(response.content, "html.parser")
#print(soup)

cards=soup.select(".quote")
#print(cards)
#print(len(cards))


first= cards[0]
#print(first)
#print(first.select_one(".text").text)
#print(first.select_one(".author").text)
#tags= first.select(".tag")
#print(tags[0].text)


all_quotes= []
for card in cards: 
    text= card.select_one(".text").text
    author= card.select_one(".author").text
    tags= []
    for tag in card.select(".tag"): 
        tags.append(tag.text)
    
    quote_item= {
        "quote": text, 
        "author": author, 
        "tags": tags
    }

    all_quotes.append(quote_item)

print(all_quotes)




