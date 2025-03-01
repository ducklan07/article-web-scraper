import requests
from bs4 import BeautifulSoup


def get_article_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")

    soup = BeautifulSoup(response.content, "html.parser")

    # get title
    title = soup.find("h1").get_text()

    # get content
    paragraphs = soup.find_all("p")
    content = " ".join([para.get_text() for para in paragraphs])

    return title, content
