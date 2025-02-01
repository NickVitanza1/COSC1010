#
# Nicholas Vitanza
# 1/31/25
# Sales Tax Programming Project
# COSC 1010
#

# Variable declarations

# Constants for the state and county tax rates

# Get the amount of the purchase.
purchase_amount = float(input('Enter the amount of the purchase: '))
# Calculate the state sales tax.
state_sales_tax = purchase_amount * 0.05
# Calculate the county sales tax.
county_sales_tax = purchase_amount * 0.025
# Calculate the total tax.
total_sales_tax = state_sales_tax + county_sales_tax
# Calculate the total of the sale.
total_sale_amount = purchase_amount + total_sales_tax
# Print information about the sale.
print('The sale is $, sale')