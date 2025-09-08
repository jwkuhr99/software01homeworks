import random

#genereer een code van 3 getallen tussen de 0 en de 9
code_3_digits = [random.randint(0, 9) for _ in range(3)]

#genereer een code van 4 getallen tussen de 1 en de 6
code_4_digits = [random.randint(1, 6) for _ in range(4)]

#laat de resultaten zien
print("3-digit combination code: ", code_3_digits)
print("4-digit combination code: ", code_4_digits)
