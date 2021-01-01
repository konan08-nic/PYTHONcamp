# PyATM: Simulateur de Guichet Automatique 

Un simple programme informatique en langage Python pour simuler un guichet automatique.

# Généralité 

Le programme lorsqu'il est exécuté, affiche le montant du compte en XOF (CFA), en USD dollar Americain et en EURO 
avec les informations relatives au client.

Les détails du client sont:

- Nom et Prenom(s)
- Numero de clientèle de 12 chiffres (ex: 444-006-334-895)
- [Numero de compte, Basic Bank Account Number (BBAN) ou Relevé d’Identité Bancaire (RIB)](https://fr.wikipedia.org/wiki/Basic_Bank_Account_Number)
- [Numero IBAN (International Bank Account Number)](https://fr.wikipedia.org/wiki/International_Bank_Account_Number)
- Type de compte (compte courant, épargne ou à terme)

## La Compostion de l'RIB ou BBAN

Le **BBAN** ou **IRB** est une subdivision locale de l'**IBAN** délivré par la banque et que l'on remet à un débiteur ou un créancier dans le but d'opérer des virements bancaires ou des prélèvements bancaires à partir d'un compte courant.

<table>
  <tr>
    <td>3 à 12 positions</td> 
    <td>8 à 20 positions</td>
  </tr>
  <tr>
    <td>IID</td>
    <td>BAN</td>
  </tr>
</table>


```markdown
IID: identification de l’établissement financier
BAN: numéro de compte bancaire
```
Il n'a pas plus de 30 positions. Chaque pays a la responsabilité de définir le format de son BBAN.

### Exemple

- Côte d'Ivoire (24 caractères) Format: BBBBBGGGGGCCCCCCCCCCCCKK

  **B** = code banque (5 chiffres), **G** = code guichet (5 chiffres), **C** = numéro de compte (12 chiffres et/ou lettres), K = clé RIB (2 chiffres entre 01 et 97)

Un exemple de BBAN en Côte d'Ivoire serait: **AC152-76543-631117930638-04**

## La Compostion de l'IBAN

L'International Bank Account Number (IBAN), généralement nommé sous l'acronyme **IBAN**, est un système international de numérotation de comptes bancaires.

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

```markdown 
CP: Code ISO du Pays (ex: CI, FR, US, TR, PR, etc.)
CC: Clef de Controle (de 02 à 98)
BBAN: Basic Bank Account Number (c'est l'équivalent du Numero de Compte ou RIB)
```
La longueur d'un IBAN est fixe dans chaque pays avec au moins 14 caractères et un maximum de 34 caractères.

### Exemples

En Côte d'Ivoire exemples d'IBAN (28 caractères):

**CI90 A0152-76543-631117930638-04**

**CI93 BI008-01113-011342912005-89**

**CI50 B0015-27654-363111793063-80**

# Fonctionnalités

Le programme a les fonctionnalités suivantes:

- Permettre au client d'ouvrir un compte 
- Authentifier le client avec son numéro de clientèle de 12 chiffres et un mot de passe
- Afficher toutes les infos du client (nom, prénoms, BBN, IBAN, montant, etc.)
- Permettre au client de retirer de l'argent 
- Permettre au client de faire un dépôt 

# Interface en Ligne de Command (CLI)

