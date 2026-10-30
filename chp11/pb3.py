class Employee:
    salary = 342
    increament = 45
    @property
    def salaryAfterincreament(self):
        return (self.salary + self.salary *(self.increament/100))
    @salaryAfterincreament.setter
    def salaryAfterincreament(self,salary):
        self.increament = ((salary/self.salary)-1)*100
r = Employee()
print(r.salary)
print(r.salaryAfterincreament)
r.salaryAfterincreament = 495.9
print(r.increament)