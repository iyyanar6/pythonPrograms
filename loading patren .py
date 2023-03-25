import os
import time
os.system("colour 0c")
for i in range(101):
    print("█"*i,f"{i}%")
    time.sleep(0.001)
    if i!=100:
        os.system("cls")

input("done...")
        
