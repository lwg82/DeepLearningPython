


# 
print("I am hungry!")

# 定义类
class Man:
    def __init__(self, name):
        self.name=name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name)

    def goodbye(self):
        print("Good bye " + self.name)


m = Man("lee")
m.hello()
m.goodbye()



