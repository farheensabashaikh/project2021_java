
product1_name,product1_price='Laptop',1000
product2_name,product2_price='Phone',2000
product3_name,product3_price='SSD',200
product4_name,product4_price='Hade Phone',800
product5_name,product5_price='Printer',3500
product6_name,product6_price='Keyboard',500
# create a company name and information
company_name = 'Electronic store'
company_address = 'Solapur'

message = 'Thanks for shopping.'
print('*' * 50)

# print company information first using format
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('=' * 50)

# print out header for section of items
print('\tProduct Name\tProduct Price')
print("-"* 50)

# create a print statement for each item
print('\t{}\t\t${}'.format(product1_name.title(), product1_price))
print('\t{}\t\t${}'.format(product2_name.title(), product2_price))
print('\t{}\t\t${}'.format(product3_name.title(), product3_price))
print('\t{}\t${}'.format(product4_name.title(), product4_price))
print('\t{}\t\t${}'.format(product5_name.title(), product5_price))
print('\t{}\t${}'.format(product6_name.title(), product6_price))
# print a line between sections
print('=' * 50)

# print out header for section of total
print('\t\t\tTotal')

total = product1_price + product2_price + product3_price + product4_price + product5_price + product6_price
print('\t\t\t${}'.format(total))

print('=' * 50)

# output thank you message
print('\n\t{}\n'.format(message))

# create a bottom border
print('*' * 50)