total=0
lista=[]
def demo(): 
    items={"idli":5,"dosa":20,"poori":20,"pongal":20}
    i=input("enter item")
    nos=int(input("no of qty= "))
    
    t=items[i]
    t=t*nos
    lista.append(t)
    n=int(input("enter 1 for next item\nenter 2 for complete bill"))
    if n==1:
        demo()
    elif n==2:
        import functools
        total=functools.reduce(lambda a,b:a+b,lista)
        print(lista)
        print("your total bill",total)
        return 
demo()

