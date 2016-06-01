#Barnaby Skinner
#2016/05/25
#Homework 2

#LISTS

#1) Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
#1) Display the number of elements in the list
random_numbers = [22, 90, 0, -10, 3, 22, 48]
print(len(random_numbers))

#2) Display the 4th element of this list.
print(random_numbers[3])

#3) Display the sum of the 2nd and 4th element of the list.
#call numbers 2 and 4
number2 = (random_numbers[1])
number4 = (random_numbers[3])
print(int(number2)+int(number4))

#4) Display the 2nd-largest value in the list.
random_numbers_sorted = sorted(random_numbers)
print(random_numbers_sorted[-2])

#5) Display the last element of the original unsorted list
print(random_numbers[-1])

#6) For each number, display a number: if your original number is less than
#10, multiply it by thirty. If it's also even, add six. If it's greater than 50
#subtract ten. If it's not negative ten, subtract one. (For example: 2 is less
#than 10, so 2 * 30 = 60, 2 is also even, so 60 + 6 = 66, 2 is not negative ten,
#so 66 - 1 = 65.)
for number in random_numbers:
    original = number
    if number > 50:
        number = number - 10
    if number < 10:
        number = number * 30
        if original % 2 == 0:
            number = number + 6
    if number > -10:
        number = number - 1
    print(number)

#7) Sum the result of each of the numbers divided by two.
print((sum(random_numbers))/2)

#DICTIONARIES
#8) Sometimes dictionaries are used to describe multiple aspects of a single
#object. Like, say, a movie. Define a dictionary called movie that works with
#the following code.
movie = {"Movie": "Rosemary's Baby", "Year": "1968", "Director": \
    "Roman Polanski", "Budget": 3.2, "Boxoffice": 33.4}

print("My favorite movie is", (movie["Movie"]), "which was released in", \
    (movie["Year"]), "and directed by", (movie["Director"]), ".")

#9) Add entries to the movie dictionary for budget and revenue (you'll use code
#like movie['budget'] = 1000), and print out the difference between the two.
print(movie["Boxoffice"] - movie["Budget"])

#10) If the movie cost more to make than it made in theaters, print "It was a
#flop". If the film's revenue was more than five times the amount it cost to
#make, print "That was a good investment
income = (movie["Boxoffice"] - movie["Budget"])
if income < 0:
    print("It was a flop.")
if income > movie["Budget"] * 5:
    print("That was a good investment.")

#11) Sometimes dictionaries are used to describe the same aspects of many
#different objects. Make ONE dictionary that describes the population of the
#boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx
#has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all
#in either millions or thousands is a good idea).
NYCBoroughs = {"Brooklyn": 2.6, "Manhattan": 1.6, "Bronx": 1.4, "Queens": 2.3, \
    "Staten Island": 0.47}

#12) Display the population of Brooklyn.
print(NYCBoroughs["Brooklyn"])

#13) Display the combined population of all five boroughs.
print(sum(NYCBoroughs.values()))

#14) Display what percent of NYC's population lives in Manhattan.
TotalNYCPopulation = NYCBoroughs["Manhattan"] / sum(NYCBoroughs.values()) *100
print(TotalNYCPopulation)
