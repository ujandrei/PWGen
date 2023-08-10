import random

class randomChar:
    def lowercaseRandomizer(self, n):
        lowercases = []
        for i in range(n):
            lowercaseRandom = random.choice('abcdefghijklmnopqrstuvwxyz')
            lowercases.append(lowercaseRandom)

        return lowercases

    def CapitalRandomizer(self, n):
        Capitals = []
        for i in range(n):
            letraAleatoria = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            Capitals.append(letraAleatoria)

        return Capitals
    
    def SpecialRandomizer(self, n):
        SpecialChar = []
        for i in range(n):
            randomSpecial = random.choice('!"#$%&()*+,-./:;<=>?@[\]^_`{|}~')
            SpecialChar.append(randomSpecial)

        return SpecialChar
    
    def NumberRandomizer(self, n):
        randomNumbers = []
        for i in range(n):
            numeroInteiro = random.randint(1, 9)
            randomNumbers.append(numeroInteiro)

        return randomNumbers

    


random_number_generator = randomChar()


resultado = random_number_generator.NumberRandomizer(5)

print(resultado)
    





