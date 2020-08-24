import time
import random
import collections
import threading


class CallCenter:
    def __init__(self, respondents, manager, director, call_queue):
        self.respondents = respondents
        self.manager = manager
        self.director = director
        self.call_queue = call_queue

    def dispatch_call(self, call):
        # Ищем первого свободного респондента
        for respondent in self.respondents:
            if respondent.is_free:
                respondent.accept_call(call)
                return
        if self.manager.is_free:
            self.manager.accept_call(call)
            return
        if self.director.is_free:
            self.director.accept_call(call)
            return
        print('THERE IS NO FREE EMPLOYEES, CALL IS PUT TO THE QUEUE')
        self.call_queue.append(call)

    def update_call_queue(self, employee):
        if len(self.call_queue) > 0:
            call = self.call_queue.popleft()
            print('GET CALL {} FROM QUEUE'.format(call))
            employee.accept_call(call)


class Employee:
    def __init__(self):
        self.is_free = True
        self.call_center = None

    def add_call_center(self, call_center):
        self.call_center = call_center

    def accept_call(self, call):
        self.is_free = False
        call.start()
        call_duration = random.randint(1, 10)
        time.sleep(call_duration)
        call.end()
        self.is_free = True
        self.note_call_ended()

    def note_call_ended(self):
        if self.call_center is None:
            raise RuntimeError('THERE IS NO ANY CALL CENTER')
        self.call_center.update_call_queue(self)


class Respondent(Employee):
    pass


class Manager(Employee):
    pass


class Director(Employee):
    pass


class Call:
    def __init__(self, number):
        self.number = number

    def start(self):
        print('CALL FROM {} WAS STARTED'.format(self.number))

    def end(self):
        print('CALL FROM {} WAS ENDED'.format(self.number))

    def __str__(self):
        return str(self.number)


def create_call_center(respondents_number=10):
    respondents = [Respondent() for _ in range(respondents_number)]
    manager = Manager()
    director = Director()
    call_queue = collections.deque()
    call_center = CallCenter(respondents, manager, director, call_queue)
    for respondent in respondents:
        respondent.add_call_center(call_center)
    manager.add_call_center(call_center)
    director.add_call_center(call_center)
    return call_center


call_center = create_call_center()

threads = []
for i in range(20):
    number = random.randint(111111, 999999)
    call = Call(number)
    thread = threading.Thread(target=call_center.dispatch_call, args=(call, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
