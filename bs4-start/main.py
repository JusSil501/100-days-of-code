from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")


yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

all_titles  = soup.find_all("a", attrs={"class": "titlelink"})

article_texts = []
article_links = []

for tag in all_titles:
    text = tag.get_text()
    link = tag.get('href')
    article_texts.append(text)
    article_links.append(link)



article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


highest = max(article_upvote)
print(highest)
index = article_upvote.index(highest) +1
print(index)



print(article_links[index])
print(article_texts[index])

