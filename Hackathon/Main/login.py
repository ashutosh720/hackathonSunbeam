# if __name__ == "__main__":
import datetime

from Main.main_menu import main_menu
from User.User import User, register_user, user_list, login_user

all_blogs=[]
def login_page():
    while(True):
        print("Welcome to Blogger")
        print("1.Login")
        print("2.Register")
        print("3.Blog")
        print("0.Exit")

        choice = int(input("Enter your choice \n"))


        if(choice == 1):

            name = input("Enter your name")
            email = input("Enter your email")
            password = input("Enter the password")
            guser = login_user(name,email,password)
            main_menu(guser)


        elif(choice == 2):
            id = int(input("Enter the uid"))
            name = input("Enter your name")
            email = input("Enter your email")
            password = input("Enter the password")
            phone = input("Enter the phone number")
            address = input("Enter the address")

            user = User(id,name,email,password,phone,address,datetime.datetime.now())
            register_user(user)
            print("User registered successfully")


        elif(choice == 3):
            for user in user_list:
                print(user.print())


        else :
            break


login_page()