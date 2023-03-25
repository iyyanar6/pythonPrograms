class television:
    brand="samsung"
    colour="black"
    price=30000
    size="32 inch"
    def quality(s):
        print("top quality brand")
    def game(s):
        print("we can play games")

tv1=television()
print(tv1.brand)
print(tv1.colour)
tv1.price=35000
print(tv1.price)

print("")
tv2=television()
tv2.brand="LG"
print(tv2.brand)
print(tv2.size)
print(tv2.price)

    
