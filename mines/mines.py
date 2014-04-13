# Start in the upper right corner.
# eg click in the upper leftmost corner.
# To start and be successful with many, we must start on a zero.
# If there is less than r*c-1 mines
# Progress down and to the right.

#  c . .
#  . . *
#  * * *

# To be successful, we must have:
#   m <= r*c - 4

# Or we could have:

# c . *
# . . *

# Or we could have:

# c . . . * * * *

#   m < r if c=1
#   m < c if r=1

# case r is 1 => true
# case c is 1 => true
# case: c is touching a mine
#   Happens when m > r*c - 4
#   Only works out if m = r*c - 1 
# case: c is not touching a mine
#   Happens when m = r*c - 4 or r is 1 or c is 1
#   EG at least 3 spaces and one click
# We must have 3 spaces or 6 spaces.
# There is definitely something special about 9

# Ampersands must be not touching mines
# * . . .
# * . . c
# * . . .
# * * * *
# * * * *

