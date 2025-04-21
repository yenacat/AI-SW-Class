from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import *
import urllib

link = pd.read_excel(
    "C:/Users/UserK/projects/Python/20250418/crawling/news_20250417.xlsx"
)
excel_name = "news_detail_20250417.xlsx"
Main_link = list(link["link"])
Information = pd.DataFrame({"number": [], "title": [], "information": [], "link": []})
Information["number"] = link["number"]
Information["title"] = link["title"]
Information["link"] = link["link"]
information = []

# 기사의 본문을 크롤링하는 과정을 전체 링크에서 진행
for main_link in Main_link:
    try:
        response = requests.get(main_link, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            html = response.content
            soup = BeautifulSoup(html, "html.parser")
            info = soup.find("div", {"id": "newsct_article"}).text.strip()
            info = info.replace("\n", "")
            information.append(info)

    except Exception as e:
        try:
            response = request.get(main_link, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code == 200:
                html = response.content
                soup = BeautifulSoup(html, "html.parser")
                info = soup.find("div", {"id": "newsEndContents"}).text.strip()
                info = info.replace("\n", "")
                end = info.index("기사제공")
                info = info[:end]
                information.append(info)
        except Exception as e:
            info = ""
            information.append(info)

Information["information"] = information

with pd.ExcelWriter(excel_name) as writer:
    Information.to_excel(writer, sheet_name="결괏값", index=False)
