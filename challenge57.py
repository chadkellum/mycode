#!/usr/bin/env python3

import html
import random

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

def main():

    question= trivia["question"]
    answer= trivia["correct_answer"]
    wrong1= trivia["incorrect_answers"][0]
    wrong2= trivia["incorrect_answers"][1]
    wrong3= trivia["incorrect_answers"][2]
    answers= [answer,wrong1,wrong2,wrong3]

    
    print(question)
    random.shuffle(answers)
    
     
    print("1",html.unescape(answers[0]))
    print("2",html.unescape(answers[1]))
    print("3",html.unescape(answers[2]))
    print("4",html.unescape(answers[3]))

    if int(input("Enter your answer: "))-1 == answers.index(answer):
        print("Correct, ya filthy animal.")
    else:
        print("Incorrect!")

if __name__ == "__main__":
    main()