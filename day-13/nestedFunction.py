def f():
    def g():
        print("inside function g :")
    g()
    print("insdie function f :")
f()