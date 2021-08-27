class Person:
    # self는 python에서 생성자 또는 내부 함수 생성시 인자에 자신을 넘겨준다.
    def __init__(self, param_name):
        print("I'm created! ", self) # Person()이 호출되는 순간에 발동
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은 ", self.name, "입니다.")

person_1 = Person("유재석")
print(person_1.name)
print(person_1)
person_1.talk()
person_2 = Person("박명수")
print(person_2.name)
print(person_2)
person_2.talk()