
from collections import defaultdict
import random

class BigramModel:
    def __init__(self, corpus):
        self.bigram_counts = defaultdict(int)
        self.unigram_counts = defaultdict(int)
        self.build_model(corpus)

    def build_model(self, corpus):
        for sentence in corpus:
            tokens = sentence.split()
            for i in range(len(tokens) - 1):
                bigram = (tokens[i], tokens[i+1])
                self.bigram_counts[bigram] += 1
                self.unigram_counts[tokens[i]] += 1

    def generate_text(self, seed_word, max_length=20):
        generated_text = [seed_word]
        current_word = seed_word

        for _ in range(max_length):
            next_word = self.sample_next_word(current_word)
            if next_word is None:
                break
            generated_text.append(next_word)
            current_word = next_word

        return " ".join(generated_text)

    def sample_next_word(self, current_word):
        candidates = [word for word in self.unigram_counts.keys() if (current_word, word) in self.bigram_counts]
        if not candidates:
            return None
        probabilities = [self.bigram_counts[(current_word, word)] / self.unigram_counts[current_word] for word in candidates]
        next_word = random.choices(candidates, probabilities)[0]
        return next_word

# Ejemplo de uso
corpus = ["el gato come", "el perro duerme", "el pájaro canta", "el gato duerme", "el perro come"]

# Crear un modelo de bigrama a partir del corpus
bigram_model = BigramModel(corpus)

# Generar texto a partir de una palabra de inicio
generated_text = bigram_model.generate_text("el", max_length=10)

print("Texto generado:")
print(generated_text)
