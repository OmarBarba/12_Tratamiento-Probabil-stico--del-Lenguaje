import nltk
from nltk.translate import IBMModel1
from nltk.translate import AlignmentModel

# Descargar recursos de nltk necesarios
nltk.download("comtrans")

# Conjunto de datos de entrenamiento
parallel_corpus = nltk.corpus.comtrans.aligned_sents()

# Entrenar modelos de alineación IBM y HMM
ibm_model1 = IBMModel1(parallel_corpus, 5)
alignment_model = AlignmentModel(parallel_corpus, ibm_model1, 5)

# Oración en inglés a traducir
english_sentence = "The cat is on the mat."

# Realizar la traducción
spanish_translation = []
for word in english_sentence.split():
    translations = alignment_model.translation_table[word]
    if translations:
        best_translation = max(translations, key=lambda t: t[1])
        spanish_translation.append(best_translation[0])
    else:
        # Si no se encuentra una traducción, se mantiene la palabra en inglés
        spanish_translation.append(word)

# Unir las palabras traducidas en una oración
spanish_translation = " ".join(spanish_translation)

# Imprimir la traducción
print("Oración en inglés:", english_sentence)
print("Traducción al español:", spanish_translation)
