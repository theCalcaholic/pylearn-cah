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

def handle_user_input(available_answers):
    valid_input = False
    selection = 0
    while valid_input == False:
        user_input = input("Selection: ")
        selection = get_user_selection(user_input)
        if selection == -1:
            valid_input = True
            return False, None
        elif selection is None:
            valid_input = False
            print("Try again!")
        else:
            user_answer = available_answers[selection-1]
            valid_input = True
            return True, user_answer


answers_sample = []

while True:
    question = choice(questions)
    question_text = question["text"]
    question_pick = question["pick"]
    print(question_text)
    answers_sample = sample(answers, 3)
    
    # ["a", "b", "c"] -enumerate-> [(0, "a"), (1, "b"), (2, "c")]
    for nr, a in enumerate(answers_sample):
        print( f"   {nr+1} {a}" )
    
    selected_answers = []
    
    while question_pick > len(selected_answers):
        run_loop, answer = handle_user_input(answers_sample)
        selected_answers.append(answer)

    if not run_loop:
        break
        
    if "____" in question_text:
        output = question_text.replace("____", answer)
    else: 
        output = question_text + "\n" + answer
    print(output + "\n")

