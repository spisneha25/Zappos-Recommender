'''
An application of Subset-Sum problem to obtain combination of goods
that satisfy a target. N (desired # of products) and X (desired dollar amount)
is taken as input. It leverages the Zappos API using search feature and PriceFacet
create a list of Zappos products whose combined values match as closely as
possible to X dollars.

`cost_list` is a sequence of products and their total cost
which is the final output

'''
import ZapposBackEnd as Z
import json
import urllib, urllib2
from urllib2 import Request
        
price_list = {}
#Get user input for budget and quantity
cost = input('Enter your budget:')
quantity = input('Enter number of gifts:')
Z.set_cost(cost)
Z.set_quantity(quantity)

#No. of records to be fetched
limit = '100'

#Apply constraints on price for extracting data
count = cost / 50
costrestriction = '['
for i in range(count+1):
    costrestriction += '"$' + str((i+1)*50) + '.00 and Under"'
    if(i == count):
        costrestriction += ']' 
    else:
        costrestriction += ',' 

#Access API using key provided
url = 'http://api.zappos.com/Search?term=&filters={"priceFacet":' + costrestriction + '}&limit=' + limit + '&page=1&key=52ddafbe3ee659bad97fcce7c53592916a6bfd73'
requests = urllib2.Request(url)
responses = urllib2.urlopen(requests)
reads = responses.read()
data = json.loads(reads)

#Creating a dictionary of the form (StyleID : [price, productname]}
for d in data['results']:
    product = []
    product.append(float(d['price'].encode('utf-8').strip('$')))
    product.append(d['productName'].encode('utf-8'))
    price_list[d['styleId'].encode('utf-8')] = product

#Finding combination of products
cost_list = Z.callFinder([i[0] for i in price_list.values()], [j[1] for j in price_list.values()])

#displaying the list
t = 0
for c in cost_list:
    print("Items:")
    print(c[0:quantity])
    print("Total Cost:")
    print(c[quantity])
    t += 1
    if t == 10:
        raw_input('Press Enter Key To Continue...')
        t = 0
    
