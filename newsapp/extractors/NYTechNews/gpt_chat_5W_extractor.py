import pandas as pd
import os
import openai

# openai.organization = "org-CVQFGcbsqK2zNgskqSNMaPDq"
openai.api_key = "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"


def getarchival5w(archive_title):
    who = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Who Raised in this sentence?: {archive_title}",
        max_tokens=5,
    )
    return who


df = pd.read_csv("../data/scraper_out/newsarchive.csv")

for archive_title in df["title_0"]:
    print(archive_title)
    print(getarchival5w(archive_title))
# test=df.apply(lambda x: getarchival5w(x["title_0"]), axis=1)
# print(test)
