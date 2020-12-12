import random
nbmax=10
nbmin=1
n= random.randint(1,100)
t=random.randrange(1,n,7)
reponse='oui'
nbsaisie=0
print("j'ai choisi un nombre compris entre 0 et 100, devinez-le!\n")
print("vous avez 10 essaies! \n")
while reponse=='oui' or reponse=='o':
    while nbsaisie!=t and nbmin<=nbmax:
       print("essaie N°",nbmin)
       print("===========")
       nbsaisie=int(input("votre devinette svp\n"))
       if nbsaisie==t:
           print("nombre correct")
           break
       else:
           print("0, le nombre n'est pas à la bonne place")       
           nbmin=nbmin+1
reponse=input("voulez vous continuer oui/non?")
