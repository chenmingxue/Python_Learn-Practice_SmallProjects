#try, except flow demos
class Try_except:
    def f1(self):
        try:
            print("a")
        except:
            print("b")
        else:
            print("c")
        finally:
            print("d")

    def f2(self):
        try:
            print("a")
            raise Exception("doom")
        except:
            print("b")
        else:
            print("c")
        finally:
            print("d")

    def f3(self):
        try:
            print ("a")
            return
        except:
            print("b")
        else:
            print("c")
        finally:
            print("d")

a = Try_except()
print(a.f1())
print("*******")
print(a.f2())
print("*******")
print(a.f3())
