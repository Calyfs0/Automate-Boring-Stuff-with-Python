# Pattern to print

# ******
# *    *
# *    *
# ******


pattern = '*'
space = ' '
rows = 4
columns = 6


for i in range(rows):
    for j in range(columns):
        if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
            print(pattern, end='')
        else:
            print(space, end='')
    print()
