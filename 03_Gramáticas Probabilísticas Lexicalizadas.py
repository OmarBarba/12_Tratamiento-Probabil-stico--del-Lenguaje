import random

# Define la gramática probabilística lexicalizada
lpcfg_rule = {
    "sentence": [
        {"rule": ["NP", "VP"], "weight": 1.0}
    ],
    "NP": [
        {"rule": ["Det", "N"], "weight": 0.6},
        {"rule": ["Det", "N", "PP"], "weight": 0.4}
    ],
    "VP": [
        {"rule": ["V", "NP"], "weight": 0.7},
        {"rule": ["V", "NP", "PP"], "weight": 0.3}
    ],
    "Det": [
        {"word": "El", "weight": 0.6},
        {"word": "un", "weight": 0.4}
    ],
    "N": [
        {"word": "gato", "weight": 0.5},
        {"word": "pescado", "weight": 0.5}
    ],
    "V": [
        {"word": "come", "weight": 0.7},
        {"word": "duerme", "weight": 0.3}
    ],
    "PP": [
        {"rule": ["Prep", "NP"], "weight": 1.0}
    ],
    "Prep": [
        {"word": "con", "weight": 1.0}
    ]
}

def generate_sentence(rule, lpcfg_rule):
    if "word" in rule:
        # Si la regla es una palabra, la retornamos
        return rule["word"]
    else:
        # Si la regla es una regla gramatical, elegimos una producción aleatoria
        production = random.choices(rule["rule"], weights=[r["weight"] for r in rule["rule"]])[0]
        # Generamos recursivamente cada parte de la producción
        generated_parts = [generate_sentence(lpcfg_rule[part], lpcfg_rule) for part in production]
        return " ".join(generated_parts)

# Generar una oración aleatoria
generated_sentence = generate_sentence(lpcfg_rule["sentence"][0], lpcfg_rule)
print("Oración generada:", generated_sentence)
