# book-cipher-python

## Présentation

Ce projet consiste à réaliser un système de chiffrement basé sur le principe du **book cipher**.
L’idée est d’utiliser un texte (ici `lost.txt`) comme référence pour transformer un message en une suite de nombres, puis pouvoir retrouver le message initial.

---

## Principe de fonctionnement

### 1. Construction du dictionnaire

Le programme commence par lire le fichier texte (`lost.txt`).
Tous les mots sont :
* mis en minuscules
* nettoyés (suppression de la ponctuation)

Ensuite, chaque mot est associé à sa position dans le texte.
On obtient donc un dictionnaire :
**mot → liste des positions où il apparaît**

---

### 2. Chiffrement

Lorsque l’utilisateur choisit le mode *encrypt* :

* le message est découpé en mots
* chaque mot est recherché dans le dictionnaire
* s’il est trouvé, il est remplacé par une de ses positions
* on ajoute ensuite un **décalage (shift)** à cette position

On obtient ainsi une liste de nombres correspondant au message.

---

### 3. Déchiffrement

En mode *decrypt* :

* on entre une liste de nombres
* le programme enlève le shift
* il retrouve les mots correspondants dans le texte

Cela permet de reconstruire le message initial.

---

## Limites du projet

* Si un mot n’est pas présent dans le texte, il ne peut pas être chiffré
* Le système dépend entièrement du fichier utilisé (`lost.txt`)

---

## ▶️ Utilisation

Lancer le programme :

```bash
python main.py
```

Exemple chiffrement :

```text
Enter plaintext: with ten
encrypt or decrypt: encrypt
Shift value: 5
```

Exemple déchiffrement :

```text
Enter ciphertext: 23371 7491
encrypt or decrypt: decrypt
Shift value: 5
```

---

## 📁 Structure

```
secret_project/
 ├── main.py
 ├── cipher.py
 └── lost.txt

