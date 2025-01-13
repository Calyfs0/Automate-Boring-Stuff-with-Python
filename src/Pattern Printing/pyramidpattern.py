# pattern to print

#    *
#   ***
#  *****
# *******


pattern = '*'
space = ' '
rows = 4
columns = 7

# for i in range(rows):
#    for j in range(rows, i + 1, -1):
#        print(space, end='')
#    for k in range(i * 2 + 1):
#        print(pattern, end='')
#    print()

x = 3

for i in range(rows):
    print(space * x + pattern * (i * 2 + 1) + space * x)
    x -= 1
