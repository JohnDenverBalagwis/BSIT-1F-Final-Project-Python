print("===================================================")
print(" WELCOME TO BALAGWIS/RIOFLORIDO ATM SYSTEM")
print("===================================================")
userpin, balance = 0, 1
myDict = {'cardo dalisay': [1234, 5000], 
            'Son Guko': [1324, 1000], 
            'Meliodas': [1111, 2000], 
            'Naruto Uzumaki': [2222, 5000], 
            'Sasuke Uchia': [3333, 1000], 
            'Shikamaru Nara': [1432, 2000], 
            'Natsu Dragneel': [0000, 5000], 
            'Tetsuya Koruko': [1010, 1000], 
            'Liza Soberano': [7777, 2000], 
            'Johnny Sin': [6666, 6666]}


username = (input("ENTER YOUR NAME: "))
try:
    if(username in myDict):
        userpin = int(input("ENTER YOUR 4 DIGITS PIN NUMBER: "))
    if(userpin == myDict[username][0]):
        balance = myDict[username][1]
        while True:
                print("""
        1.BALANCE
        2.DEPOSIT BALANCE
        3.WITHDRAW BALANCE
        4.EXIT
        """)

                try:   
                    option = int(input("PLEASE ENTER YOUR CHOICE: "))
                except:
                    print("PLEASE ENTER VALID OPTION")
                
                if option >= 5:
                    print("PLEASE ENTER VALID OPTION")
                
                if option == 1:
                    print(f"YOUR CURRENT BALANCE IS: {balance}")
                                    
                if option == 2:
                    deposit_amount = int(input("PLEASE ENTER THE AMOUNT OF MONEY YOU WANT TO DEPOSITE: "))
                    balance = balance + deposit_amount
                    print(f"{deposit_amount} IS CREDITED TO YOUR ACCOUNT")
                    print(f"YOUR UPDATED BALANCE IS: {balance}")
           
                if option == 3:
                    withdraw_amount = int(input("PLEASE ENTER THE AMOUNT OF MONEY YOU WANT TO WITHDRAW: "))
                    if (withdraw_amount >= balance):
                        print("Not Enough Balance, You should atleast leave P 1 pesos in your balance.")
                    else:
                        balance = balance - withdraw_amount
                        print(f"{withdraw_amount} IS DEDUCTED FROM YOUR ACCOUNT")
                        print(f"YOUR UPDATED BALANCE IS: {balance}")


                if option == 4:
                    break
    else:
        print("Wrong Pin Number")
        print("PLEASE TRY AGAIN!")
except:
    print("INVALID DATA")
    print("PLEASE TRY AGAIN!")
else: 
    print("===================================================")
    print("Thank you for using BALAGWIS/RIOFLORIDO ATM System")
    print("===================================================")
