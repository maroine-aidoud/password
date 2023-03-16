import hashlib
import json

MDP = str(input("Veuillez entrer votre mot de passe : "))

conditions = [
    lambda MDP: any(char.isupper() for char in MDP), 
    lambda MDP: any(char.islower() for char in MDP),
    lambda MDP: any(char.isdigit() for char in MDP),
    lambda MDP: any(char.isalnum() for char in MDP),
    lambda MDP: len(MDP) >= 8, ]

if all(condition(MDP) for condition in conditions):
    print("Le mot de passe est bon.")
else:
    print("Le mot de passe ne respecte pas toutes les conditions.")

hashed_MDP = hashlib.sha256(MDP.encode()).hexdigest()
print("Le mot de passe hashé est :", hashed_MDP)



MDP_dict = {"Mot de passe": hashed_MDP}

with open("MDP.json", "r") as fichier:
    data = json.load(fichier)

    print(data)


print(MDP_dict)

