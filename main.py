#!/usr/bin/env python

from cards import answers, questions
from random import choice, sample


def get_user_selection(inp):
    is_invalid = True
    
    if inp.lower() == "end":
        is_invalid = False
        return -1
    else:
        selection = int(inp)
        if 0 < selection and selection <= len(answers_sample):
            is_invalid = False
            return selection
    
    return None


selection = 0
answers_sample = []
run_loop = True
user_input_invalid = True

while run_loop:
    print(choice(questions))
    answers_sample = sample(answers, 3)
    
    # ["a", "b", "c"] -enumerate-> [(0, "a"), (1, "b"), (2, "c")]
    for nr, a in enumerate(answers_sample): 
        print( f"   {nr+1} {a}")

    user_input = input("Selection: ")
    selection = get_user_selection(user_input)
    
    if selection == -1:
        run_loop = False
    elif selection is None:
        user_input = input("Try again. Selection: ")
        selection = get_user_selection(user_input)
    else:
        print(answers_sample[selection-1])

    #while user_input_invalid == True:
    #    selection = int(input("Sorry I didn't understand. Please try again: "))
    