from random import choice, sample
from cards import questions, answers as answers_pool

def comprehension(a, b):
     return [x for x in a if x not in b]

def draw_cards(answers, question_pick):
    answers_sample = sample(answers, question_pick)
    for card in answers_sample:
        answers.remove(card)
    return answers_sample

def get_user_selection(inp, max_selection):
    
    if inp.lower() == "end":
        return -1
    else:
        selection = int(inp)
        #integrisieren
        if 0 < selection and selection <= max_selection:
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
        selection = get_user_selection(user_input, len(available_answers)) #siehe definition
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

def get_question():
    question = choice(questions)
    return question 

    # remove_selected_answers(...) -> util
def remove_selected_answers(selected_answers, hand_answers, question_pick):

    for element in selected_answers:
        hand_answers.remove(element)
    if len(answers) < question_pick:
        answers = []
        answers.extend(answers_pool)

    return answers, hand_answers