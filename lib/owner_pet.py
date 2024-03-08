class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        owner_pets = []
        for pet in Pet.all:
            if isinstance(pet.owner, Owner) and pet.owner == self:
                owner_pets.append(pet)
        return owner_pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added as pets.")
        pet.owner = self

    def get_sorted_pets(self):
        owner_pets = self.pets()
        sorted_pets = sorted(owner_pets, key=lambda x: x.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type. Please choose from: {}".format(self.PET_TYPES))
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all.append(self)


# Testing the implementation
if __name__ == "__main__":
    # Create owners
    owner1 = Owner("Alice")
    owner2 = Owner("Bob")

    # Create pets and assign owners
    pet1 = Pet("Buddy", "dog", owner1)
    pet2 = Pet("Fluffy", "cat", owner1)
    pet3 = Pet("Max", "bird", owner2)

    # Test adding pets to owners
    owner1.add_pet(pet3)  # Should raise an exception since pet3 is not owned by owner1

    # Test getting sorted pets
    sorted_pets_owner1 = owner1.get_sorted_pets()
    sorted_pets_owner2 = owner2.get_sorted_pets()

    print("Owner 1's sorted pets:")
    for pet in sorted_pets_owner1:
        print(pet.name)

    print("Owner 2's sorted pets:")
    for pet in sorted_pets_owner2:
        print(pet.name)
