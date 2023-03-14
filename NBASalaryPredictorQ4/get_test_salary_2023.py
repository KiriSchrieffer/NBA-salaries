# Author: Qingyuan Zhang
# This is a crawler file to get test data of salaries of players.
# This program will output a csv file, ANSI encoding.
import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

lis = []

for num in range(1, 14):
    url = f"http://www.espn.com/nba/salaries/_/page/{num}"
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    names = soup.find_all("td")
    for name in names:
        lis.append(name.text)

for i in range(0, len(lis), 4):
    if i == 0:
        liss = []
        liss.append(lis[i + 1].split(',')[0])
        liss.append(lis[i + 3])
        ws.append(liss)
    if lis[i + 3][0] == '$':
        liss = []
        liss.append(lis[i + 1].split(',')[0])
        liss.append(lis[i + 3][1:].replace(",", ""))
        ws.append(liss)
wb.save("test_salary_2023.csv")