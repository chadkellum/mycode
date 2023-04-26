#!/usr/bin/env python3

luke_skywalker = {
    'Title': ['Jedi Knight', 'Jedi Master', 'Red Five', 'Rogue Leader'
              ],
    'Occupation': ['Apprentice', 'Moisture Farmer', 'Pilot', 'Jedi'],
    'Affiliation': [
        'Skywalker family',
        'Rebel Alliance',
        'Rogue Squadron',
        'Jedi',
        'New Republic',
        'New Jedi Order',
        'Resistance',
        'Galactic Alliance',
        'Jedi Council',
        ],
    'Family': ['Padm\xc3\xa9 Amidala (mother)',
               'Anakin Skywalker (father)', 'Leia Organa (twin sister)'
               , 'Owen Lars (paternal step-uncle)',
               'Beru Lars (paternal step-aunt)'],
    }

luke_skywalker.update({"Enemies":"Darth Vader"})
# print(luke_skywalker)
luke_skywalker["Enemies"] = "Emperor Palpatine"
# print(luke_skywalker.keys())
# print(luke_skywalker.values())
luke_skywalker["Enemies"] = ["Emperor Palpatine", "Darth Vader", "Jake Skywalker", "Rian Johnson"]
# print(luke_skywalker.values())
print(luke_skywalker.keys())
choice = input("Choose a key: \n ")
value = luke_skywalker.get(choice,"Not a key. Please type one of the keys above to learn more.")
print(f"Luke Skywalker's {choice} is: {value}")

