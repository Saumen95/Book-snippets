'''
Nope. I'm not going to write a manual full alphabet script, not because
of the complexity, but because of the time involved. My approach would
be to create two base functions - one to draw a line, and one an arc that
curved to the right.
Both would take four arguments: starting x,y and ending x,y.
Then, assuming a letter aspect ratio of arbitrary size (e.g., twice as
tall as wide), I'd plot out letters with a series of "draw from here to
there" commands.
'''