def display(**kwargs):
    for key, value in kwargs.items():
        print(key, "->", value)

display(name="Ronak", age=20, course="CSE")