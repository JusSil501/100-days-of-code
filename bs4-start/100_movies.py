import requests
from bs4 import BeautifulSoup

times = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")


soup = BeautifulSoup(times.text, "html.parser")

titles = soup.find_all("h3", class_="title")

movies = []
for title in titles:
    if title.getText() == "12: The Godfather Part II":
        movies.append(title.getText())

    else:
        movies.append(title.getText())

new_sorted_movies = []



for i in range(len(movies)-1, -1, -1):
    print(movies[i])
    new_sorted_movies.append(movies[i])







with open ("movies.txt", "a") as file:
    for movie in new_sorted_movies:
        file.write(movie)
        file.write("\n")


