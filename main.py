#!/usr/bin/env python

from cards import answers, questions
from random import choice, sample


selection = 0
answers_sample = []

while selection <= len(answers_sample):
    print(choice(questions))
    answers_sample = sample(answers, 3)
    
    # ["a", "b", "c"] -enumerate-> [(0, "a"), (1, "b"), (2, "c")]
    for nr, a in enumerate(answers_sample): 
        print( f"   {str(nr+1)} {a}")

    selection = int(input("Selection: "))

    if 0 < selection <= len(answers_sample):
        print(answers_sample[selection-1])
