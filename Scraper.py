import requests
from bs4 import BeautifulSoup
import pandas as pd

dataTables = []


for x in range(0,20200,200):
    url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={}&sortColumn=sortOrder&value=&criteria=&resultsPerPage=200&isDescending=false".format(x)
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    table_data = soup.find('table', class_='picklist-dataTable')

    headers = []

    for i in table_data.find_all('th'):
        title = i.text.strip()
        headers.append(title)

    df = pd.DataFrame(columns = headers)


    for j in table_data.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [tr.text.strip() for tr in row_data]
            length = len(df)
            df.loc[length] = row
    dataTables.append(df)




for x in dataTables:
    print(x)
