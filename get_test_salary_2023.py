import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

salary_list = []
name_list = []
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
    liss = []
    liss.append(lis[i])
    liss.append(lis[i + 1])
    liss.append(lis[i + 2])
    liss.append(lis[i + 3])
    ws.append(liss)
wb.save("test_salary_2023.csv")

