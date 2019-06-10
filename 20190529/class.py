class Person:
    name = '사람의 고유한 속성'
    age = '출생 이후부터 삶을 마감할 때까지의 기간'

    def greeting(self):
        print(f'{self.name}이 인사합니다. 안녕하세요.')

    def eating(self):
        print(f'{self.name}이 식사합니다.')

    def aging(self):
        print(f'{self.name}은 현재 {self.age}세이고 현재 나이를 먹어가는 중입니다.')

jason = Person()
print(jason.name)
print(jason.age)
jason.name = 'jason'
jason.age = 19
print(jason.name)
print(jason.age)
jason.greeting()
jason.eating()
jason.aging()