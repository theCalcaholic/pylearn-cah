from cards import questions
from random import choice


def my_func(person_1, person_2, person_3):
    print("hello " + person_1)
    print("hello " + person_2)
    print("hello " + person_3)


my_name = "thomas"

my_func(my_name, "alfred", "guenther")


def smarte_addition(number_1, number_2):
    return number_1 + number_2



sum = smarte_addition(5, 7)
print(sum)

print(smarte_addition(1, 2))

print( smarte_addition(9, 8) ** 2)

def listen_summe(liste_1):
    summe = 0
    for number in liste_1:
        summe = summe + number
    return summe



print(listen_summe([1, 2, 3, 4, 5, 6]))


def ticktock(max):
    number = 1
    while number != max:
        if number % 3 == 0 and number % 5 == 0:
            print(str(number) + "Ticktock")
        else:
            if number % 3 == 0:
                print(str(number) + "Tick")
            if number % 5 == 0:
                print(str(number) + "Tock")
        
        number = number + 1


ticktock(17)
l = [1, 2, 3]
a = l[-1] #letzte
print(l[-2]) #vorletzte

def fibonacci(max):
    fibo_liszt = [0, 1]
    b = fibo_liszt[-1]
    while b < max:
        a = fibo_liszt[-2]
        b = fibo_liszt[-1]
        fibo_liszt.append(a + b)
    return fibo_liszt


print(fibonacci (100))

