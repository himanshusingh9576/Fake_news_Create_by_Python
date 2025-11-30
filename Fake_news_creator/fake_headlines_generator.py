# Import the random module
import random
#Create subjects
subjects = ["Sharukh khan", "Virat Kohli",
            "Nirmala sitharaman", "A Mumbai Cat",
            "A Group of Monkrys", "PM Modi",
            "Auto Rickshaw Driver from Delhi"]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "order",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Matches",
    "at India Gate"
    
]

# Step3- start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (Yes/No)").strip().lower()
    if user_input == "no":
        break

#print Goodbye message
print("\n" + headline)