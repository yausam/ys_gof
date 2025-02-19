import random
from abc import ABC, abstractmethod


# === Product Interfaces ===
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Plant(ABC):
    @abstractmethod
    def grow(self):
        pass


# === Concrete Products for the Forest Ecosystem ===
class Deer(Animal):
    def speak(self):
        return "Deer bleats"


class Wolf(Animal):
    def speak(self):
        return "Wolf howls"


class OakTree(Plant):
    def grow(self):
        return "Oak tree grows tall"


class PineTree(Plant):
    def grow(self):
        return "Pine tree grows straight"


# === Concrete Products for the Savannah Ecosystem ===
class Lion(Animal):
    def speak(self):
        return "Lion roars"


class Elephant(Animal):
    def speak(self):
        return "Elephant trumpets"


class AcaciaTree(Plant):
    def grow(self):
        return "Acacia tree spreads its branches"


class SavannahGrass(Plant):
    def grow(self):
        return "Grass sways in the wind"


# === Abstract Factory ===
class EcosystemFactory(ABC):
    @abstractmethod
    def create_animal(self, animal_role: str) -> Animal:
        """
        Create an animal based on its ecological role (e.g., predator, prey, herbivore).
        """
        pass

    @abstractmethod
    def create_plant(self, plant_type: str) -> Plant:
        """
        Create a plant based on its type (e.g., tree, grass).
        """
        pass


# === Concrete Factory for the Forest Ecosystem ===
class ForestFactory(EcosystemFactory):
    def create_animal(self, animal_role: str) -> Animal:
        if animal_role == "prey":
            return Deer()
        elif animal_role == "predator":
            return Wolf()
        else:
            raise ValueError(f"Unknown animal role: {animal_role}")

    def create_plant(self, plant_type: str) -> Plant:
        if plant_type == "tree":
            # Using a factory method pattern internally to decide the tree type
            return self._create_tree()
        else:
            raise ValueError(f"Unknown plant type: {plant_type}")

    # This is the Factory Method: it encapsulates the logic to decide which tree to create.
    def _create_tree(self) -> Plant:
        # Imagine that complex logic (e.g., based on soil quality, sunlight, etc.) decides the tree type.
        if random.random() > 0.5:
            return OakTree()
        else:
            return PineTree()


# === Concrete Factory for the Savannah Ecosystem ===
class SavannahFactory(EcosystemFactory):
    def create_animal(self, animal_role: str) -> Animal:
        if animal_role == "predator":
            return Lion()
        elif animal_role == "herbivore":
            return Elephant()
        else:
            raise ValueError(f"Unknown animal role: {animal_role}")

    def create_plant(self, plant_type: str) -> Plant:
        if plant_type == "tree":
            return AcaciaTree()
        elif plant_type == "grass":
            return SavannahGrass()
        else:
            raise ValueError(f"Unknown plant type: {plant_type}")


# === Client Code ===
def simulate_ecosystem(factory: EcosystemFactory):
    """
    Simulate an ecosystem by creating animals and plants using the provided factory.
    """
    # Try creating two animals with different roles.
    try:
        animal1 = factory.create_animal("prey")
    except ValueError:
        # For ecosystems that don't use "prey", try "herbivore" instead.
        animal1 = factory.create_animal("herbivore")
    animal2 = factory.create_animal("predator")

    # Create a plant: if the ecosystem doesn't support trees, fall back to another type.
    try:
        plant1 = factory.create_plant("tree")
    except ValueError:
        plant1 = factory.create_plant("grass")

    print(f"Animal1 speaks: {animal1.speak()}")
    print(f"Animal2 speaks: {animal2.speak()}")
    print(f"Plant grows: {plant1.grow()}")


if __name__ == "__main__":
    print("Forest Ecosystem Simulation:")
    forest_factory = ForestFactory()
    simulate_ecosystem(forest_factory)

    print("\nSavannah Ecosystem Simulation:")
    savannah_factory = SavannahFactory()
    simulate_ecosystem(savannah_factory)
