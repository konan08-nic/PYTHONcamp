# Python Boot Camp: Apprendre Le Langage Python Facilement 

## Découvrez Python

### Pour la petite histoire

Python est un langage de programmation, dont la première version est sortie en 1991. Créé par **Guido van Rossum**, il a voyagé du Macintosh de son créateur, qui travaillait à cette époque au Centrum voor Wiskunde en Informatica aux Pays-Bas, jusqu'à se voir associer une organisation à but non lucratif particulièrement dévouée, la **Python Software Foundation**, créée en 2001. Ce langage a été baptisé ainsi en hommage à la troupe de comiques les «Monty Python».

### À quoi peut servir Python ?

Python est un langage puissant, à la fois facile à apprendre et riche en possibilités. Dès l'instant où vous l'installez sur votre ordinateur, vous disposez de nombreuses fonctionnalités intégrées au langage.

Il est, en outre, très facile d'étendre les fonctionnalités existantes, comme nous allons le voir. Ainsi, il existe ce qu'on appelle des bibliothèques qui aident le développeur à travailler sur des projets particuliers. Plusieurs bibliothèques peuvent ainsi être installées pour, par exemple, développer des interfaces graphiques en Python.

Concrètement, voilà ce qu'on peut faire avec Python :

   * de petits programmes très simples, appelés scripts, chargés d'une mission très précise sur votre ordinateur ;

   * des programmes complets, comme des jeux, des suites bureautiques, des logiciels multimédias, des clients de messagerie…

   * des projets très complexes, comme des progiciels (ensemble de plusieurs logiciels pouvant fonctionner ensemble, principalement utilisés dans le monde professionnel).

Voici quelques-unes des fonctionnalités offertes par Python et ses bibliothèques :

   * créer des interfaces graphiques ;

   * faire circuler des informations au travers d'un réseau ;

   * dialoguer d'une façon avancée avec votre système d'exploitation ;

   * et j'en passe…

Bien entendu, vous n'allez pas apprendre à faire tout cela en quelques minutes. Mais ce cours vous donnera des bases suffisamment larges pour développer des projets qui pourront devenir, par la suite, assez importants.

### Un langage de programmation interprété

Eh oui, vous allez devoir patienter encore un peu car il me reste deux ou trois choses à vous expliquer, et je suis persuadé qu'il est important de connaître un minimum ces détails qui peuvent sembler peu pratiques de prime abord.
Python est un langage de programmation **interprété**, c'est-à-dire que les instructions que vous lui envoyez sont « transcrites » en langage machine au fur et à mesure de leur lecture. D'autres langages (comme le C / C++) sont appelés « langages **compilés** » car, avant de pouvoir les exécuter, un logiciel spécialisé se charge de transformer le code du programme en langage machine. On appelle cette étape la «**compilation**». À chaque modification du code, il faut rappeler une étape de compilation.

Les avantages d'un langage interprété sont la simplicité (on ne passe pas par une étape de compilation avant d'exécuter son programme) et la portabilité (un langage tel que Python est censé fonctionner aussi bien sous Windows que sous Linux ou Mac OS, et on ne devrait avoir à effectuer aucun changement dans le code pour le passer d'un système à l'autre). Cela ne veut pas dire que les langages compilés ne sont pas portables, loin de là ! Mais on doit utiliser des compilateurs différents et, d'un système à l'autre, certaines instructions ne sont pas compatibles, voire se comportent différemment.

En contrepartie, un langage compilé se révélera bien plus rapide qu'un langage interprété (la traduction à la volée de votre programme ralentit l'exécution), bien que cette différence tende à se faire de moins en moins sentir au fil des améliorations. De plus, il faudra installer Python sur le système d'exploitation que vous utilisez pour que l'ordinateur puisse comprendre votre code.

### Différentes versions de Python

Lors de la création de la Python Software Foundation, en 2001, et durant les années qui ont suivi, le langage Python est passé par une suite de versions que l'on a englobées dans l'appellation Python 2.x (2.3, 2.5, 2.6…). Depuis le 13 février 2009, la version 3.0.1 est disponible. Cette version casse la **compatibilité ascendante** qui prévalait lors des dernières versions.

Quand un langage de programmation est mis à jour, les développeurs se gardent bien de supprimer ou de trop modifier d'anciennes fonctionnalités. L'intérêt est qu'un programme qui fonctionne sous une certaine version marchera toujours avec la nouvelle version en date. Cependant, la Python Software Foundation, observant un bon nombre de fonctionnalités obsolètes, mises en œuvre plusieurs fois… a décidé de nettoyer tout le projet. Un programme qui tourne à la perfection sous Python 2.x devra donc être mis à jour un minimum pour fonctionner de nouveau sous Python 3. C'est pourquoi je vais vous conseiller ultérieurement de télécharger et d'installer la dernière version en date de Python. Je m'attarderai en effet sur les fonctionnalités de Python 3 et certaines d'entre elles ne seront pas accessibles (ou pas sous le même nom) dans les anciennes versions.

## Installer Python

L'installation de Python est un jeu d'enfant, aussi bien sous Windows que sous les systèmes Unix. Quel que soit votre système d'exploitation, vous devez vous rendre sur [le site officiel de Python](https://www.python.org/downloads/).

## Lancer Python

### Sous Windows

Voici les différents moyens d'accéder à la ligne de commande Python que nous allons tout particulièrement étudier dans ce cours.
Vous avez plusieurs façons d'accéder à la ligne de commande Python, la plus évidente consistant à passer par les menus **Démarrer** >> **Tous les programmes** >> **Python 3.4** >> **Python (Command Line)**. Si tout se passe bien, vous devriez obtenir une magnifique console (figure suivante). Il se peut que les informations affichées dans la vôtre ne soient pas les mêmes, mais ne vous en inquiétez pas.

![Ligne de commande de Windows](https://user.oc-static.com/files/425001_426000/425782.jpg)

Vous pouvez également passer par la ligne de commande Windows ; à cause des raccourcis, je privilégie en général cette méthode, mais c'est une question de goût.
Allez dans le menu **Démarrer**, puis cliquez sur **Exécuter**. Dans la fenêtre qui s'affiche, tapez simplement « **py** » et la ligne de commande **Python** devrait s'afficher de nouveau. Sachez que vous pouvez directement vous rendre dans **Exécuter** en tapant le raccourci **Windows + R**.

Pour fermer l'interpréteur de commandes Python, vous pouvez taper « **exit()** » puis appuyer sur la touche **Entrée**.

### Sous Linux

Lorsque vous l'avez installé sur votre système, Python a créé un lien vers l'interpréteur sous la forme python3.X (le X étant le numéro de la version installée).

Si, par exemple, vous avez installé Python 3.4, vous pouvez y accéder grâce à la commande

    $ python3
    Python 3.4.0 (default, Apr 23 2014, 05:55:41)
    [GCC 4.4.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Pour fermer la ligne de commande Python, n'utilisez pas **CTRL** + **C** mais **CTRL** + **D**.



## Source

[Lien du cours sur openclassrooms.com](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python)
