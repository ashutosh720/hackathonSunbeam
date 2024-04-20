from Blog.Blog import Blog

user_list=[]
class User:
    def __init__(self, uid,name, email, password, phone, address,date ,bid=None, title=None, content=None, category=None):
        self.uid = uid
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address
        self.date = date
        self.blogs = [Blog(bid, title, content, category)]

    def add_blog(self, bid, title,content,category):
        self.blogs.append(Blog(bid,title,content,category))

    def print(self):
        print(f"{self.name} ,{self.email} ,{self.password} ,{self.phone} ,{self.address} ,{self.date}")






def login_user(name, email, password):
    guser = None

    for user in user_list:
        if (user.name == name and user.email == email and user.password == password):
            print(f"You are logged in as {user.name}")
            guser = user
        else:
            print("Invalid user name id")
    return guser

def register_user(user):
    user_list.append(user)

