# ATM: Simulateur de Guichet Automatique 

> Un simple programme informatique en langage Python pour simuler un guichet automatique.


Le programme lorsqu'il est exécuté, affiche le montant du compte en XOF (CFA), en USD dollar Americain et en EURO 
avec les informations relatives au client.

Les détails du client sont:

- Nom et Prenom(s)
- Numero de clientèle de 12 chiffres (ex: 444-006-334-895)
- [Numero de compte ou Relevé d’Identité Bancaire (RIB)](https://fr.wikipedia.org/wiki/Basic_Bank_Account_Number)[1]
- [Numero IBAN (International Bank Account Number)](https://fr.wikipedia.org/wiki/International_Bank_Account_Number)[2]
- Type de compte (compte courant, épargne ou à terme)

## La compostion du IBAN

<table>
  <tr>
    <td>2</td> 
    <td>lettres	2 chiffres</td>
    <td>30 positions</td> 
  </tr>
  <tr>
    <td>CP</td>
    <td>CC</td>
    <td>BBAN</td>
  </tr>
</table>

> **CP**: Code du Pays

> **CC**: Clef de Controle

> **BBAN**: Basic Bank Account Number (c'est l'équivalent du Numero de Compte ou RIB)

La longueur d'un IBAN est fixe dans chaque pays avec au moins 14 caractères et un maximum de 34 caractères.

## Interface en ligne de command du programme

