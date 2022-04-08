# rented movies- each movie is 3 dollars a day
# little mermaid- 3 days
# brother bear- 5 days
# hercules- 1 day 
# find how much you will have to pay 

from operator import truediv


movies = [
    {'name':'the little mermaid', 'days': 3},
    {'name':'brother bear', 'days': 5},
    {'name':'hercules', 'days': 1}
]


total_price = sum([m['days']*3 for m in movies])

print('the total price is $' + str(total_price))


# 2 
# contractor for amazon, google, facebook
#google pays 400 per hour
#amazon pays 380 per hour 
#facebook pays 350 per hour 

goo_pay= 400
ama_pay= 380
fac_pay = 350
goo_hour= 6 
ama_hour= 4
fac_hour = 10

total_pay = goo_pay * goo_hour + ama_pay * ama_hour + fac_pay * fac_hour

print('The total pay is $' + str(total_pay))


#3
# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

is_not_full = True
no_conflicts = True

can_enroll = is_not_full and no_conflicts

if can_enroll == True:  
    print('This student can enroll')
else:
    print('This student cannot enroll')


#4
# A product offer can be applied only if people buys more than 2 items
# and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

premium_member = True
items_more_than_2 = True
offer_valid = True

product_offer= (
    offer_valid and items_more_than_2) or (
    offer_valid and premium_member)

print( 'Eligible for product offer')



