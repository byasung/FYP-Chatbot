import requests
import csv
from bs4 import BeautifulSoup as bs

url = requests.get("https://lib.hku.hk/general/borrowing/index.html#0")
soup = bs(url.content, 'html.parser')

filename = "h1.csv"
csv_writer = csv.writer(open(filename, 'w'))

content = soup.find("content_area")
print (content)
for div in soup.find_all("div"):
    string = []

    for section in div.find_all("h2"):
        string.append(th.text)
    if string:
        print("Inserting section : {}".format(','.join(string)))
        csv_writer.writerow(string)
        continue

data = []
table = soup.find('table', attrs={'class':'lineItemsTable'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

    # if :
    #     data.append(td.text.strip())
    # if data:
    #     print("Inserting data: {}".format(','.join(data)))
    #     csv_writer.writerow(data)


# for tr in soup.find_all("tr"):
#     data = []
#     # for headers ( entered only once - the first time - )
#     for th in tr.find_all("th"):
#         data.append(th.text)
#     if data:
#         print("Inserting headers : {}".format(','.join(data)))
#         csv_writer.writerow(data)
#         continue
#
#     for td in tr.find_all("td"):
#         if td.a:
#             data.append(td.a.text.strip())
#         else:
#             data.append(td.text.strip())
#     if data:
#         print("Inserting data: {}".format(','.join(data)))
#         csv_writer.writerow(data)
