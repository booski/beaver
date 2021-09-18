'''
scared state: dark room: turn on the light, move on
              light room: switch to conservation state
conservation state: light room, lit neighbor: turn off the light, move on
                    light room, dark neighbors: stop
                    dark room: switch to scared state
'''

from random import choice
from pprint import pformat

class Beaver:
    def __init__(self, rooms):
        self.state = self.conserve
        self.rooms = rooms
        self.position = int(len(rooms)/2)
        self.done = False
        
    def scared(self):
        self.move(dir=1)
        if self.rooms[self.position] is False:
            self.rooms[self.position] = True
            return "Turned on the light."
        else:
            self.state = self.conserve
            return "Turning off lights to conserve energy."

    def conserve(self):
        self.move(dir=1)
        if self.rooms[self.position] is True:
            if (
                    self.rooms[self.move(False, -1)] is False and
                    self.rooms[self.move(False, 1)] is False
            ):
                self.state = self.finish
                return "Ok, only this room is lit now."
                
            self.rooms[self.position] = False
            return "Turned off the light."
        else:
            self.state = self.scared
            return "I'm scared!"

    def finish(self):
        self.done = True
        return "Good night."

    def move(self, doit=True, dir=None):
        position = self.position
        if dir is None:
            position += choice([-1, 1])
        else:
            position += dir
        if position < 0:
            position = len(self.rooms) - 1
        elif position >= len(self.rooms):
            position = 0
        if(doit):
            self.position = position
        return position

    def release(self):
        step = 0
        while not self.done:
            step += 1
            result = self.state()
            yield (step, self.position, self.rooms, result)


if __name__ == '__main__':
    import sys
    try:
        length = len(sys.argv)
        if length == 2:
            # One argument:
            #  number of rooms
            size = int(sys.argv[1])
            rooms = [choice([True, False]) for i in range(size)]
        elif length == 3:
            # Two arguments:
            #  number of rooms
            #  initial state
            size = int(sys.argv[1])
            rooms = [bool(int(sys.argv[2])) for i in range(size)]
        elif length > 3:
            # More than two arguments:
            #  list of initial states
            rooms = [bool(int(i)) for i in sys.argv[1:]]
    except Exception as e:
        print("Usage: "+sys.argv[0]+" <int> | <int> <bool> | <bool> <bool> ...")
        exit(1)
    beaver = Beaver(rooms)
    try:
        for (step, position, rooms, result) in beaver.release():
            state = ''.join([str(int(i)) for i in rooms])
            pointer = "^".rjust(len(str(step)) + 3 + position)
            print('{} [{}] {}'.format(step, state, result))
            print(pointer)
    except KeyboardInterrupt as e:
        print()
        exit(0)
