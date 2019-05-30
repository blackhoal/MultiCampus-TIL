from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/mulcam")
def mulcam():
    return "This is Multicampus!"

@app.route("/greeting/<string:name>")
def greeting(name):
    return f'반갑습니다, {name}님!'

@app.route("/cube/<int:num>")
def cube(num):
    result = num ** 3
    return f'result'

# 특정 사람 수만큼 점심 메뉴 추천
# <int:people>

@app.route("/lunch/<int:people>")
def lunch(people):
    menu = ['돈까스', '피자', '치킨', '제육볶음']
    return str(random.sample(menu, people))
    # print(f"{i + 1}번 째 손님에게는 {random.choice(menu)}를 추천드립니다.")

@app.route("/html")
def html():
    multiple_String = """
        <h1>This is h1 tag!</h1>
        <p>This is p tag!</p>
    """
    return multiple_String

@app.route("/html_file")
def html_file():
    return render_template('html_file.html')

@app.route("/hi/<string:name>")
def hi(name):
    # Template Variable
    return render_template('h1.html', your_name=name)

@app.route("/menu_list")
def menu_list():
    menu = ['돈까스', '피자', '치킨', '제육볶음']
    return render_template('menu_list.html', menu_list=menu)

if __name__ == '__main__':
    app.run(debug=True)