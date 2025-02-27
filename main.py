import feepending
import feepaid
import otp

admin_username = input("Enter User name: ")
if admin_username == "admin":
    otp = otp.send_otp("vamshiburra11@gmail.com")
    x = int(input("Enter OTP: "))
    if x == otp:
        print("Login Sucess !")
    else:
        print("Login Failed !")
        exit()
else:
    print("Invalid Username")
    exit()

userdetails = {
    101 : ["vamshi","vamshiburra11@gmail.com","false"],
    102 : ["Shashi","shashi2028j@gmail.com","false"],
    103 : ["Poojitha","kodudhulapoojitha19@gmail.com","false"],
    104 : ["harshitha","harshithamudhiraj16@gmail.com","false"],
    105 : ["Manohar","reddymanohar894@gmail.com","true"]
    }
print("Welcome Admin")
while True:
    print("Choose your Option")
    print("1. Edit Information")
    print("2. Send mail to Fee Pending users")
    print("3. Send mail to Fee cleared users")
    print("4. Exit")
    x1 = int(input("Enter option: "))
    if x1 == 1:
        for user in userdetails:
            if userdetails[user][2] == "false":
                status = input(f"Enter the Status of {userdetails[user][0]}: ")
                userdetails[user][2] = status.lower()
                print(f"{userdetails[user][0]} Data Updated !")
        else:
            print("Data Edited")
    elif x1 == 2:
        res = []
        for user in userdetails:
            if userdetails[user][2] == "false":
                res.append([userdetails[user][0],userdetails[user][1]])
        feepending.send_mails(res)
        print("All mails sent to Fee pending users")
    elif x1 == 3:
        res = []
        for user in userdetails:
            if userdetails[user][2] == "true":
                res.append([userdetails[user][0],userdetails[user][1]])
        feepaid.send_mails(res)
        print("All mails sent to fee Cleared users !")
    else:
        print("Thank You")
        print("visit again")
        break
        
