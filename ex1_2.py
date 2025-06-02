import random

x=[]
rep=[]
i = 1
with open("fichier_pass.txt", "r") as f:
    for line in f:
        rep.append(line)
rep = random.choices(rep)
rep = str(rep)
while True:
    if i >= 4:
        print("Vous avez raté :( vous avez essayé " + str(x))
        print("le mot de passe était " + str(rep).strip('\n').strip("\t"))
        break

    rep = str(rep).replace("'", '').replace('[', '').replace(']', "")
    #print(rep)
    print("Essaie de pass : ")
    essaie = input()
    #print(len(essaie))
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