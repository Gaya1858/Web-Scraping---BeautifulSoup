from bs4 import BeautifulSoup
import requests
import html.parser

website = "http://automationpractice.com/index.php?id_category=3&controller=category" # website link to scrap
# get request
resp = requests.get(website)
print(resp.status_code)
# status codes:
# Informational responses (100–199)
# Successful responses (200–299)
# Redirection messages (300–399)
# Client error responses (400–499)
# Server error responses (500–599)

# soup object , 1 arg . response.content(), 2 arg. python's html parser
soup_object = BeautifulSoup(resp.content, parser="html.parser", features="lxml")

# find by id
contact_us = soup_object.find(id ="columns").get_text().replace('\n','')
#print(contact_us)
contact_us_2 = soup_object.find(id ="contact-link").find('a')

#print(contact_us_2)
# find by class
cl_list =soup_object.find(class_ = "ajax_block_product").find(class_ = "content_price")
print(cl_list)
lis = soup_object.findAll(class_ = "ajax_block_product")
print(lis[1].get_text()) # lis has 7 items and you can use array index get and .gt_text returns just texts from the content

# SELECT_ONE() WITH CLASS
# select_one() by css selector -return first element- equivalent to find()
css_lis = soup_object.select_one(".shop-phone").get_text().strip().replace("Call us now: ","") # .uses for css selector
print(css_lis)

#SELECT_ONE() WITH ID if you use select() - findAll()
css_lis1 = soup_object.select_one("#contact-link").get_text().strip()# # uses for css selector
print(css_lis1)

# extract by attribute values
#itemprop is an attribute of html
print(soup_object.find(itemprop ="name").find('a').get_text().lstrip())
print(soup_object.find(itemprop ="name").find('a').get('title'))

# navigate to Siblings to parent
print(soup_object.select_one('.ajax_block_product').find_next_sibling().select_one(".product-name").get_text().strip())
#print(soup_object.select_one('.ajax_block_product').find_parent())

list_all = soup_object.select('.ajax_block_product')
for i in list_all:

    print(i.select_one(".product-name").get_text( ).strip( ))
    print('\t')
    print(i.select_one(".content_price").get_text().strip())

# extract links and URL
print(soup_object.find(id="contact-link").find('a')['href']) # http://automationpractice.com/index.php?controller=contact
link_variable = soup_object.findAll(itemprop='name')
for i in link_variable:
    print(i.find('a')['href'])

# find elements - alternative syntax
print(soup_object.find('div', {"id":"contact-link"}))
print(soup_object.find('a', {"class":"subcategory-name"}).get_text().strip())





