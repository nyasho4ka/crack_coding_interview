import random
from collections import deque


class Shelter:
    def __init__(self, shelter_imp):
        self.shelter_imp = shelter_imp

    def enqueue(self, animal):
        self.shelter_imp.enqueue(animal)

    def dequeue_any(self):
        return self.shelter_imp.dequeue_any()

    def dequeue_dog(self):
        return self.shelter_imp.dequeue_dog()

    def dequeue_cat(self):
        return self.shelter_imp.dequeue_cat()


class ShelterGeneralQueueImp:
    def __init__(self):
        self.animal_queue = deque()

    def enqueue(self, animal):
        self.animal_queue.append(animal)

    def dequeue_any(self):
        return self.animal_queue.popleft()

    def dequeue_dog(self):
        oldest_dog = self.__get_oldest_dog()
        return oldest_dog

    def __get_oldest_dog(self):
        return self.__class__

    def dequeue_cat(self):
        oldest_cat = self.__get_oldest_cat()
        return oldest_cat

    def __get_oldest_cat(self):
        return self.__class__


class ShelterDiffQueueImp:
    def __init__(self):
        self.cat_queue = deque()
        self.dog_queue = deque()
        self.id = 0

    def enqueue(self, animal):
        self.__set_id(animal)
        if animal.kind == 'cat':
            self.cat_queue.append(animal)
        else:
            self.dog_queue.append(animal)

    def __set_id(self, animal):
        animal.id = self.id
        self.id += 1

    def dequeue_any(self):
        if self.cat_queue[0].id < self.dog_queue[0].id:
            return self.cat_queue.popleft()
        return self.dog_queue.popleft()

    def dequeue_dog(self):
        return self.dog_queue.popleft()

    def dequeue_cat(self):
        return self.cat_queue.popleft()


class Animal:
    """
    To simplify there is just one Animal implementation
    Suppose that in ShelterGeneralQueueImp we use Animal
    Without id field (just set it to None)
    """
    def __init__(self, kind):
        self.id = None
        self.kind = kind


animal_types = ['cat', 'dog']
animals = [Animal(random.choice(animal_types)) for i in range(10)]

shelter = Shelter(ShelterDiffQueueImp())
