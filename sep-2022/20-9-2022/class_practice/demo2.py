class demo:
    name="iyyanar"
    age=24
    sex="male"
    def play(s):
        print("i can play")
    def read(s):
        print("i can read")
d1=demo()
print(d1.name)
print(d1.age)
d1.age=25
print(d1.age)
print(d1.sex)
print(d1.play())
print("")

d2=demo()
d2.name="sam"
print(d2.name)
d2.age=34
print(d2.age)
print(d2.sex)
print(d2.read())
