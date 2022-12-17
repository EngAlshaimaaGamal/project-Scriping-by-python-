import requests
from bs4 import BeautifulSoup as bs
import csv
from itertools import zip_longest
name = []
price = []
shipping = []
Evaluation = []
url = requests.get("https://www.amazon.eg/s?k=lab+top&i=electronics&crid=1N961HIRJLKHI&sprefix=lab+%2Celectronics%2C242&ref=nb_sb_ss_ts-doa-p_1_4")
soup = bs(url.text, "html.parser")
lap_name = soup.find_all("span",{"class":"a-size-base-plus a-color-base a-text-normal"})
lap_price = soup.find_all("span", {"class": "a-price-whole"})
lap_shipping = soup.find_all("div", {"class": "a-row a-size-base a-color-secondary s-align-children-center"})
lap_evaluation = soup.find_all("a", {"class": "a-popover-trigger a-declarative"})
for i in range(len(lap_price)):
    name.append(lap_name[i].text)
    price.append(lap_price[i].text.replace(".\u200e","جنيه"))
    shipping.append(lap_shipping[i].text)
    Evaluation.append(lap_evaluation[i].text)

file_list = [name, price, shipping, Evaluation]
sho = zip_longest(*file_list)
with open("E:/myfile.csv", "w", encoding="utf-8") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["lab Name", "The Price", "Shipping", "Evaluation"])
    wr.writerows(sho)