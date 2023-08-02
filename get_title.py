import requests
from bs4 import BeautifulSoup


response = requests.get("https://arxiv.org/search/?query=reinforcement+learning&searchtype=all&source=header")
papers = response.text
rl = BeautifulSoup(papers, "html.parser")
rl_papers = rl.find_all("p", {"class": "title is-5 mathjax"})
titles_list = [paper.get_text().strip() for paper in rl_papers]

# Save titles to a text file (one title per line)
with open("rl_titles.txt", "w", encoding="utf-8") as file:
    for title in titles_list:
        file.write(title + "\n")

# Print the titles to the console
for title in titles_list:
    print(title)
