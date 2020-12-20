
from random import randint
rp=1
nbmin = 1
nbmax = 10
s = randint(1,100)
v = 0
print("soyez les bienvenus(es) dans mon jeux \n")
print("J'ai choisi un nombre entre 1 et 100 \n")
print("devinez en",nbmax,"tentatives au maximum !\n")
while rp==1:
 while v!= s and nbmin <= nbmax:
  
  print("Essai no ",nbmin)
  v = int(input("Votre devinette svp:\n "))
  if s < v:
    print("pas juste")
  elif s > v:
    print("pas juste")
  else:
    print("Bravo ! Vous avez trouvé",v,"en",nbmin,"essai(s)")
  nbmin=nbmin+1

  if nbmin>nbmax and s!= v :
    print("Désolé, vous avez utilisé vos",nbmax,"essais en vain.")
    print("J'avais choisi le nombre",s,".")
 rp=input("voulez vous recommencer? 1-oui/2-non \n")

  
