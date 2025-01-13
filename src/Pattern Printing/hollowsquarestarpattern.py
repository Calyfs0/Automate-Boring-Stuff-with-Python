# Pattern to print

# ****
# *  *
# *  *
# ****


pattern = '*'
rows = 8


for i in range(rows):
    for j in range(rows):
        if i > 0 and i < rows - 1 and j > 0 and j < rows - 1:
            print(' ', end='')
        else:
            print(pattern, end='')
    print()
