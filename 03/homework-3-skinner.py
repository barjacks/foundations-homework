#Barnaby Skinner
#2016-05-30
#Homework 3

#LISTS

#1) Make a list called "countries" - it should contain seven different
#countries and NOT be in alphabetical order
countries = ["Switzerland", "Germany", "United Kingdom", "France", "Italy",
"Liechstenstein"]

#2) Using a for loop, print each element of the list
for country in countries:
    print(country)

#3) Sort the list permanently.
countries.sort()
#print(countries)

#4) Display the first element of the list
print(countries[0])

#5) Display the second-to-last element of the list using a line of code that
#will work no matter what the size of the list is (hint: len will be helpful)
countries_count = int(len(countries))
countries_count_minus_1 = countries_count - 2
print(countries[countries_count_minus_1])

#6) Delete one of the countries from the list using its name (we didn't
#learn this in class).
countries.remove("Germany")

#7) Using a for loop, print each element of the list again, which should now
#be one element shorter.
for country in countries:
    print(country)

#DICTIONARIES

#1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age',
#'location_name', 'latitude' and 'longitude'. Pick a tree from
#here:https://en.wikipedia.org/wiki/List_of_trees
tree = {"name": "Granit Oak", "species": "Oak", "age": 1650, "location_name":
    "Granit village, Bulgaria", "Latitude": 42.252403, "Longitude": 25.136684}

#2) Print the sentence "{name} is a {years old} tree that is in {location_name}"
print((tree["name"]), "is a", (tree["age"]), "years old tree that is in",
    (tree["location_name"]), ".")

#3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see
#if the tree is south of NYC, and print "The tree {name} in {location} is south
#of NYC" if it is. If it isn't, print "The tree {name} in {location} is north
#of NYC"
New_York = {"Latitude": 40.7128, "Longitude": -74.0059}
if New_York["Latitude"] < tree["Latitude"]:
    print("The tree", (tree["name"]), "in", (tree["location_name"]),
    "is north of NYC.")
else:
    print("The tree", (tree["name"]), "in", (tree["location_name"]),
    "is south of NYC.")

#4) 4) Ask the user how old they are. If they are older than the tree, display
#"you are {XXX} years older than {name}." If they are younger than the tree,
#display "{name} was {XXX} years old when you were born."
user_age= input("How old are you, if I may ask? ")

if int(user_age) > tree["age"]:
    age_difference = int(user_age) - tree["age"]
    print("You are", age_difference, "years older than", tree["name"])
else:
    age_difference2 = tree["age"] - int(user_age)
    print(tree["name"], "was", age_difference2, "years old, when you were born",)

#LISTS OF DICTIONARIES

#1) Make a list of dictionaries of five places across the world - (1) Moscow,
#(2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary
#should include each city's name and latitude/longitude (see note above).
Five_places = [
        {"name": "Moscow", "Latitude": 55.755826, "Longitude": 37.617300},
        {"name": "Tehran", "Latitude": 35.689197, "Longitude": 51.388974},
        {"name": "Falkland Islands", "Latitude": -51.796253, "Longitude": -59.523613},
        {"name": "Seoul", "Latitude": 37.566535, "Longitude": 126.977969},
        {"name": "Santiago", "Latitude": -33.4489, "Longitude": -70.6693}
    ]
#2) Loop through the list, printing each city's name and whether it is above or
#below the equator (How do you know? Think hard about the latitude.). When you
#get to the Falkland Islands, also display the message "The Falkland Islands are
#a biogeographical part of the mild Antarctic zone," which is a sentence I stole
#from Wikipedia.
for city in Five_places:
    if city["Latitude"] == -51.796253:
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone, and below the equator.")
    elif city["Latitude"] > 0 and city["Latitude"] != -51.796253:
        print(city["name"], "is above the equator.")
    else:
        print(city["name"], "is below the equator.")

#3) Loop through the list, printing whether each city is north of south of your
#tree from the previous section.

for city in Five_places:
    if city["Latitude"] > tree["Latitude"]:
        print((city["name"]), "is north of the", (tree["name"]))
    elif city["Latitude"] == tree["Latitude"]:
        print((city["name"]), "and", (tree["name"]), "are at exactly the same latitude.")
    else:
        print((city["name"]), "is south of the", (tree["name"]))
