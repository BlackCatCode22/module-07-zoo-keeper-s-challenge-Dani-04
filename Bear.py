# Bear.py

from Animal import Animal

class Bear(Animal):
    numOfBears = 0  # Static variable to keep track of the number of bears

    # Constructor
    def __init__(self, name, animal_id, birth_date, color, gender, weight, originating_zoo, date_arrival):
        super().__init__(name, animal_id, birth_date, color, gender, weight, originating_zoo, date_arrival)
        Bear.numOfBears += 1  # Increment the number of bears each time a new Bear is created

    # Method to get the next available bear name from the bear names list
    @staticmethod
    def get_bear_name(bear):
        bear_name_list = ["Yogi", "Smokey", "Paddington", "Lippy", "Bungle", "Baloo", "Rupert", "Winnie the Pooh", "Snuggles", "Bert"]
        return bear_name_list[Bear.numOfBears % len(bear_name_list)]

    # String representation of the Bear object for easier printing
    def __str__(self):
        return f"{self.animal_id}, {self.name}; birthdate: {self.birth_date}; {self.color}; {self.gender}; {self.weight}; {self.originating_zoo}; arrived: {self.date_arrival}"
