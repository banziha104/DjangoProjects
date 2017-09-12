from exampleDP import Duck

class RubberDuck(Duck):
    def display(self):
        print("Rubber Duck 입니다")

    def quack(self):
        print("ㄱ삐이이익")

if __name__ == "__main__":
    duck = RubberDuck()
    duck.display()
    duck.quack()