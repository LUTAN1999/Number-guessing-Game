
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Step 1: Fetch IMDb page
url = 'https://www.imdb.com/chart/top/'
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Extract data
movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [float(b.attrs.get('data-value')) for b in soup.select('td.posterColumn span[name=ir]')]

# Step 3: Store data
movie_list = []

for index, movie in enumerate(movies):
    title = movie.a.text.strip()  # safer way to get movie title
    year = movie.span.text.strip("()")  # extract year
    place = index + 1  # rank
    
    data = {
        "place": place,
        "movie_title": title,
        "year": int(year),
        "rating": ratings[index],
        "star_cast": crew[index],
    }
    movie_list.append(data)

# Step 4: Print first 10 movies
for movie in movie_list[:10]:
    print(f"{movie['place']} - {movie['movie_title']} ({movie['year']}) - "
          f"Starring: {movie['star_cast']} Rating: {movie['rating']}")

# Step 5: Save to CSV
df = pd.DataFrame(movie_list, columns=["place", "movie_title", "year", "rating", "star_cast"])
df.to_csv('imdb_top_250_movies.csv', index=False)
print("✅ Data saved to imdb_top_250_movies.csv")
