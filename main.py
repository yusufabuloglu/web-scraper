import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.ycombinator.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = []

for item in soup.select(".titleline"):
    titles.append(item.get_text())

df = pd.DataFrame(titles, columns=["Title"])
df.to_csv("news_titles.csv", index=False)

print("Data scraped and saved to news_titles.csv")