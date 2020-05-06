#!/usr/bin/env python

from cards import answers, questions
from random import choice, sample

def comprehension(a, b):
     return [x for x in a if x not in b]

def get_user_selection(inp):
    
    if inp.lower() == "end":
        return -1
    else:
        selection = int(inp)
        #integrisieren
        if 0 < selection and selection <= len(answers_sample):
            #Auswahl der Antwort
            return selection
    
    return None

def handle_user_input(available_answers): 
    """
    Umgang mit Input
    """
    
    selection = 0
    while True:
        user_input = input("Selection: ") #Eingabeaufforderung
        selection = get_user_selection(user_input) #siehe definition
        if selection == -1:
            #"end"
            return False, None
        elif selection is None:
            #Kein valider Input
            print("Try again!")
        else:
            #valider Input ohne "end"
            user_answer = available_answers[selection-1]
            return True, user_answer


answers_sample = []
new_answers = []
answers_sample = sample(answers, 3)
for card in answers_sample:
    answers.remove(card)

while True:
    #question = {"pick": 0}
    #while question["pick"] < 2:
    question = choice(questions)
    question_text = question["text"]
    question_pick = question["pick"]
    print(question_text)
    
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
            question_text = question_text.replace("____", answer, 1)
        else:
            question_text = question_text + "\n" + answer

    answers.extend(selected_answers)
    
    if not run_loop:
        break

    print(question_text + "\n")

    
    
    for element in selected_answers:
        answers_sample.remove(element)
    new_answers = sample(answers, question_pick)
    for hand_card in new_answers:
        answers.remove(hand_card)
    answers_sample = answers_sample + new_answers # TODO: Variable umbenennen
