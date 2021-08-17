# busy.py - a busy beaver

A busy beaver implemented in python.
It traverses a circular list of boolean values, each representing a light in a room. Each step, the beaver 
moves randomly one unit forwards or backwards in the list.

 * If it encounters a dark room, it starts turning on lights
 * If it encounters a lit room, it starts turning off lights
 * If it is about to turn off the light in a room whose two neighbors are also dark, it stops.
 
## Usage

### When run directly (```python3 beaver.py ...``` etc.)

```beaver.py <length> [<initial>] | <bool> <bool> <bool> ...```

 * When run with less than three arguments, the first argument is the length of the list of "rooms".

   If a second argument is provided, it will determine the initial state of all cells.
   
 * When run with three or more arguments, the arguments are used directly to produce the list of "rooms".
 
In both cases, 0 is interpreted as False, anything else as True.

### When imported

```python3
from busy import Beaver

beaver = Beaver([True, False, True, True])
for (step, position, rooms, result) in beaver.release():
    state = ''.join([str(int(i)) for i in rooms])
    pointer = "^".rjust(len(str(step)) + 3 + position)
    print('{} [{}] {}'.format(step, state, result))
    print(pointer)
```
