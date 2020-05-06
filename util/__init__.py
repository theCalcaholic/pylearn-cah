from random import choice, sample

def comprehension(a, b):
     return [x for x in a if x not in b]

def get_new_cards(answers_sample, answers, question_pick):
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