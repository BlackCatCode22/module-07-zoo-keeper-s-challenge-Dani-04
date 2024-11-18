# Main.py
# driver file for Zoo Keeper's Challenge
# last update 10/13/23 by dH
# last update 10/14/23
# last Update 4/1/24 by dH

from Animal import Animal
from Hyena import Hyena
from Lion import Lion
from Tiger import Tiger
from Bear import Bear

from _datetime import date

# Create lists of the species
list_of_hyenas = [
    {"age": 4, "sex": "female", "birth_season": "spring", "color": "tan", "weight": 70, "location": "Friguia Park, Tunisia"},
    {"age": 12, "sex": "male", "birth_season": "fall", "color": "brown", "weight": 150, "location": "Friguia Park, Tunisia"},
    {"age": 4, "sex": "male", "birth_season": "spring", "color": "black", "weight": 120, "location": "Friguia Park, Tunisia"},
    {"age": 8, "sex": "female", "birth_season": "unknown", "color": "black and tan striped", "weight": 105, "location": "Friguia Park, Tunisia"}
]

# List of lions
list_of_lions = [
    {"age": 6, "sex": "female", "birth_season": "spring", "color": "tan", "weight": 300, "location": "Zanzibar, Tanzania"},
    {"age": 12, "sex": "female", "birth_season": "winter", "color": "dark tan", "weight": 375, "location": "KopeLion, Tanzania"},
    {"age": 22, "sex": "male", "birth_season": "fall", "color": "golden", "weight": 450, "location": "Zanzibar, Tanzania"},
    {"age": 4, "sex": "female", "birth_season": "spring", "color": "tan and brown", "weight": 275, "location": "KopeLion, Tanzania"}
]

# List of tigers
list_of_tigers = [
    {"age": 2, "sex": "male", "birth_season": "spring", "color": "gold and tan stripes", "weight": 270, "location": "Dhaka, Bangladesh"},
    {"age": 4, "sex": "female", "birth_season": "spring", "color": "black stripes", "weight": 400, "location": "Dhaka, Bangladesh"},
    {"age": 18, "sex": "male", "birth_season": "fall", "color": "gold and tan", "weight": 300, "location": "Bardia, Nepal"},
    {"age": 3, "sex": "female", "birth_season": "spring", "color": "black stripes", "weight": 285, "location": "Bardia, Nepal"}
]

# List of bears
list_of_bears = [
    {"age": 7, "sex": "male", "birth_season": "spring", "color": "brown", "weight": 320, "location": "Alaska Zoo, Alaska"},
    {"age": 25, "sex": "female", "birth_season": "spring", "color": "black", "weight": 425, "location": "Woodland Park Zoo, Washington"},
    {"age": 4, "sex": "female", "birth_season": "fall", "color": "black", "weight": 355, "location": "Woodland Park Zoo, Washington"},
    {"age": 4, "sex": "male", "birth_season": "spring", "color": "brown", "weight": 405, "location": "Alaska Zoo, Alaska"}
]

# This is needed for the calc birthday stuff.
current_date = date.today()
current_year = current_date.year

# Sample content from arrivingAnimals.txt (data extracted for testing)
arriving_animals = [
    "4 year old female hyena, born in spring, tan color, 70 pounds, from Friguia Park, Tunisia",
    "12 year old male hyena, born in fall, brown color, 150 pounds, from Friguia Park, Tunisia",
    "4 year old male hyena, born in spring, black color, 120 pounds, from Friguia Park, Tunisia",
    "8 year old female hyena, unknown birth season, black and tan striped color, 105 pounds, from Friguia Park, Tunisia",
    "6 year old female lion, born in spring, tan color, 300 pounds, from Zanzibar, Tanzania",
    "12 year old female lion, born in winter, dark tan color, 375 pounds, from KopeLion, Tanzania",
    "22 year old male lion, born in fall, golden color, 450 pounds, from Zanzibar, Tanzania",
    "4 year old female lion, born in spring, tan and brown color, 275 pounds, from KopeLion, Tanzania",
    "2 year old male tiger, born in spring, gold and tan stripes color, 270 pounds, from Dhaka, Bangladesh",
    "4 year old female tiger, born in spring, black stripes color, 400 pounds, from Dhaka, Bangladesh",
    "18 year old male tiger, born in fall, gold and tan color, 300 pounds, from Bardia, Nepal",
    "3 year old female tiger, born in spring, black stripes color, 285 pounds, from Bardia, Nepal",
    "7 year old male bear, born in spring, brown color, 320 pounds, from Alaska Zoo, Alaska",
    "25 year old female bear, born in spring, black color, 425 pounds, from Woodland park Zoo, Washington",
    "4 year old female bear, born in fall, black color, 355 pounds, from Woodland park Zoo, Washington",
    "4 year old male bear, born in spring, brown color, 405 pounds, from Alaska Zoo, Alaska"
]

