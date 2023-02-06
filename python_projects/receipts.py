#furniture description
lovely_loveseat_description = '''Lovely Loveseat.
Tufted polyester blend on wood.
32 inches high x 40 inches wide x 30 inches deep.
Red or white.'''

stylish_settee_description = '''Lovely Loveseat.
Tufted polyester blend on wood.
32 inches high x 40 inches wide x 30 inches deep.
Red or white.'''

luxurious_lamp_description = '''Luxurious Lamp.
Glass and iron.
36 inches tall.
Brown with cream shade.'''

#furniture prices
lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15

#sales tax
sales_tax = .088

#customers
customer_one_total = 0
customer_one_itemization = ""

#customer purchases
customer_one_total += lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization += lovely_loveseat_description + luxurious_lamp_description

#tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax
rounded_total = round(customer_one_total, 2)

#receipt printing
print('Customer One Items:')
print(customer_one_itemization)
print()
print('Customer One Total:')
print(rounded_total)
