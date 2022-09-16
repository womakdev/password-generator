
import random


#Les différents caractères qui peuvent être générés
numbers = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
letters = "a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"
capital_letters = "A", "Z", "E", "R", "T", "U", "I", "O", "P", "Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "W", "X", "C", "V", "B", "N"
symbols = "&", "é", "(", "-", "_", "ç", ")" "=", "+", "$", "*", "^", "ù", ":", "!", ";", ",", "?"





#Affichage du questionnement ainsi que du résultat
if 1:
    lenght = int(input("Combien de caractères voulez-vous ? : "))
    passwd = ""
    for x in range(0,lenght):
        variable = random.choice(numbers + letters + capital_letters + symbols)
        password = passwd + variable
        print(password, end='')