import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
# Actual Website html is under
website_html = response.text    


soup = BeautifulSoup(website_html, "html.parser")
all_headings = soup.find_all(name="h3", class_="title")

# NOTE - We can use getText() to get the string value from all headings beacuse all_headings is a list. 

heading_titles =[headings.getText() for headings in all_headings]
movies = heading_titles[::-1]  # [::-1] is the slice operator which reverse the list. 

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
