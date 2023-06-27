from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_text.append(article_texts)
    article_link = article_tag.get("href")
    article_link.append(article_link)

article_upvote = soup.find(name="spam", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote)



# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.string)

# # print(soup.prettify())

# # print(soup.li.string)

# # all_anchor_tags = soup.find_all(name="a")

# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))

# # heading = soup.find_all(name = "h1", id="name")
# # print(heading)

# # section_heading = soup.find_all(name="h3", class_="heading")
# # print(section_heading)

# name = soup.select_one(selector="#name")  # # Sign is used for id
# print(name)

# heading = soup.select(selector=".heading")  # . Sign is used for classes 
# print(heading)