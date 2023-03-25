##user=[{"name":"python","skils":["reading","writting","easy to access"]},{"name":"java","skils":["reading","writting","easy to access"]}]
##for i in range(0,len(user)):
##    print(i+1,".",user[i]["name"])
##    n=user[i]["skils"]
##    
##    for j in range(0,len(n)):
##        print("  ",j+1,".",n[j])

c=0
w=0
skip=0


user=[{"qustion":"how many months in a year","option":["23","13","12"],"ans":"12"},{"qustion":"what is square of 10  ","option":["10","100","1000"],"ans":"100"},{"qustion":"what is square of 5  ","option":["25","50","5"],"ans":"25"}]
for i in range(0,len(user)):
    a=65
    print(i+1,".",user[i]["qustion"])
    n=user[i]["option"]
    
    for j in range(0,len(n)):   
        print("  ",chr(a),".",n[j])
        a+=1
        answer={"A":user[i]["option"][0],"B":user[i]["option"][1],"C":user[i]["option"][2]}
    ans=input("you don't know ans enter space bar\nenter your option= ")
    if ""==ans:
        skip+=1 
    elif user[i]["ans"]==answer[ans]:
        c+=1
    else:
        w+=1
print("correct=",c)
print("wrong=",w)
print("skip=",skip)




