import bs4
import requests
from pandas import DataFrame
import json

print("Scraping NY Tech News")


class NYTechNews:
    def __init__(self, archive_url):
        self.archive_url = archive_url
        self.archive_titles_0 = []
        self.archive_titles_1 = []
        self.archive_links = []

    def clean_archive_title(title):
        return (
            title.replace(" + More NYC Tech Industry News", "").strsplit(";").str[0],
            title.replace(" + More NYC Tech Industry News", "").strsplit(";").str[1],
        )

    def get_article_urls(self):
        response = requests.get(self.archive_url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("li", {"class": "campaign"})
        blocks = [article.find("a") for article in articles]
        links = [block["href"] for block in blocks]
        titles = [block["title"] for block in blocks]
        return titles, links

        DataFrame({"title": titles, "link": links}).to_csv(
            "NYTechNews.csv", index=False
        )

        # article_urls = [article["text"] for article in articles]
        # return articles


if __name__ == "__main__":
    # Newspage = NYTechNews().get_article_urls
    newsarchive = NYTechNews(
        "https://us1.campaign-archive.com/home/?u=2aa4d42d498f5b86e450f88c8&id=5dd2e495c1"
    )
    archive_titles, archive_links = newsarchive.get_article_urls()

    for archive_title in archive_titles:
        if ";" in archive_title:
            newsarchive.archive_titles_0.append(archive_title.split(";")[0])
            newsarchive.archive_titles_1.append(
                archive_title.split(";")[1].replace(
                    " + More NYC Tech Industry News", ""
                )
            )
        else:
            newsarchive.archive_titles_0.append(
                archive_title.replace(" + More NYC Tech Industry News", "")
            )
            newsarchive.archive_titles_1.append("N/A")

    DataFrame(
        {
            "title_0": newsarchive.archive_titles_0,
            "title_1": newsarchive.archive_titles_1,
            "link": archive_links,
        }
    ).to_csv("../data/scraper_out/newsarchive.csv", index=False)
    # for title in titles:
    #   clean_archive_title(self.titles)
