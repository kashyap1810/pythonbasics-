gross_salary=10000
health_insurance=430.99
rent=1200
food=400.5
salary_tax=0.2
donation_to_the_poor=0.1

tax_amount_in_money=gross_salary*salary_tax
net_salary=gross_salary-tax_amount_in_money-health_insurance-rent-food
print('net salary : ' +str(net_salary))

donation=donation_to_the_poor*net_salary
print('donation amount to the poor : ' +str(donation))