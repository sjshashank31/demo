def decorate(func):
    def inner(a,b):
        if a<b:
            a, b = b, a
        func(a,b)
    return inner

@decorate
def div(a,b):
    print(a/b)

@decorate
def sub(a,b):
    print(a-b)

sub(1,4)
div(3, 9)


