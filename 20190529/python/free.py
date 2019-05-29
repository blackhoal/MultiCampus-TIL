import random
people = 5
for i in range(people):
    menu = ('돈까스', '피자', '치킨', '제육볶음')
    print(f"{i+1}번 째 손님에게는 {random.choice(menu)}를 추천드립니다.")