from Blog.Blog import Blog

user_list=[]
class User:
    def __init__(self, name, email, password, phone, address,date ,bid=None, title=None, content=None, category=None):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address
        self.date = date
        self.blog = [Blog(bid, title, content, category)]

    def print(self):
        print(f"{self.name} ,{self.email} ,{self.password} ,{self.phone} ,{self.address} ,{self.date}")






def login_user(name, email, password):
    for user in user_list:
        if (user.name == name and user.email == email and user.password == password):
            print(f"You are logged in as {user.name}")
        else:
            print("Invalid user name id")

def register_user(user):
    user_list.append(user)