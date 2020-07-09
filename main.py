#!/usr/bin/env python

from cards import answers as answers_pool, questions # TODO: Move to util
from random import choice, sample
from util import handle_user_input, draw_cards, get_question, remove_selected_answers


def user_select_answers (question_pick, hand_answers, question_text): 
    selected_answers = []

    
    while question_pick > len(selected_answers):
        run_loop, answer = handle_user_input(hand_answers)
        selected_answers.append(answer)

        if not run_loop:
            break
        
        if "____" in question_text:
            question_text = question_text.replace("____", answer, 1)
        else:
            question_text = question_text + "\n" + answer
    
    return selected_answers, run_loop, question_text
    

# get_answers -> util
answers = []
answers.extend(answers_pool)
new_answers = []

hand_answers = draw_cards(answers, 3)

while True:

    question = get_question()
    question_text = question["text"]
    question_pick = question["pick"]


    print(question_text)
    
    # ["a", "b", "c"] -enumerate-> [(0, "a"), (1, "b"), (2, "c")]
    for nr, a in enumerate(hand_answers):
        print( f"   {nr+1} {a}" )
    
    selected_answers, run_loop, question_text = user_select_answers (question_pick, hand_answers, question_text)
    
    if not run_loop:
        break

    print(question_text + "\n")

    answers, hand_answers = remove_selected_answers() # TODO: Remaining parameters
    
    new_answers = draw_cards(answers, question_pick)
    hand_answers = hand_answers + new_answers # TODO: Variable umbenennen
