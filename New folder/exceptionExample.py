##try:
##    a=int(input("enter a number: "))
##    c=a/0
##except ValueError:
##    print("enter only integer values")
##except ZeroDivisionError:
##    print(" any number divided by zero gives infinite")
##except Exception:
##    print("error occurs")
##else:
##    print("a value is ",a)
##finally:
##    print("program completed successfully")


try:
    a=int(input("enter a number: "))
    if(a>100):
        raise Exception("a value is greater than 100")
    else:
        print("a is less than 100")
except Exception as e:
  print(e)



##
####raise Exception
##
##a=int(input("enter a number: "))
##if(a>100):
##    raise Exception()
##else:
##    print("a is less than 100")
