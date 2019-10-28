class Fruit(object):
    def __init__(self):
        print ("Fruit")
    def run_base(self):
        print ("Fruit run_base")

class Apple(Fruit):
    def __init__(self):
        print ("Apple")
    def run_base(self):
        print ("Apple run_base")
    def run_sub(self):
        print ("Apple run_sub")

fruit = Fruit()
fruit.run_base()

apple = Apple()
apple.run_base()
apple.run_sub()
