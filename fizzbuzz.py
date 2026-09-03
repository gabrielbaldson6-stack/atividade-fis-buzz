# FizzBuzz
# Imprime os números de 1 a 30.
# Múltiplos de 3: Fizz
# Múltiplos de 5: Buzz
# Múltiplos de 3 e 5: FizzBuzz

for numero in range(1, 31):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
