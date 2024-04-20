from Blog.Blog import Blog

all_blogs = []


def main_menu(user):
    print("1.Show Category")
    print("2.Add Category")
    print("3.Create Blog")
    print("4.Display All Blogs")
    print("5.Show My Blogs")
    print("6.Delete Blogs")
    print("7.Read Blog Contents")
    print("8.Edit Blog")
    print("9.Search Blog")
    print("Logout")

    choice = int(input("Enter your choice"))

    if (choice == 3):
        bid = int(input("Enter the blog id"))
        category = input("Enter the category")
        title = input("Enter the title")
        content = input("Enter the content")
        blog = Blog(bid, title, content, category)
        all_blogs.append(blog)
        user.add_blog(bid, category, title, content)

    elif choice == 4:
        for blog in all_blogs:
            print(blog.print())
