# closure function and function factory
# example 1:
def outer():
    x=3
    def inner(y):
        return x+y
    return inner

i = outer()
print(i)

print(i(y=2))

# example 2:
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2)
print(square.__closure__)
print(square(4))
 
# example 3: change variable to nonlocal
import time
def make_timer():
    #only works in init state, in later call, it has no effect
    last_called = None 
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result
    return elapsed

t1 = make_timer()

t2 = make_timer()

print(t1)

print(t2)

#t1 and t2 has no inteference
