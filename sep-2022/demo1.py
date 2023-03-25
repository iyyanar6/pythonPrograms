##print(("\t"),"I "*5)
##for i in range(0,5):
##    print(("\t"),"    I")
##print(("\t"),"I "*5)
for i in range(0,5):
    for j in range(0,5):
        if i>=j:
            print("*",end=" ")
    print(" ")
