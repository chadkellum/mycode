#!/usr/bin/env python3
import os

def main():

    print("What kind of Chad are you? Find out by answering the questions using 1-4.")
   
    questions = {
        "question1": "Which activity do you like best?:	\n1. Reading	\n2. Drawing	\n3. Chilling	\n4. Running\n", 
        "question2": "Which movie is the best?:	\n1. Empire Strikes Back	\n2. Revenge of the Sith	\n3. The Last Jedi	\n4. Rise of Skywalker\n", 
        "question3": "What is the meaning of life?:\n 1. 42	\n2. Drink and be merry	\n3. Be one with the world	\n4. Procreate\n", 
        "question4": "You shall not _____?:	\n1. Pass	\n2. Bruh	\n3. Litter	\n4. Rest\n",
        "question5": "What is your drink of choice?:	\n1. Blue Milk	\n2. Bud light	\n3. Red Wine	\n4. Warm Jaegermeister \n",
        "question6": "Who said 'This is the way'?:	\n1. Mando	\n2. Tom Cruise	\n3. Bob Ross	\n4. I did\n",
        "question7": "What is your favorite thing to do outdoors?:	\n1. LARP	\n2. Day drink	\n3. Paint	\n4. People watch\n",
        "question8":"How many houses are there in Hogwarts?:	\n1. 4	\n2. What's Hogwarts?	\n3. It's a castle	\n4. Only one that matters: Slytherin\n",
        "question9": "Who is the greatest of all time?:	\n1. Gandalf	\n2. LeBron	\n3. Meryl Streep	\n4. Dexter\n",
        "question10":"What is the airspeed velocity of an unladen swallow?:	\n1. African or European	\n2. 100	\n3. Swallows are pretty	\n4. 2 coconuts\n"
        
        }

    nerdy_count= 0
    bro_count= 0
    artsy_count= 0 
    psycho_count= 0

    for x in questions:
        print(questions[x])
        while True:
                answer= input(">")
                if answer == "1":
                   nerdy_count += 1
                   os.system("clear")
                   break
                elif answer == "2":
                   bro_count += 1
                   os.system("clear")
                   break
                elif answer == "3":
                    artsy_count += 1
                    os.system("clear")
                    break
                elif answer == "4":
                    psycho_count += 1
                    os.system("clear")
                    break
                else:
                    print("Your answer is not valid. Please choose an answer between 1-4")

    results = (nerdy_count, bro_count, artsy_count, psycho_count)
    max_value = max(results)
    print(f"Nerdy: {nerdy_count}, Bro: {bro_count}, Artsy: {artsy_count}, Psycho: {psycho_count}\n")
    
    if max_value == nerdy_count:
        print("You are a nerdy kind of Chad. Nice beard, by the way.")
    elif max_value == bro_count:
        print("You are a bro kind of Chad. Nice beard, by the way.")
    elif max_value == artsy_count:
        print("You are an artsy kind of Chad. Nice beard, by the way.")
    elif max_value == psycho_count:
        print("You are a psycho kind of Chad. Nice beard, by the way.")
    else:
        print("You are a well-rounded Chad, Chad. Nice beard!")

main()
               # ...etc.
               # I don't know if the A answers are nerdy or not, this is just a for instance
               # but the above loops over each question, prints that question and the answers out,
               # then a while loop starts.
               # if the user's answer matches "a" or "b" or whatever, it increases the score by 1 and breaks out of the while loop
               # the for loop then moves on to the next question

     # LONG SIMPLE(R) WAY
     # write a bunch of print functions for each question in your dictionary

    #  print(question[question1])
    #  answer= input(">")
    #  while True:
    #      if answer == "a":
    #          nerdy_count += 1
    #          break
    #      elif answer == "b":
    #          bro_count += 1
    #          break
    #      # etc.

    #  print(question[question2])
    #  answer= input(">")
    #  while True:
    #      if answer == "a":
    #          nerdy_count += 1
    #          break
    #      elif answer == "b":
    #          bro_count += 1
    #          break
         # etc.

     # above you can see that the whole section of code is being repeated for each question. it's less efficient,
     # but once you figure out how to write the code for ONE question you can re-use it for the rest

     # at the end of your code, you find which variable has the highest value
     # the max() function will tell you wish value is highest
     # then print your answer



