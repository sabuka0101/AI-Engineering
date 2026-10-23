# Task 1
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

#     @property
#     def salary(self):
#         return self.__salary

#     @salary.setter
#     def salary(self, new_salary):
#         if new_salary < 0:
#             print("Salary can't be negative!")
#             return
#         self.__salary = new_salary

#     @salary.deleter
#     def salary(self):
#         print(f"{self.name}'s salary was deleted")
#         del self.__salary


# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def get_info(self):
#         print(
#             f"Name: {self.name} | Department: {self.department} | Salary: {self.salary}"
#         )


# manager = Manager("Saba", 5000, "IT")
# manager.get_info()

# manager.salary = -100
# manager.salary = 6000
# manager.get_info()

# del manager.salary


# Task 2
# class Payment:
#     def process_payment(self, amount):
#         print(f"Processing payment of {amount} GEL...")


# class CreditCardPayment(Payment):
#     def process_payment(self, amount):
#         print(f"Paid {amount} GEL with credit card")


# class PayPalPayment(Payment):
#     def process_payment(self, amount):
#         print(f"Paid {amount} GEL with PayPal")


# payments = [Payment(), CreditCardPayment(), PayPalPayment()]

# for payment in payments:
#     payment.process_payment(100)


# Task 3
class SmartDevice:
    def __init__(self, brand):
        self.brand = brand
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True
        print(f"{self.brand} device is ON")

    def turn_off(self):
        self.__is_on = False
        print(f"{self.brand} device is OFF")

    @property
    def is_on(self):
        return self.__is_on


class SmartLight(SmartDevice):
    def __init__(self, brand, brightness):
        super().__init__(brand)
        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            print("Brightness must be between 0 and 100, setting it to 50")

    def turn_on(self):
        super().turn_on()
        print(f"Brightness: {self.brightness}%")


light = SmartLight("Philips", 80)
print(light.is_on)

light.turn_on()
print(light.is_on)

light.turn_off()
print(light.is_on)
