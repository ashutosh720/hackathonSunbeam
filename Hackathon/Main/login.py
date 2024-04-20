# if __name__ == "__main__":
import datetime

from User.User import User, register_user, user_list, login_user


def login_page():
    while(True):
        print("Welcome to Blogger")
        print("1.Login")
        print("2.Register")
        print("0.Exit")

        choice = int(input("Enter your choice \n"))


        if(choice == 1):
            name = input("Enter your name")
            email = input("Enter your email")
            password = input("Enter the password")
            login_user(name,email,password)


        elif(choice == 2):
            name = input("Enter your name")
            email = input("Enter your email")
            password = input("Enter the password")
            phone = input("Enter the phone number")
            address = input("Enter the address")

            user = User(name,email,password,phone,address,datetime.datetime.now())
            register_user(user)
            print("User registered successfully")
            for user in user_list:
                print(user.print())

        else :
            break


login_page()