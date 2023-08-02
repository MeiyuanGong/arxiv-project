import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class Paper:
    def __init__(self, title, authors, abstract, keywords):
        self.title = title
        self.authors = authors
        self.abstract = abstract
        self.keywords = keywords

    def __str__(self):
        return f"{self.title}\n{self.authors}\n{self.abstract}\n{self.keywords}\n"
    
    def __repr__(self):
        return f"Paper({self.title}, {self.authors}, {self.abstract}, {self.keywords})"
    



response = requests.get("https://arxiv.org/search/?query=reinforcement+learning&searchtype=all&source=header")
papers = response.text
rl = BeautifulSoup(papers, "html.parser")
# rl_papers = rl.find_all("p", {"class": "title is-5 mathjax"})
# titles_list = [paper.get_text().strip() for paper in rl_papers]

def ger_info(rl):
    rl_divs = rl.find_all("div", {"class": "tags is-inline-block"})
    divs_list = [div.get_text().strip() for div in rl_divs]

    rl_papers = rl.find_all("p", {"class": "title is-5 mathjax"})
    titles_list = [paper.get_text().strip() for paper in rl_papers]

    rl_authors = rl.find_all("p", {"class": "authors"})
    authors_list = [author.get_text().strip() for author in rl_authors]

    rl_abstracts = rl.find_all("span", {"class": "abstract-full has-text-grey-dark mathjax"})
    abstracts_list = [abstract.get_text().strip().encode("utf-8") for abstract in rl_abstracts]

    
    return titles_list, authors_list, abstracts_list, divs_list

titles_list, authors_list, abstracts_list, divs_list= ger_info(rl)
papers_list = []
# print(len(titles_list))
for i in range(len(titles_list)):
    papers_list.append(Paper(titles_list[i], authors_list[i], abstracts_list[i], divs_list[i]))

    

print(papers_list[0].abstract)

