import random

# Gramática probabilística independiente del contexto (PCFG)
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": ["the", "a"],
    "N": ["cat", "dog", "ball"],
    "V": ["chased", "ate", "threw"]
}

def generate_sentence(grammar, symbol):
    if symbol not in grammar:
        # Si el símbolo no tiene producción, es un terminal (palabra)
        return symbol
    else:
        # Elegir una producción aleatoria para el símbolo no terminal
        production = random.choice(grammar[symbol])
        # Recursivamente generar las partes de la producción
        sentence = [generate_sentence(grammar, part) for part in production]
        return " ".join(sentence)

# Generar una oración aleatoria
sentence = generate_sentence(grammar, "S")
print("Oración generada:", sentence)
