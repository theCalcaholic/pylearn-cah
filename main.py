#!/usr/bin/env python

from cards import answers, questions
from random import choice, sample


def get_user_selection(inp):
    
    if inp.lower() == "end":
        return -1
    else:
        selection = int(inp)
        if 0 < selection and selection <= len(answers_sample):
            return selection
    
    return None


selection = 0
answers_sample = []
run_loop = True
user_input_invalid = True


while run_loop:
    question = choice(questions)["text"]
    valid_input = False
    print(question)
    answers_sample = sample(answers, 3)
    
    # ["a", "b", "c"] -enumerate-> [(0, "a"), (1, "b"), (2, "c")]
    for nr, a in enumerate(answers_sample):
        print( f"   {nr+1} {a}" )
    
    while valid_input == False:
        user_input = input("Selection: ")
        selection = get_user_selection(user_input)
        if selection == -1:
            run_loop = False
            valid_input = True
        elif selection is None:
            valid_input = False
            print("Try again!")
        else:
            if "____" in question:
                answer = question.replace("____", answers_sample[selection-1])
            else: 
                answer = question + "\n" + answers_sample[selection-1]
            print(answer + "\n")
            valid_input = True

    
