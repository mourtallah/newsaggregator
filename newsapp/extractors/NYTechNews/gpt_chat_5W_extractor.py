import pandas as pd
import os
import openai
import time

# openai.organization = "org-CVQFGcbsqK2zNgskqSNMaPDq"
openai.api_key = "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"


def da_vinci_getarchival5w(archive_title):
    who = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Who Raised in this sentence?: {archive_title}",
        max_tokens=5,
    )
    return who


def regex_getarchival5w(archive_title):
    who = archive_title
    return who


df = pd.read_csv("~/Projects/newsaggregator/newsapp/data/scraper_out/newsarchive.csv")

for archive_title in df["title_0"]:
    time.sleep(1.5)
    print("Print Archive: " + archive_title)
    if "raise" in archive_title.lower():
        who = regex_getarchival5w(archive_title).replace("raise", "")
        print("Who: " + who)
    else:
        print("No Raise found")
# test=df.apply(lambda x: getarchival5w(x["title_0"]), axis=1)
# print(test)
