spam = ['apples', 'bananas', 'tofu', 'cats']


def updateList(spam):
    outputString = ''
    if len(spam) == 0:
        return outputString
    if len(spam) == 1:
        return spam[0]
    stringLength = len(spam)
    for index, value in enumerate(spam):
        outputString += value
        if index == stringLength - 2:
            outputString += ' and '
        elif index == stringLength - 1:
            outputString += '.'
        else:
            outputString += ', '

    return outputString


output = updateList(spam)
print(output)
