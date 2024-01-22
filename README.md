# Morse-Code

# Traducteur de Code Morse

Un programme simple en Python qui traduit du texte en code Morse et vice versa. Le programme utilise un dictionnaire prédéfini (`morse_code_alphabet`) qui fait correspondre des caractères à leurs représentations en code Morse.

## Utilisation

1. Exécutez le programme en lançant le script (`morse_code_translator.py`).
2. Choisissez une option :
    - Entrez `1` pour traduire du texte en code Morse.
    - Entrez `2` pour traduire du code Morse en texte.
    - Entrez `3` pour quitter le programme.

## Fonctions

### Texte vers Code Morse

```python
def text_to_morse(texte):
    # Traduit un texte donné en code Morse.
    # Entrée : texte (str) - Le texte à traduire.
    # Sortie : Affiche la représentation en code Morse.
```
###  Code Morse vers Texte

```python
def morse_to_text(code):
    # Traduit un code Morse donné en texte.
    # Entrée : code (str) - Le code Morse à traduire.
    # Sortie : Affiche le texte traduit.
```