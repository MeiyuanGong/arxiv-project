import requests
from bs4 import BeautifulSoup
import time


response = requests.get("https://arxiv.org/search/?query=reinforcement+learning&searchtype=all&source=header")
papers = response.text
rl = BeautifulSoup(papers, "html.parser")
rl_papers = rl.find_all("p", {"class": "title is-5 mathjax"})
titles_list = [paper.get_text().strip() for paper in rl_papers]

def ger_info(rl):
    rl_divs = rl.find_all("div", {"class": "tags is-inline-block"})
    divs_list = [div.get_text().strip() for div in rl_divs]

    rl_papers = rl.find_all("p", {"class": "title is-5 mathjax"})
    titles_list = [paper.get_text().strip() for paper in rl_papers]

    rl_authors = rl.find_all("p", {"class": "authors"})
    authors_list = [author.get_text().strip() for author in rl_authors]

    rl_abstracts = rl.find_all("span", {"class": "abstract-full has-text-grey-dark mathjax"})
    abstracts_list = [abstract.get_text().strip() for abstract in rl_abstracts]

    
    return titles_list, authors_list, abstracts_list, divs_list

# Save titles to a text file (one title per line)
with open("rl_titles.txt", "w", encoding="utf-8") as file:
    for title in titles_list:
        file.write(title + "\n")

def get_new_titles(titles_list):
    with open("rl_titles.txt", "r", encoding="utf-8") as file:
        old_titles = file.read().splitlines()
    new_titles = [title for title in titles_list if title not in old_titles]
    return new_titles

while True:
    time.sleep(60)

    new_titles = get_new_titles(titles_list)
    print(new_titles)
