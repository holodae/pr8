summ = 0


while True:
    input_user = input("Вводите знаечния: ")

    if input_user.lower() in ['stop', 'exit']:
        print("Цикл завершен", summ)
        break

    try:
        num = float(input_user)
        summ += num
        print("Сумма: ", summ)

    except ValueError:
         print("Введите корректные данные")
