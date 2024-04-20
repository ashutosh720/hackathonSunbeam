


class Blog:

    def __init__(self, bid, title, content, category):
        self.bid = bid
        self.content = content
        self.category = category
        self.title = title


    def print(self):
        print(f"{self.bid} , {self.title} , {self.content} , {self.category}")
