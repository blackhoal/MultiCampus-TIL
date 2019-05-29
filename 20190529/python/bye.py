def hello(func):
        print('hi hi')
        func()
        print('hi hi')

@hello
def bye():
    print('bye bye')
