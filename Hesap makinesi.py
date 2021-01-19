command = input("İşlem giriniz: ")


parseCommand = command.split()

if len(parseCommand) != 3:
    print("Yanlış işlem girdiniz.")
    exit(0)


try:
    number1 = int(parseCommand[0])
    operator = parseCommand[1]
    number2 = int(parseCommand[2])
except ValueError:
    print("Sayısal deger girmeniz gerekiyor.")
    exit(0)


if operator == '+':
    print(command, '=', number1 + number2)
elif operator == '-':
    print(command, '=', number1 + number2)
elif operator == '*':
    print(command, '=', number1 * number2)
elif operator == '/':
    print(command, '=', number1 / number2)