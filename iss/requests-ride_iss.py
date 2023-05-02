#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

    for astronaut in helmetson["people"]:
        # notice that the text is pink between the two " marks
        # python thinks you're starting and stopping a string on one line
        # the fix is to mix up your ' and " quotation marks a bit

        #print(f"{astronaut["name"]} is on the {astronaut["craft"]}") 
        print(f"{astronaut['name']} is on the {astronaut['craft']}") 

if __name__ == "__main__":
    main()

