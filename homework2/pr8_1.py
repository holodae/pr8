while True:
    a = input("Введиет первое значение: ")
    
    if a.lower() == 'exit':
            print("Конец цикла")

            break
    b = input("Введите второе число:" )

    try:
        sum = int(a) + int(b)
        print(sum)
    except ValueError:
        print("Введиет корректное число")
