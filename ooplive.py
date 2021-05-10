class Car():
    def __init__(self, car_data_list):
        self.car_data_list = car_data_list

    def insurance_calculation(self):
        year_of_release = self.car_data_list[0]
        car_price = self.car_data_list[1]
        model = self.car_data_list[2]

        if 2020 >= year_of_release >= 2010 and 6000 <= car_price <= 17000:
            calculated_insurance = car_price * 0.5
        else:
            calculated_insurance = car_price * 0.7
        print('calculated insurance of %s: %s ' % (model, calculated_insurance))

    def doors_closed(self):
        door_status = self.car_data_list[-1]
        if door_status == True:
            print('doors are closed')
        elif door_status == False:
            print('doors are open')
        else:
            print('wrong value inserted')

    def car_data(self):
        print(f'the car model is '.format(self.car_data_list[2], self.car_data_list[0], self.car_data_list[1]))


ford_focus_list = [2005, 5000, 'ford_focus', True]

ford_focus_instance = Car(ford_focus_list)

ford_focus_instance.insurance_calculation()
ford_focus_instance.doors_closed()
ford_focus_instance.car_data()

print('\n')
audi_a3_list = [2011, 15000, 'audi_a3', False]

audi_a3_instance = Car(audi_a3_list)
audi_a3_instance.insurance_calculation()
audi_a3_instance.doors_closed()
audi_a3_instance.car_data()
