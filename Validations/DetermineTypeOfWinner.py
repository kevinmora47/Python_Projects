from Algorithm import GenerateNumbers
from Validations import UserInput


def determineWinner():
    winnerRandomValues = GenerateNumbers.createRandomNumbers()
    print("Estos son los resultados del lotto usalos para validar tus resultados.", winnerRandomValues)
    print("Ingresa los valores a participar:")
    userInputValues = UserInput.validateUserInput()

    numbersMatched = 0
    if userInputValues == winnerRandomValues:
        print("Haz ganado el premio mayor.")
    else:
        for i in userInputValues:
            for j in winnerRandomValues:
                if i == j:
                    numbersMatched += 1

    if numbersMatched == 2:
        print("Haz ganado 200 colones.")

    if numbersMatched == 3:
        print("Haz ganado 9500 colones.")

    if numbersMatched == 4:
        print("Haz ganado 100.000 colones.")

