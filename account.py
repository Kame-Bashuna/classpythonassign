
class Account:
    def __init__(self, number, pin, customer_name):
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.customer_name = customer_name


    def show_balance(self,pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Input wrong pin"


    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} has been deposited in your account.")



    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"{amount} has been withdrawn from your account.")


    def check_balance(self):
        print(f"Hi,{self.customer_name} your Current balance is {self.__balance}.")


    def customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.number)
        print(f"Balance: {self.__balance}\n")


    def update_customer_details(self, new_name, new_number, new_pin):
        self.customer_name = new_name
        self.number = new_number
        self.__pin = new_pin


























