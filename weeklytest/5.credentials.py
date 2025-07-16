credentials=("admin", "python123")
user=input()
password=input()
if credentials[0]==user and credentials==password:
    print("Login Successful")
else:
    print("Access Denied")