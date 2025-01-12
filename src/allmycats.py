cats = []

while True:
    print(f"Enter the name of the cat {len(cats) + 1} or enter nothing to stop:")
    catName = input()
    if catName == '':
        break
    cats = cats + [catName]
print('The cat names are:')
for cat in cats:
    print(cat)
