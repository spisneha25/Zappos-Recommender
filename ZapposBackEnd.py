'''
It functions as the backend. Once the data is fetched by the ZapposApi program,
the cost of products are contained in product_costs and name of products are
contained in product_costs. The recursive function:finderList implements
the subset sum logic modifying it to stop when the number of items exceeds
users desired #no. of products.

`final_items` contains the sorted list which is a sequence of products
and their total cost
'''
import operator
final_cost = []
final_name = []
Quantity = 0
Cost = 0

#Set value of items defined by user
def set_quantity(q):
    global Quantity
    Quantity = q

#Set value of cost target defined by user    
def set_cost(c):
    global Cost
    Cost = c

#Finds list of items fitting criteria
#Sorts them in descending order of their cost
def callFinder(product_costs, product_names):
    finderList(product_costs, product_names)
    for i in range(len(final_name)):
        final_name[i].append(sum(final_cost[i]))
    final_items = sorted(final_name, key = operator.itemgetter(Quantity), reverse = True)
    return final_items

#Recursive function to compute combination of items matching the criteria    
def finderList(prices, names, partial_p = [], partial_n = []):
    s = sum(partial_p)

    if s <= Cost:
        if len(partial_p) == Quantity:
            final_cost.append(partial_p)
            final_name.append(partial_n)
            return
    if s >= Cost:
        return  

    for i in range(len(prices)):
        n = prices[i]
        m = names[i]
        remaining_costs = prices[i+1:]
        remaining_names = names[i+1:]
        finderList(remaining_costs, remaining_names, partial_p + [n], partial_n + [m]) 
    
