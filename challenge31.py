#!/usr/bin/env python3

wordbank= ["indentation", "spaces"]

tlgstudents= ["Brandon", "Caleb", "Cat", "Chad the Beardulous", "Chance", "Chris", "Jessica", "Jorge", "Joshua", "Justin", "Lui", "Stephen"]

wordbank.append(4)
print(wordbank)

num = int(input("Pick a number between 0 and 11 \n"))

student_name = tlgstudents[num]
print(student_name)
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent. ")

