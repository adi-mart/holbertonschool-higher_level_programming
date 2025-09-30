# Python - Input/Output

Ce projet contient des exercices sur les opérations d'entrée/sortie en Python, incluant la manipulation de fichiers texte, la sérialisation/désérialisation JSON, et les classes.


## Description

Ce module explore en profondeur les opérations d'entrée/sortie en Python, offrant une approche complète de la manipulation de fichiers, de la sérialisation JSON et de la programmation orientée objet appliquée aux données.

### Concepts clés

#### 📁 **Input/Output (I/O)**
L'input/output désigne les opérations de lecture et d'écriture de données. En Python, cela inclut :
- **Input** : lecture de données depuis des fichiers, clavier, réseau, etc.
- **Output** : écriture de données vers des fichiers, écran, réseau, etc.

#### 🔄 **Sérialisation**
Processus de conversion d'un objet Python (liste, dictionnaire, classe) en format de données pouvant être stocké ou transmis :
- **But** : Sauvegarder l'état d'un objet dans un fichier ou l'envoyer sur le réseau
- **Formats courants** : JSON, XML, Pickle, CSV
- **Exemple** : `[1, 2, 3]` → `"[1, 2, 3]"` (format JSON)

#### 🔄 **Désérialisation**
Processus inverse de la sérialisation : conversion d'un format de données vers un objet Python :
- **But** : Reconstruire un objet Python à partir de données stockées
- **Exemple** : `"[1, 2, 3]"` → `[1, 2, 3]` (liste Python)

#### 📋 **JSON (JavaScript Object Notation)**
Format de données texte léger et lisible par les humains :
- **Avantages** : Simple, universel, lisible
- **Types supportés** : string, number, boolean, null, object, array
- **Usage** : APIs web, fichiers de configuration, échange de données

#### 🏗️ **Manipulation de fichiers**
Opérations de base sur les fichiers :
- **Lecture** (`r`) : Lire le contenu d'un fichier existant
- **Écriture** (`w`) : Créer/remplacer complètement un fichier
- **Ajout** (`a`) : Ajouter du contenu à la fin d'un fichier existant
- **Encodage UTF-8** : Standard pour gérer les caractères internationaux

#### 🎯 **Classes et objets**
Concepts de programmation orientée objet :
- **Classe** : Modèle/blueprint définissant des attributs et méthodes
- **Instance** : Objet créé à partir d'une classe
- **Attributs** : Variables stockant les données de l'objet
- **Méthodes** : Fonctions définies dans une classe


## Structure du projet

```
python-input_output/
├── README.md
├── 0-read_file.py          # Lecture de fichier texte
├── 0-main.py               # Test pour 0-read_file.py
├── 1-write_file.py         # Écriture dans un fichier
├── 1-main.py               # Test pour 1-write_file.py
├── 2-append_write.py       # Ajout de texte à un fichier
├── 2-main.py               # Test pour 2-append_write.py
├── 3-to_json_string.py     # Conversion objet vers JSON string
├── 3-main.py               # Test pour 3-to_json_string.py
├── 4-from_json_string.py   # Conversion JSON string vers objet
├── 4-main.py               # Test pour 4-from_json_string.py
├── 5-save_to_json_file.py  # Sauvegarde objet vers fichier JSON
├── 5-main.py               # Test pour 5-save_to_json_file.py
├── 6-load_from_json_file.py # Chargement objet depuis fichier JSON
├── 6-main.py               # Test pour 6-load_from_json_file.py
├── 7-add_item.py           # Script d'ajout d'éléments à une liste JSON
├── 8-class_to_json.py      # Conversion classe vers dictionnaire
├── 8-main.py               # Test pour 8-class_to_json.py
├── 8-main_2.py             # Test alternatif pour 8-class_to_json.py
├── 8-my_class.py           # Classe exemple pour test
├── 8-my_class_2.py         # Classe exemple 2 pour test
├── 9-student.py            # Classe Student basique
├── 9-main.py               # Test pour 9-student.py
├── 10-student.py           # Classe Student avec filtre
├── 10-main.py              # Test pour 10-student.py
├── 11-student.py           # Classe Student avec reload
├── 11-main.py              # Test pour 11-student.py
├── 12-pascal_triangle.py   # Triangle de Pascal
├── 12-main.py              # Test pour 12-pascal_triangle.py
└── __pycache__/            # Cache Python
```


