class Account:
    def __init__(self):
        print("Enter Account Holder details below:\n")
        #self.c = 0


    def set_details(self):
        self.acc_number = int(input("Account Number:"))
        self.name = input("Account Holder's Name: ")
        self.current_balance = float(input("Current Balance: "))

        self.type = input("Type of Account: ")
        #self.money_deposited=[]
        #self.money_withdrawn=[]
        self.money_balance=[]
        self.no_of_operations=0
        self.no_of_operations += 1
        self.money_balance.append(self.current_balance)

   # def typeof_acc(self):
        #self.type = input("Type of Account: ")


    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.current_balance += amount
        self.no_of_operations+=1
        self.money_balance.append(self.current_balance)
        print("\n Amount deposited: %.2f" % amount)

    def draw_money(self):
        amount = float(input("enterv the amount to be withdrawn: "))
        if self.current_balance >= amount:
            self.current_balance -= amount
            self.no_of_operations+=1
            self.money_balance.append(self.current_balance)
            print("\n You Withdrew: %.2f" % amount)

        else:
            print("\n Insufficient balance !! ")
    def display(self):
        print(" Accont Number: ", self.acc_number)
        print("Account Holder's Nmae: ",self.name)
        print("Current Balace: %.2f" %self.current_balance)
        print("Account Type: ", self.type)
    def modify(self):
        print("enter the data to be modified:\n")
        self.name = input("Account Holder's Name: ")
        self.type = input("Type of Account: ")
    def get_account_number(self):
        return self.acc_number
    def get_balance(self):
        return self.current_balance
    def get_type(self):
        return self.type
    def report(self):
        print(" BALANCE     OPERATION       CURRENT")
        for i in range(self.no_of_operations-1):
            print("%10.2f   %10.2f    %10.2f"%(self.money_balance[i],self.money_balance[i+1]-self.money_balance[i],self.money_balance[i+1]))


if __name__ == '__main__':


    user = Account()
    user.set_details()
    while True:
        comment = input("do you want to \n1)deposit or \n 2)withdraw \n 3)show current balance \n 4)print report ? : ")
        if comment == '1':
            user.deposit()

        elif comment == '2':
            user.draw_money()
        elif comment== '3':
            print("Your current balance: ",user.get_balance())
        elif comment=='4':
            user.report()
            break

        else :
            print("Invalid entry!!")


    user.display()