# Pattern to print

# ******
#  ******
#   ******
#    ******

pattern = '*'
space = ' '
rows = 4
columns = 6


for i in range(rows):
    print(space * i + pattern * columns)
