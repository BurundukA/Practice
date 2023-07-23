import requests
from bs4 import BeautifulSoup

def parsing(part_of_link):
    url = "https://apsjournals.apsnet.org/doi/" + part_of_link

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract abstract
    abstract_element = soup.find("div", class_="hlFld-Fulltext")
    abstract = abstract_element.text.strip()

    return abstract