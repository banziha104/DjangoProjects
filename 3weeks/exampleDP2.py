from exampleDP import Duck

class MallardDuck(Duck):
    def display(self):
        print("Mallard 오리 입니다")
    def quack(self):
        print("뺴애애애앵")

if __name__ == "__main__":
    duck = MallardDuck()
    duck.display()
    duck.quack()