#!/usr/bin/en python3
# -*- coding: utf-8 -*-

"""Un exemple pour PyATM pour aider à formater le programme
avec la signature des differentes fonctions à définir.
La structure de PyATM pourrait ne pas être conforme à celle-ci.
Ceci est juste un modèle à titre indicatif. Vous pouvez définir
votre propre structure pour PyATM à la condition que celle-ci
respecte les exigences et spécificités de PyATM.

IMPORTANT
---------
Pour rentre ce modèle fonctionnel il faut supprimer toutes les
occurences du mot clé 'pass' et ensuite implémenter la fonction
principale 'main' et les autres fonctions auxilliaires.

Lire le fichier README.md situé dans le même dossier que ce 
fichier ci pour plus d'information sur PyATM.
"""

import sys

# Déclaration des variables

# Liste de tous les clients de notre banque fictive NetBank
# Elle servira de source de donnée au programme.
liste_clients = [["Alassane Dramane","OUATTARA","2101-0200-0100","Q2256-31793-AO000100100000-95","CI50-Q2256-31793-AO000100100000-95","Courant",55205775253,"XOF (FCFA)","adjfeiedc85r"],
                 ["Anne","LOTO","2101-0200-0101","Q2256-31793-AL000101100001-02","CI50-Q2256-31793-AL000101100001-02","Courant",28899997.1555,"XOF (FCFA)","qdjfeiedc85r"],
                 ["Ange Marie","Kouakou","2101-0200-0102","Q2256-00736-AK000100100002-04","CI50-Q2256-00736-AK000102100002-04","Courant",6491253.2021,"XOF (FCFA)","qdjfeiedc85r"],
                 ["Ahmed","BAKAYOKO","2102-0500-0103","Q2256-00028-AB000103100003-90","CI50-Q2256-00028-AB000103100003-90","Courant",70752431.1023,"XOF (FCFA)","qdjfeiedc85r"],
                 ["Patrick","ACHI","2102-0800-0104","Q2256-00028-PA000104100004-78","CI50-Q2256-00028-PA000104100004-78","Courant",35273846.897,"XOF (FCFA)","qdjfeiedc85r"],
                 ["Mamadou","COULIBALY","2103-1000-0105","Q2256-00093-,MC000105100005-59","CI50-Q2256-00093-MC000105100005-59","Courant",19930524.2812,"XOF (FCFA)","qdjfeiedc85r"],
                 ["Pascal Affi","N'GUSESSAN","2104-1100-0106","Q2256-10766-PN000106100006-32","CI50-Q2256-10766-PN000106100006-32","Courant",77815253.859,"XOF (FCFA)","qdjfeiedc85r"],
                 ["Konan Nicaise","KOUAKOU","2106-1200-0107","Q2256-31793-KK000107100007-16","CI50-Q2256-31793-KK000107100007-16","Courant",46478975253.341,"XOF (FCFA)","qdjfeiedc85r"],
                 ["Abdoul Karim","TOURE","2106-1200-0108","Q2256-31793-AT000108100008-18","CI50-Q2256-31793-AT000108100008-18","Courant",63289684251.685,"XOF (FCFA)","qdjfeiedc85r"],
                 ["Henri Konan","BEDIE","2106-2500-0109","Q2256-45678-HB000109100009-63","CI50-Q2256-45678-HB000109100009-63","Courant",12891547263.932,"XOF (FCFA)","qdjfeiedc85r"]]


# Représente l'ID du client actuel connecté
# A initialiser avec le numero de clientèle après authentication
client_id = None


# Définitions des fonctions prédéfinies ou importantes

# Authentifie le client
def auth(clientNO, clientPass):
  pass

# Affiche les info personels du client 
def info_client():
  pass

# Fait un depot sur le compte du client actuel
def depot(montant):
  pass

# Rétire un montant du compte du client actuel
def retrait(montant):
  pass

# Termine la session et quitte le programme
def fin():
  pass

# Autre definitions de fonctions secondaires ou personnalisées

# Il est permis de définir ses propres fonctions 
# dans cette section du programme.

# Cette function teste le programme. 
# Peut être simplement ignorée.
def test():
  pass


### ZONE IMPORTANTE ###

# La fonction principale du programme
def main(argv):
  # Cette fonction servira comme point d'entrée du programme
  # C'est ici que les autres fonctions sont invoquées. 
  # A l'exception des definitions de fonction tout le reste du code 
  # doit être écrit ici et pas ailleurs. J'insiste LE RESTE DU CODE
  # EST A ECRIRE ICI!!!
  pass


### ZONE ROUGE A NE PAS MODIFIER ###
if __name__ == '__main__':
  main(sys.argv[1:])
