import classes.magic8Ball as mb
import random

r = random.randint(1, 9)
answer = mb.getAnswer(r)
print(answer)
