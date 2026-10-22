class Student:

    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("Object Destroyed")


s1 = Student()

del s1