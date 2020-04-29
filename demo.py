from cards import questions
from random import choice



answer = ["abc", "garstig"]
better_answer = ["abc", "gründlich", "garstig"]

#best_answer = comprehension(better_answer, answer)


for key, value in questions[0].items():
    print(f"{key}: {value}")

#print(best_answer)