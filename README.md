
# TP4 – Implémentation de l'algorithme Minimax

## 🎯 Objectif

Ce projet a pour but d'implémenter l'algorithme **Minimax** sur un arbre de jeu fixe afin de :

- Déterminer la **valeur minimax de l'arbre**
- Identifier **le meilleur coup à jouer pour le joueur MAX** (entre les nœuds `b`, `c` ou `d`)

---

## 🧠 Structure de l'arbre

L'arbre de jeu est composé de 4 niveaux alternant entre les joueurs **MAX** et **MIN** :

```
            a (MAX)
         /     |     \
      b        c        d (MIN)
    /   \    /   \    /   |   \
   e     f  g     h  i    j    k (MAX)
  / \   / \ / \   / \ / \  / \  / \
 4  8  8  3 7  9  4 1 0 5 7  8 1  5 (MIN)
```

---

## 📂 Fichiers

- `minimax_tp4.py` : Contient le code Python de l'implémentation Minimax.
- `README.md` : Ce fichier de documentation.

---

## 🚀 Lancer le script

### Pré-requis
- Python 3.x installé

### Exécution

```bash
python minimax_tp4.py
```

---

## 📌 Résultats affichés

- ✅ **Valeur minimax de l'arbre** : la valeur optimale que peut garantir le joueur MAX.
- 🎯 **Meilleur coup pour MAX** : parmi les choix `b`, `c` et `d`.

---

## 🧪 Exemple de sortie

```
Valeur de b : 4
Valeur de c : 4
Valeur de d : 5
✅ Valeur minimax de l'arbre : 5
🎯 Meilleur coup pour MAX : d
```

---

## 📘 Concepts utilisés

- Algorithme Minimax
- Arbre de recherche à 2 joueurs (MAX vs MIN)
- Représentation d’un arbre avec un dictionnaire Python
- Appels récursifs
