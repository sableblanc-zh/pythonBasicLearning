import random

def rollTheDice(faces, attribut, difficulty_check):
    jet = random.randint(1, faces)
    
    print("Tu as eu " + str(jet) + " avec cette jette")
    if jet == faces:
        return "réussite - Critical"
    elif jet == 1:
        return "échec - Fumble"
    
    print("Ton attribut: " + str(attribut))
    print("Ton resultat final: " + str(jet + attribut))
    print("Comparer avec la difficulty: " + str(difficulty_check))
    if jet + attribut >= difficulty_check:
        return "réussite"
    else:
        return "échoue"


attribut = random.randint(-6, 6)
difficulte = random.randint(5, 30)
print(rollTheDice(20, attribut, difficulte))