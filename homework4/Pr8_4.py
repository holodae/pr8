try:
    firstNumber, secondNumber = int(input("Введите 1 число ")), int(input("Введите 2 число "))

    a, b = 0, 0
    if (firstNumber > secondNumber):
        a = firstNumber
        b = secondNumber
    else:
        a = secondNumber
        b = firstNumber 
    print(a, b)
    for i in range(b + 1, a): 
            print(i)
        
except ValueError:
    print("Неверный ввод!")
