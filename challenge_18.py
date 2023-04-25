#shebang
#!/usr/bin/python3
from datetime import datetime

def greeting():

    name= input("Please enter your name.")
    day= datetime.now()

    print(f"Hello, {name}! Happy {day.strftime('%A')}!")
    
greeting()    

