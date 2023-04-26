#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

eyes= challenge[2][1]
goggles= challenge[2][0]
nothing= challenge[-1]

#My eyes! The goggles do nothing!

print(f"My {eyes}! The {goggles} do {nothing}!")

eyesT= trial[2]["goggles"]
gogglesT= trial[2]["eyes"]
nothingT= trial[-1]
print(f"My {eyesT}! The {gogglesT} do {nothingT}!")

