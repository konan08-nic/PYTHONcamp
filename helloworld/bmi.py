nom=str(input("entrer votre nom svp \n"))
pr=str(input("entrer votre prenoms svp \n"))
taille=float(input("entrer la taille en cm svp \n"))
poids=int(input("entrer votre poids svp\n"))
an=int(input("entrer votre anneé de naissance svp \n"))
age=int(2020-an)
tail=float(taille/100)
bmi=int(poids//(tail*tail))
print("nom:",nom )
print("prénoms:",pr )
print("age:",age )
print("taille (m):",tail )
print("BMI:",bmi)



