import random

x=[]
i = 1
rep = random.choices(["123456", "password", "admin", "123456789", "qwerty", "abc123", "letmein", "welcome", "monkey", "football"])
while True:
    if i >= 4:
        print("Vous avez raté :( vous avez essayé " + str(x))
        break

    rep = str(rep).replace("'", '').replace('[', '').replace(']', "")
    #print(rep)
    print("Essaie de pass : ")
    essaie = input()
    print(len(essaie))
    if rep != essaie:
        x.append(essaie)
        if len(rep) > len(essaie):
            print("le mot de passe est plus long")
        elif len(rep) < len(essaie):
            print("le mot de passe est plus court")
        else:
            print("le mot de passe fait la même longeur")
        i = i+1
    
    else:
        print("Vous avez trouvé le mot de passe en " + str(i) + " tentative.s")
        break