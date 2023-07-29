"""
У нас є список показників студентів групи – це список з отриманими балами з тестування.
Необхідно поділити список на дві частини.
Напишіть функцію split_list, яка приймає список (цілі числа), знаходить середнє значення бала у списку
та ділить його на два списки. 
У перший потрапляють значення менше середнього, включаючи середнє значення, тоді як у другий — строго більше від середнього. 
Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.
"""


def split_list(grade):
    tuple_of_lists = ()
    above_average = []
    below_average = []
    
    for item in grade:
        sum_items = sum(grade)
        average = sum_items / int(len(grade))
        if item <= int(average):
            below_average.append(item) 
        elif item > int(average):
                above_average.append(item)
        elif len(grade) == 0:
                return above_average, below_average


    tuple_of_lists = (below_average, above_average)        
    
    return tuple_of_lists

print(split_list([1, 12, 3, 24, 5]))

