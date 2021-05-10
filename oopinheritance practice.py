class Employee:
    def __init__(self, years_of_experience, position_name, employee_name):
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name

    @property
    def calculate_salary(self):
        base_salary = 2500
        calculated_salary = 0
        if 0 < self.years_of_experience <= 2:
            calculated_salary = base_salary + 1500
        elif 2 < self.years_of_experience <= 5:
            calculated_salary = base_salary + 2500
        elif self.years_of_experience > 5:
            calculated_salary = base_salary + 3500
        else:
            print('wrong value inserted')

        print('the calculated salary is %s '%calculated_salary)
        return calculated_salary

    def candidate_bonus(self, the_calculated_salary):
        salary_with_bonus = 0
        if 'front end' in self.position_name:
            salary_with_bonus = the_calculated_salary * 1.1
        if self.years_of_experience > 2:
            salary_with_bonus = the_calculated_salary * 1.2
        print('the bonus for the position %s is : %s '%(self.position_name,salary_with_bonus))


class programmer(Employee):
    def __init__(self, years_of_experience, position_name, employee_name):
        super().__init__(years_of_experience, position_name, employee_name)
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name

    def print_data(self):
        print('the employee %s work as %s in our company' % (self.employee_name, self.position_name))


junior_python_programmer = programmer(1, 'front end', 'joseph')
calculated_salary_value = junior_python_programmer.calculate_salary
junior_python_programmer.candidate_bonus(calculated_salary_value)
junior_python_programmer.print_data()

# excuting methods

senior_dev = programmer(6, 'front end', 'ravi')
calculated_salary_value = senior_dev.calculate_salary
senior_dev.candidate_bonus(calculated_salary_value)
senior_dev.print_data()
