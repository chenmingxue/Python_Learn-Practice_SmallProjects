def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined

def foo2():
    a=200 #only work in this function
    print(a)

if __name__ == '__main__':
    a = 100 #globale viable
    # print(b)  # NameError: name 'b' is not defined
    print("****local/globle variable****")
    print('****foo demo****')
    foo()
    print('****foo2 demo****')
    foo2()
    print(a) #from global