## Tableau récapitulatif des fichiers

| Fichier | Description | Type | Fonctions/Classes principales |
|---------|-------------|------|-------------------------------|
| `0-read_file.py` | Lecture de fichier texte | Module | `read_file()` |
| `1-write_file.py` | Écriture dans un fichier | Module | `write_file()` |
| `2-append_write.py` | Ajout de texte à un fichier | Module | `append_write()` |
| `3-to_json_string.py` | Conversion objet → JSON string | Module | `to_json_string()` |
| `4-from_json_string.py` | Conversion JSON string → objet | Module | `from_json_string()` |
| `5-save_to_json_file.py` | Sauvegarde objet → fichier JSON | Module | `save_to_json_file()` |
| `6-load_from_json_file.py` | Chargement fichier JSON → objet | Module | `load_from_json_file()` |
| `7-add_item.py` | Script ajout éléments liste JSON | Script | Script exécutable |
| `8-class_to_json.py` | Conversion classe → dictionnaire | Module | `class_to_json()` |
| `9-student.py` | Classe Student basique | Classe | `Student`, `to_json()` |
| `10-student.py` | Classe Student avec filtre | Classe | `Student`, `to_json(attrs)` |
| `11-student.py` | Classe Student avec reload | Classe | `Student`, `to_json()`, `reload_from_json()` |
| `12-pascal_triangle.py` | Triangle de Pascal | Module | `pascal_triangle()` |

## Fichiers et Descriptions

### 0. Read file
**Fichier :** `0-read_file.py`

Fonction qui lit un fichier texte (UTF8) et l'affiche sur la sortie standard.

```python
def read_file(filename=""):
```

**Paramètres :**
- `filename` : nom du fichier à lire

---

### 1. Write to a file
**Fichier :** `1-write_file.py`

Fonction qui écrit une chaîne dans un fichier texte (UTF8) et retourne le nombre de caractères écrits.

```python
def write_file(filename="", text=""):
```

**Paramètres :**
- `filename` : nom du fichier où écrire
- `text` : texte à écrire dans le fichier

**Retour :** nombre de caractères écrits

---

### 2. Append to a file
**Fichier :** `2-append_write.py`

Fonction qui ajoute une chaîne à la fin d'un fichier texte (UTF8) et retourne le nombre de caractères ajoutés.

```python
def append_write(filename="", text=""):
```

**Paramètres :**
- `filename` : nom du fichier où ajouter du texte
- `text` : texte à ajouter au fichier

**Retour :** nombre de caractères ajoutés

---

### 3. To JSON string
**Fichier :** `3-to_json_string.py`

Fonction qui retourne la représentation JSON d'un objet sous forme de chaîne.

```python
def to_json_string(my_obj):
```

**Paramètres :**
- `my_obj` : objet à convertir en chaîne JSON

**Retour :** représentation JSON de l'objet

---

### 4. From JSON string to Object
**Fichier :** `4-from_json_string.py`

Fonction qui retourne un objet (structure de données Python) représenté par une chaîne JSON.

```python
def from_json_string(my_str):
```

**Paramètres :**
- `my_str` : chaîne JSON à convertir en objet

**Retour :** structure de données Python représentée par la chaîne JSON

---

### 5. Save Object to a file
**Fichier :** `5-save_to_json_file.py`

Fonction qui écrit un objet dans un fichier texte en utilisant une représentation JSON.

```python
def save_to_json_file(my_obj, filename):
```

