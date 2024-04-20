import datetime
class Category:
    def __init__(self, title, desc_reg):
        self.title = title
        self.desc_reg = desc_reg
        self.Cat_list = []

    def add_category(self, category):
        self.Cat_list.append(category)

    def show_category(self):
            print(f"{self.title},{self.desc_reg},{datetime.datetime.now()}")


def main():
    cat_list = []
    while True:
        print("\nMenu:")
        print("1. Add category")
        print("2. Show Categories")
        ch = input("Enter your choice: ")

        if ch == '1':
            title = input("Enter category title: ")
            desc_reg = input("Enter category description: ")
            category = Category(title, desc_reg)
            cat_list.append(category)
            print(f"{title} added successfully!")

        elif ch == '2':
            if cat_list:
                for cat in cat_list:
                    cat.show_category()
            else:
                print("No categories added yet.")

if __name__ == "__main__":
    main()