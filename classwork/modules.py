data={
    '1234':{"balance":45678,"pin":123,"history":[]},
    '5673':{"balance":75333,"pin":123,"history":[]},
    '9833':{"balance":34566,"pin":123,"history":[]},
    '4673':{"balance":46786,"pin":123,"history":[]},
    }
acc_num=None
login_status=False
def welcome():
    print("welcome to ATM.center(-*40)")
def menu():
    print("1.login")
    print("2.check_balance")
    print("3.deposit")
    print("4.withdraw")
    print("0.exit")
def login(acc,pin):
    if acc in  data:
        if acc[data]['pin']==pin:
            global acc_num
            global login_status
            acc_num=acc
            login_status=True
            print("Login Succesuful")
    else:
        print("invalid login")
def check_balance():
    if login_status and acc_num:
        print("current Balance:{data[acc_num]['balance]}")
    else:
        print("login again")
def deposit():
    if login_status and acc_num:
        amount=int(input("Enter the amount to deposit: "))
        data[acc_num]['balance']+=amount
        data[acc_num]['history'].append(f'Deposited :${amount}')
        print(f"{amount} is successfully deposit")
    else:
        print("not deposited")
def Withdraw():
    if login_status and acc_num:
        amount=int(input("Enter the amount to withdraw:"))
        data[acc_num]['balance']-=amount
        data[acc_num]['history'].append(f"Withdraw :${amount}")
        print(f"{amount} is successfuly Withdraw")
    else:
        print("sufficient balance")
def veiw_transcation():
    if login_status and acc_num:
        
