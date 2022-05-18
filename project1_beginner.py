from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl.workbook import Workbook

website = "https://books.toscrape.com/"
resp = requests.get(website)
#print(resp.status_code)

soup = BeautifulSoup(resp.content, parser="html.parser", features="lxml")
# books = soup.findAll(class_="side_categories")
# print(books)

#product  tile of the books
result = soup.find_all('li',{'class' : "col-xs-6"})
product = result[0]
# print(product.find('h3').find('a').get('title'))
# print(product.find('p', {"class":"price_color"}).get_text())
# print(product.find('p', {"class":"instock availability"}).get_text().strip())
title = []
prices = []
stock = []
for i in result:
    title.append(i.find('h3').find('a').get('title'))
    prices.append(i.find('p', {"class": "price_color"}).get_text( ))
    stock.append(i.find('p', {"class": "instock availability"}).get_text( ).strip( ))
book_info =pd.DataFrame({"Name": title, "Price": prices,"Stock_Availability": stock})

print(book_info)
# saving into excel file
book_info.to_excel("books_result_done.xlsx")


#product price of the books
# product availability of the books

