# Pattern to print

#     ****
#    ****
#   ****
#  ****


pattern = '*'
space = ' '
rows = 4


for i in range(rows):
    print(space * (rows - i + 1) + pattern * rows)
