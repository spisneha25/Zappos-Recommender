Zappos-Challenge
================
The repository contains two files: 
ZapposApi and ZapposBackEnd 
The ZapposApi.py mainly accesses the api and searches for products whose value is lesser than the cost mentioned by the user. 
It uses the price facet provided by the Zappos api. Once, products have been extracted, they are passed on to the callFinder 
function of ZapposBackEnd.py. This inturn makes call to the finderList function which is a recursive function implementing the 
subset-sum method for two criteria: cost target and number of prducts. The list computed is returned back to the callFinder 
which sorts the list based on the total cost value of products selected and returns the new sorted list. The ZapposApi function 
then displays this list, 10 at a time. 
Here, limit value is set to 100. 

