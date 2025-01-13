# Pattern to print

# *
# **
# ***
# ****

pattern = '*'
space = ' '
rows = 4

for i in range(rows):
    print(pattern * (i + 1) + space * (rows - i + 1))
