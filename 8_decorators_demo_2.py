# decorators demo - 2
# example 1: with wrap function
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def remove_special_char():
    return 'blomkÒ'

remove_special_char()


# example 2:

class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)
    
@CallCount
def hello(name):
    print('Hello, {}'.format(name))

hello('Ann')
hello('Luke')
print(hello.count)

# example 3: multi decrators
class Trace:
    def __init__(self):
        self.enabled = True
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

tracer = Trace()
@tracer
@escape_unicode
def remove_special_char():
    return 'hello ' + 'blomkÒ'

# call remove_special_char() -> escape_unicode -> tracer

remove_special_char()
tracer.enabled = False
remove_special_char()
# see the print difference, we can control by decrator value










