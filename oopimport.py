#create a object

class Building():
    def __init__(self,season_in_year,apartment_number,apartment_size):
        self.season_in_year=season_in_year
        self.apartment_number=apartment_number
        self.apartment_size=apartment_size

    def rent_calculation(self):
        base_price_per_month=2000
        season_price_buffer=0

        if self.season_in_year=='summer':
            season_price_buffer=1.5

        elif self.season_in_year=='spring':
            season_price_buffer=1.4

        else:
            season_price_buffer= None

            if self.apartment_size>130:
                season_price_buffer+=0.1

        total_rent_value = base_price_per_month * season_price_buffer


        print('the total price is %s' %total_rent_value)

        print('the buffer is %s' %season_price_buffer)

        return total_rent_value

    def monthly_maintainenece(self,rent_value):

        maintainence=0
        if rent_value>3000:
            maintainence=100
        else:
            maintainence=50
        print('the maintainence is :  %s '%maintainence )

lease_contract_1=Building('summer',4,135)

rent_value1=lease_contract_1.rent_calculation()#passing a variable rent_price inside the  method
lease_contract_1.monthly_maintainenece(rent_value1)


print('\n')
lease_contract_2=Building('spring',7,100)

rent_value2=lease_contract_2.rent_calculation()
lease_contract_2.monthly_maintainenece(rent_value2)




print('***************************************************************')

