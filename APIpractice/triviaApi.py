#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?"

def main():
    
    numquests= int(input("How many questions would you like?\n>"))
    if numquests:
        numquests= f"amount={numquests}"
    difficultychoices= int(input("Select a difficulty:\n1. Easy\n2. Medium\n3. Hard\n>"))
    if difficultychoices == 1:
        difficultychoices= f"&difficulty=easy"
    elif difficultychoices == 2:
        difficultychoices= f"&difficulty=medium"
    elif difficultychoices== 3:
        difficultychoices=  f"&difficulty=hard" 
    else:
        difficultychoices= "" 
    typequest= int(input("Multiple Choice or True/False questions?: 1. Multiple Choice 2.True/False\n>"))
    if typequest== 1:
        typequest= f"&type=multiple"
    elif typequest == 2:
        typequest = F"&type=boolean"
    else:
        typequest = ""
    category= int(input("Pick a number between 9 and 32 for the category of questions.\n>"))
    if category:
        category= f"&category={category}"
    else:
        category= ""

    newURL= f"{URL}{numquests}{difficultychoices}{category}{typequest}"
    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(newURL).json()
    


    print(f"Here is your API Link: {newURL}")
    
if __name__ == "__main__":
    main()