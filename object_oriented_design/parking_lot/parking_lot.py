class ParkingLot:
    def __init__(self, parking_places, ticket_class):
        self.parking_places = parking_places
        self.ticket_class = ticket_class

    def get_free_place(self):
        for i, place in enumerate(self.parking_places):
            if place.is_free:
                return i
        return -1

    def park_car(self, car):
        free_place = self.get_free_place()
        if free_place >= 0:
            self.put_car(free_place, car)
            ticket = self.create_ticket(free_place)
            return True, ticket
        return False, None

    def put_car(self, place_id, car):
        self.parking_places[place_id].car = car
        self.parking_places[place_id].is_free = False

    def create_ticket(self, place_id):
        return self.ticket_class(place_id)

    def take_car_back(self, ticket):
        car = self.parking_places[ticket.place_id].car
        # TIME LOGIC AND MONEY PAYMENT
        self.parking_places[ticket.place_id].is_free = True


class ParkingPlace:
    def __init__(self):
        self.car = None
        self.is_free = True


class Car:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Ticket:
    def __init__(self, place_id):
        self.place_id = place_id
