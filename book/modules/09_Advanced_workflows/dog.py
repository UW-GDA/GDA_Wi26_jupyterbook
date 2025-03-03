class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        print(f'happy birthday {self.name}!')
        self.age += 1
        return

def human_years_to_dog_years(human_years_age):
    if human_years_age < 0:
        raise Exception('Ages must be positive')
    if human_years_age <= 1:
        dog_years_age = human_years_age*15
    elif 1 < human_years_age <= 2:
        dog_years_age = 15 + (human_years_age - 1)*9
    else:
        dog_years_age = 24 + (human_years_age - 2)*5
    return dog_years_age

n_dog_chromosomes = 78