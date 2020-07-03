# MANY KNOWN ISSUES RIGHT NOW

# (DONE) check if json exists, if it doesnt, create a file for users water drinking records

# (DONE) greet the user with random fact about water

# (DONE, NEEDS BUGFIX) ask the user for name so they can "log in" (list already known users)

# if the json exists then count number of days when the user drank water
# and tell them that so far they have drank enough water for X days

# (DONE) ask for input if user has drunk enough water today

# (KINDA, not for JSON) if yes ask for volume and write yes and volume into json

# if no remind them it is important to drink enough water and write no into json

# return to input with quote that this is the next day

# (DONE) rewrite for while true loop

# allow for the user to stop the script when they fail to answer yes/no

# THERE NEEDS TO BE A DAY = 1 OR SOMETHING AND IN THE NEXT ITERATION IT SETS TO DAY+1 OR SOMETHING LIKE THAT
# WITH NEW OPEN IT READS LAST DAY OPENED FOR THAT USER AND AUTOMATICALLY SETS FOR DAY+1

import random
import json
import os


def finddatabase(filename):
    return os.path.exists(filename)


if finddatabase("water-test-data.json.json"):
    print("Existing water data found!")
else:
    print("Water data not found, will create database!")

randomfacts = ["Hey! Did you know that water is very interesting?", "You might have not known it, but water is like "
                                                                    "really really wet!",
               "In case you missed the memo, water is not a solid substance!", "There are rumours there is water "
                                                                               "even on Mars! Think about that!",
               "Even fish drink water daily!"]

yes = ["Y", "y", "yes"]

no = ["N", "n", "no", "nope"]

while True:
    chosenfact = random.choice(randomfacts)

    print("Fun Fact about Water of the Day! " + chosenfact)

    username = input("What is your name?")
    with open("water-test-data.json", "r") as checkifknown:
        usernamecheck = json.load(checkifknown)
        if username in usernamecheck.keys():
            print("Welcome Back, " + username + ". So far you have drunk *VALUE* of water since using this tracker.")
        else:
            print("Hello,", username)

    drankwatertoday = input("Did you drink enough water today? Y/N")

    # check if username exists in json file.
    # if exists then welcome back and tell them how much they have drunk water in how many days
    # most consecutive days water drunk?
    # NEEDS A WAY TO ADD NEW DAYS INTO JSON SO IT IS TRACKABLE
    # if it doesnt then greet user for the first time

    if drankwatertoday in yes:
        print("Good on You, " + username)

        watervolume = input("And how much water in mililitres did you drink today?")
        print("Okay, " + username + ". Today you have drunk " + watervolume + " ml of water.")

        # waterdata = {"name": username, "waterdrunk": watervolume}
        # no way, this requires major rework, else it overrides everything and doesnt
        # work as intended. Bad structure

        ### IF KEY USERNAME IN OUTFILE THEN ADD TO EXISTING VALUE
        ### MAYBE GET VALUE FROM WATERVOLUME_PREVIOUS AND ADD WATERVOLUME
        ### THEN JSON.DUMP
        ### ELSE JSON.DUMP but what?

        # THIS SOLUTION DOES NOT ADD TO THE VALUE DRUNK, BUT OVERRIDES THE VALUE OF A KEY

        with open("water.json", "a") as outfile:
            json.dump(waterdata, outfile)
        continue

    elif drankwatertoday in no:
        print("Not Good, " + username)

        ### IF KEY USERNAME IN OUTFILE THEN PASS
        ### ELSE JSON.DUMP WATERDATA = "0"
        continue
    else:
        print("Only Y/N answers please.")
        break

print('You have quit the program.')