**Paramètres :**
- `my_obj` : objet à sauvegarder
- `filename` : nom du fichier où sauvegarder

---

### 6. Create object from a JSON file
**Fichier :** `6-load_from_json_file.py`

Fonction qui crée un objet à partir d'un fichier JSON.

```python
def load_from_json_file(filename):
```

**Paramètres :**
- `filename` : nom du fichier JSON à charger

**Retour :** objet créé à partir du fichier JSON

---

### 7. Load, add, save
**Fichier :** `7-add_item.py`

Script qui ajoute tous les arguments à une liste Python, puis les sauvegarde dans un fichier JSON.

**Utilisation :**
```bash
./7-add_item.py arg1 arg2 arg3
```

Le script charge le fichier `add_item.json` s'il existe, ajoute les nouveaux arguments, et sauvegarde la liste mise à jour.

---

### 8. Class to JSON
**Fichier :** `8-class_to_json.py`

Fonction qui retourne la description sous forme de dictionnaire avec une structure de données simple pour la sérialisation JSON d'un objet.

```python
def class_to_json(obj):
```

**Paramètres :**
- `obj` : instance d'une classe

**Retour :** représentation sous forme de dictionnaire de l'objet

---

### 9. Student to JSON
**Fichier :** `9-student.py`

Classe qui définit un étudiant avec une méthode de sérialisation JSON.

```python
class Student:
    def __init__(self, first_name, last_name, age):
    def to_json(self):
```

**Attributs :**
- `first_name` : prénom de l'étudiant
- `last_name` : nom de famille de l'étudiant
- `age` : âge de l'étudiant

**Méthodes :**
- `to_json()` : retourne une représentation sous forme de dictionnaire

---

### 10. Student to JSON with filter
**Fichier :** `10-student.py`

Classe Student étendue avec un filtre d'attributs pour la sérialisation JSON.

```python
class Student:
    def __init__(self, first_name, last_name, age):
    def to_json(self, attrs=None):
```

**Méthodes :**
- `to_json(attrs=None)` : retourne une représentation sous forme de dictionnaire, optionnellement filtrée par une liste d'attributs

---

### 11. Student to disk and reload
**Fichier :** `11-student.py`

Classe Student avec la capacité de recharger ses attributs à partir d'un dictionnaire JSON.

```python
class Student:
    def __init__(self, first_name, last_name, age):
    def to_json(self, attrs=None):
    def reload_from_json(self, json):
```

**Méthodes :**
- `reload_from_json(json)` : remplace tous les attributs de l'instance Student

---

### 12. Pascal's Triangle
**Fichier :** `12-pascal_triangle.py`

Fonction qui retourne une liste de listes d'entiers représentant le triangle de Pascal de n.

```python
def pascal_triangle(n):
```

**Paramètres :**
- `n` : nombre de lignes du triangle de Pascal

**Retour :** liste de listes représentant le triangle de Pascal

## Utilisation

Chaque fichier peut être testé avec son fichier main correspondant :

```bash
# Exemple pour tester la lecture de fichier
python3 0-main.py

# Exemple pour tester l'écriture de fichier
python3 1-main.py

# Test du triangle de Pascal
python3 12-main.py
```

## Exigences

- Tous les fichiers sont interprétés/compilés sur Ubuntu 20.04 LTS en utilisant python3 (version 3.8.5)
- Tous les fichiers se terminent par une nouvelle ligne
- La première ligne de tous les fichiers est exactement `#!/usr/bin/python3`
- Le code utilise le style pycodestyle (version 2.8.*)
- Tous les fichiers sont exécutables
- La longueur des fichiers est testée en utilisant `wc`
- Tous les modules ont une documentation
- Toutes les classes ont une documentation
- Toutes les fonctions (internes et externes aux classes) ont une documentation

## Auteur

Ce projet fait partie du curriculum Holberton School.
Aurélie Di Martino