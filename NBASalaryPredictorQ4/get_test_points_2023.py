# Author: Qingyuan Zhang
# This is a crawler file to get test data of 3-point field goal,
# assist and points per game of players.
# This program will output a csv file, ANSI encoding.
import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook


wb = Workbook()
ws = wb.active
url = "https://www.basketball-reference.com/leagues/NBA_2023_totals.html"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")
headers = soup.find_all("thead")
fg3_pct = soup.find_all("td", attrs={"data-stat": "fg3_pct"})
ast = soup.find_all("td", attrs={"data-stat": "ast"})
pts = soup.find_all("td", attrs={"data-stat": "pts"})
player = soup.find_all("td", attrs={"data-stat": "player"})
games = soup.find_all("td", attrs={"data-stat": "g"})
lis = ["name", "fg3_pct", "ast", "pts"]
ws.append(lis)
for i in range(0, len(pts)):
    if fg3_pct[i].text != "":
        liss = [player[i].text, float(fg3_pct[i].text) * 100, int(ast[i].text)
                / int(games[i].text), int(pts[i].text) / int(games[i].text)]
        ws.append(liss)
wb.save("test_points_2023.csv")