#!/usr/bin/env python

from cards import answers as answers_pool, questions
from random import choice, sample
from util import handle_user_input, get_new_cards


answers = []
answers.extend(answers_pool)
answers_sample = []
new_answers = []

answers_sample = get_new_cards(answers_sample, answers, 3)

while True:

    # get_question(...) -> util
    question = choice(questions)
    question_text = question["text"]
    question_pick = question["pick"]


    print(question_text)
    
    # ["a", "b", "c"] -enumerate-> [(0, "a"), (1, "b"), (2, "c")]
    for nr, a in enumerate(answers_sample):
        print( f"   {nr+1} {a}" )
    

    # user_select_answers(...)
    selected_answers = []
    
    while question_pick > len(selected_answers):
        run_loop, answer = handle_user_input(answers_sample)
        selected_answers.append(answer)

        if not run_loop:
            break
        
        if "____" in question_text:
            question_text = question_text.replace("____", answer, 1)
        else:
            question_text = question_text + "\n" + answer
    

    if not run_loop:
        break

    print(question_text + "\n")

    # remove_selected_answers(...) -> util
    for element in selected_answers:
        answers_sample.remove(element)
    if len(answers) < question_pick:
        answers = []
        answers.extend(answers_pool)
    
    # get_new_cards(...) -> util
    new_answers = get_new_cards(answers_sample, answers, question_pick)
    answers_sample = answers_sample + new_answers # TODO: Variable umbenennen