# Animal names for each species
hyena_names = ["Shenzi", "Banzai", "Ed", "Zig", "Bud", "Lou", "Kamari", "Wema", "Nne", "Madoa", "Prince Nevarah"]
lion_names = ["Scar", "Mufasa", "Simba", "Kiara", "King", "Drooper", "Kimba", "Nala", "Leo", "Samson", "Elsa", "Cecil"]
tiger_names = ["Tony", "Tigger", "Amber", "Cosimia", "Cuddles", "Dave", "Jiba", "Rajah", "Rayas", "Ryker"]
bear_names = ["Yogi", "Smokey", "Paddington", "Lippy", "Bungle", "Baloo", "Rupert", "Winnie the Pooh", "Snuggles",
              "Bert"]


# Function to calculate birth date based on season and age
def calc_birth_date(season, years_old):
    year_of_birthday = int(current_year) - int(years_old)
    if "spring" in season:
        return f"{year_of_birthday}-03-21"
    elif "summer" in season:
        return f"{year_of_birthday}-06-21"
    elif "fall" in season:
        return f"{year_of_birthday}-09-21"
    elif "winter" in season:
        return f"{year_of_birthday}-12-21"
    else:
        return f"{year_of_birthday}-01-01"  # Default for unknown seasons


# Process each line in the arriving_animals list
def process_one_line(one_line):
    # Create variables to help parse arrivingAnimals.txt
    species = ""
    gender = ""
    age_in_years = 99
    season = ""
    color = ""
    weight = ""
    origin_01 = ""
    origin_02 = ""

    groups_of_words = one_line.strip().split(",")
    single_words = groups_of_words[0].strip().split(" ")
    age_in_years = single_words[0]
    gender = single_words[3]
    species = single_words[4]

    # Further split for other data
    single_words = groups_of_words[1].strip().split(" ")
    season = single_words[2]
    color = groups_of_words[2].strip()
    weight = groups_of_words[3].strip()
    origin_01 = groups_of_words[4].strip()
    origin_02 = groups_of_words[5].strip()

    from_zoo = f"{origin_01}, {origin_02}"
    birth_day = calc_birth_date(season, age_in_years)

    # Create animal object based on species
    if "hyena" in species:
        my_hyena = Hyena("aName", "aID", birth_day, color, gender, weight, from_zoo, current_date)
        my_hyena.name = hyena_names[Hyena.numOfHyenas % len(hyena_names)]
        my_hyena.animal_id = f"Hy{str(Hyena.numOfHyenas).zfill(2)}"
        list_of_hyenas.append(my_hyena)

    if "lion" in species:
        my_lion = Lion("aName", "aID", birth_day, color, gender, weight, from_zoo, current_date)
        my_lion.name = lion_names[Lion.numOfLions % len(lion_names)]
        my_lion.animal_id = f"Li{str(Lion.numOfLions).zfill(2)}"
        list_of_lions.append(my_lion)

    if "tiger" in species:
        my_tiger = Tiger("aName", "aID", birth_day, color, gender, weight, from_zoo, current_date)
        my_tiger.name = tiger_names[Tiger.numOfTigers % len(tiger_names)]
        my_tiger.animal_id = f"Ti{str(Tiger.numOfTigers).zfill(2)}"
        list_of_tigers.append(my_tiger)

    if "bear" in species:
        my_bear = Bear("aName", "aID", birth_day, color, gender, weight, from_zoo, current_date)
        my_bear.name = bear_names[Bear.numOfBears % len(bear_names)]
        my_bear.animal_id = f"Be{str(Bear.numOfBears).zfill(2)}"
        list_of_bears.append(my_bear)


# Process each line in arriving_animals list
for line in arriving_animals:
    process_one_line(line)

# Access the static variable numOfAnimals
print(f"\n\nNumber of animals created: {Animal.numOfAnimals}")

# Output the static variables for each species
print(f"\n\nNumber of hyenas created: {Hyena.numOfHyenas}")
print(f"Number of lions created: {Lion.numOfLions}")
print(f"Number of tigers created: {Tiger.numOfTigers}")
print(f"Number of bears created: {Bear.numOfBears}")

# Output the zoo population report
print("\nZookeeper's Challenge Zoo Population\n")
print("Hyena Habitat:")
for hyena in list_of_hyenas:
    print(hyena)

print("\nLion Habitat:")
for lion in list_of_lions:
    print(lion)

print("\nTiger Habitat:")
for tiger in list_of_tigers:
    print(tiger)

print("\nBear Habitat:")
for bear in list_of_bears:
    print(bear)
