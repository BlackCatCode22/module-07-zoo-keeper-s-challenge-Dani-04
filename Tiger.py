# Tiger.py

from Animal import Animal

class Tiger(Animal):
    numOfTigers = 0  # Static variable to keep track of the number of tigers

    # Constructor
    def __init__(self, name, animal_id, birth_date, color, gender, weight, originating_zoo, date_arrival):
        super().__init__(name, animal_id, birth_date, color, gender, weight, originating_zoo, date_arrival)
        Tiger.numOfTigers += 1  # Increment the number of tigers each time a new Tiger is created

    # Method to get the next available tiger name from the tiger names list
    @staticmethod
    def get_tiger_name(tiger):
        tiger_name_list = ["Tony", "Tigger", "Amber", "Cosimia", "Cuddles", "Dave", "Jiba", "Rajah", "Rayas", "Ryker"]
        return tiger_name_list[Tiger.numOfTigers % len(tiger_name_list)]

    # String representation of the Tiger object for easier printing
    def __str__(self):
        return f"{self.animal_id}, {self.name}; birthdate: {self.birth_date}; {self.color}; {self.gender}; {self.weight}; {self.originating_zoo}; arrived: {self.date_arrival}"
