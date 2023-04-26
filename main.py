#Parent Class

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

#======================================
# johan = User("Johan", 21, "Male")
# johan.show_details()

#Child Class


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated: ", self.balance)

    def withdraw(self, amount):
        self.amount= amount
        if self.amount > self.balance:
            print("Insufficent fund || Available Balance: ", self.balance)

        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated || Available Balance:" , self.balance)

    def view_balance(self):
        self.show_details()
        print("Account Balance is ", self.balance)


johan = Bank("Johan", 20, "Male")
print(johan.age)
johan.deposit(1000)
johan.withdraw(200)
johan.show_details()
