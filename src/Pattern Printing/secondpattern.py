# Pattern to print

#    *
#   **
#  ***
# ****

pattern = '*'
space = ' '

rows = 6

for i in range(rows):
    for j in range(rows):
        if j < rows - i - 1:
            print(space, end='')
        else:
            print(pattern, end='')
    print()
