#Barney Skinner
#05/23/2016
#"Homework 1"

year_of_birth = input("Which year were you born in, if I may ask? ")

if int(year_of_birth) > 2016:
    print("That was in the future, you can do better than that.")

year_of_birth = input("Try again. Which year were you born in?")

age = 2016 - int(year_of_birth)
heartbeat_per_year = int(age) * 42000000
heartbeat_Blue_Whale = int(age) * 4700000
heartbeat_small_rabbit = int(age) * 94600000

#Calculations are here: https://docs.google.com/spreadsheets/d/1fqbLEryuxhpVMlXjHY4QsKr5I6sdy_8cMwgv53tfIoI/edit?usp=sharing

print("You are roughly", age, "years old.")
#Source of heartrate https://www.sharecare.com/health/circulatory-system-health/heart-beat-year
print("Taking an average rate of 80 beats per minute, your heart has beaten", heartbeat_per_year, "times in your lifetime.")
#Source of heart rate of a blue whale: http://www.whalefacts.org/blue-whale-heart/
print("During the same time period, a blue whale's heart has only beaten", heartbeat_Blue_Whale, "times.")
#Source of rabbit heart beat: http://rabbit.org/cardiac-heart-disease-in-rabbits/
if heartbeat_small_rabbit > 1000000000:
    heartbeat_small_rabbit = int(heartbeat_small_rabbit) / 1000000000
    print("A rabbit's hearts on the other have beaten", heartbeat_small_rabbit, "billion times.")
else:
    print("A rabbit's hearts on the other have beaten", heartbeat_small_rabbit, "times.")

#Calculations for years Planets are here: https://docs.google.com/spreadsheets/d/1fqbLEryuxhpVMlXjHY4QsKr5I6sdy_8cMwgv53tfIoI/edit#gid=0

print(  ) #making output more readable

age_on_venus = int(age) * 365 / 225
age_on_Neptune = int(age) * 365 / 89666

print("On Venus you are", age_on_venus, "years old.")
print("On Neptune you are", age_on_Neptune, "years old.")

print(  ) #making output more readable

if age == 41:
    print("You are the same age as the famous programmer Barney.")
elif age > 41:
    print("You are older than the famous programmer Barney.")
else:
    print("You are younger than the famous programmer Barney.")

#Calculations to work out difference to the age of the famous programmer

age_differenceolder = int(age) - 41
age_differenceyounger = 41 - int(age)
if age > 41:
    print("You are", age_differenceolder, "years older than him.")
elif age < 41:
    print("You are", age_differenceyounger, "years younger than him.")

print(  ) #making output more readable

if int(age) % 2 == 0:
    print("You were born in an even year.")

print(  ) #making output more readable

#Source for Steelers SB wins: http://www.steelers.com/history/superbowl.html
Pittsburgh_wins = [1975, 1976, 1979, 1980, 2006, 2009]

wins_count = 0
for win in Pittsburgh_wins:
    if int(year_of_birth) <= win:
        wins_count += 1
print("You have experienced", wins_count, "6 Pittsburgh Superbowl-Wins in your lifetime.")

if int(year_of_birth) >= 2009:
   print("You were born during Obama's Presidency - fellow Columbia alum.")

elif int(year_of_birth) >= 2001:
   print("You were born during George W. Bush's Presidency.")

elif int(year_of_birth) >= 1993:
   print("You were born during Clinton's Presidency.")

elif int(year_of_birth) >= 1989:
   print("You were born during Bush Senior's Presidency.")

elif int(year_of_birth) >= 1981:
   print("You were born during Reagan's Presidency.")

elif int(year_of_birth) >= 1977:
   print("You were born during Carter's Presidency.")

elif int(year_of_birth) >= 1974:
   print("You were born during Ford's Presidency.")

elif int(year_of_birth) >= 1969:
   print("You were born during Nixon's Presidency.")

elif int(year_of_birth) >= 1963:
   print("You were born during LBJ's Presidency.")

elif int(year_of_birth) >= 1961:
   print("You were born during JFK's Presidency.")

elif int(year_of_birth) >= 1953:
   print("You were born during Eisenhower's Presidency.")

elif int(year_of_birth) >= 1945:
   print("You were born during Truman's Presidency.")

elif int(year_of_birth) >= 1933:
    print("You were born during FDR's Presidency.")
