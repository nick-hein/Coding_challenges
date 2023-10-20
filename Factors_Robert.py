print('Welcome to LCS Factor Finder! input any number and we will find all of it\'s factors.\n\n\n')

def finder():
    print('Input any number.')
    number = int(input(''))
    factorList = []
    deviList = []
    for i in range(0, number):
        deviList.append(number / (i+1))
        print(deviList[i])
        if deviList[i] % 1 == 0:
            factorList.append(int(deviList[i]))
    print('\nFactors of ' + str(number) + ': ' + str(factorList))
finder()