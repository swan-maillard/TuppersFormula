# The Tupper's Formula (Everything Formula)

## Description

Ce projet est une application interactive en Python qui repose sur la formule de Tupper, une formule mathématique qui, lorsqu'elle est utilisée avec un certain entier `K`, permet de visualiser une image de 106*17 pixels. 
L'utilisateur peut soit dessiner une image directement dans une grille interactive, soit entrer une valeur de `K` pour afficher l'image associée à ce nombre.

La valeur de `K` est calculée en interprétant la grille de dessin et peut ensuite être copiée dans le presse-papiers.

La formule de Tupper est une inégalité définie par :

```
1/2 < ⌊ mod(⌊y/17⌋ 2^(-17⌊x⌋ - mod(⌊y⌋, 17)), 2) ⌋
```

Elle permet de générer des images en fonction d'un entier `K` très grand, où `x` et `y` sont les coordonnées des pixels.

Voir plus sur la Formule de Tupper : https://clairelommeblog.fr/2022/10/16/la-formule-autoreferente-de-tupper/

## Fonctionnalités

- **Dessin interactif** : L'utilisateur peut dessiner des pixels sur une grille de 106 colonnes et 17 lignes.
- **Calcul du nombre `K`** : L'application calcule le nombre `K` correspondant à l'image dessinée et le copie dans le presse-papiers.
- **Affichage de l'image pour un `K` donné** : L'utilisateur peut entrer une valeur de `K`, et l'image associée à ce nombre est affichée.
- **Réinitialisation** : Il est possible de réinitialiser la grille pour effacer tous les pixels.

## Prérequis

Avant d'exécuter l'application, assurez-vous d'avoir installé les dépendances nécessaires. Vous pouvez les installer via `pip` :

```bash
pip install arcade matplotlib tk
```

### Bibliothèques utilisées :
- **arcade** : Pour l'interface graphique de la grille de dessin.
- **matplotlib** : Pour la génération et l'affichage du graphique correspondant à la formule de Tupper.
- **tkinter** : Pour la saisie de la valeur `K` et la gestion des fenêtres d'entrée utilisateur.

## Installation

1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/swan-maillard/TuppersFormula.git
   ```

2. Accédez au répertoire du projet :
   ```bash
   cd TuppersFormula
   ```

3. Installez les dépendances :
   ```bash
   pip install arcade matplotlib tk
   ```

4. Lancez le programme :
   ```bash
   python main.py
   ```

## Utilisation

### Dessiner une image

1. Cliquez dans la grille pour allumer ou éteindre les pixels.
2. Lorsque vous êtes satisfait du dessin, cliquez sur **Plot** pour générer le nombre `K`.
3. L'image correspondant à votre dessin sera affichée à l'aide de `matplotlib`, et le nombre `K` sera copié dans le presse-papiers.

### Saisir une valeur de `K`

1. Cliquez sur le bouton **Input a K**.
2. Saisissez un entier divisible par 17 et cliquez sur **Plot** pour afficher l'image correspondante.
3. Si `K` n'est pas divisible par 17, un message d'erreur sera affiché.

## Auteurs

- Swan Maillard (maillard.swan@gmail.com)

## Licence

Ce projet est sous licence MIT. Veuillez consulter le fichier `LICENSE` pour plus d'informations.
