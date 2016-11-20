# coding=utf-8
from nltk.metrics.distance import edit_distance
import codecs

# Array de questões
questions = []

# Lendo arquivo cybora
cybora_aiml = codecs.open("./core/base/cybora.aiml", "r", encoding="utf-8")

# Frase para teste
phrase = 'meu nome é rodrigo e o seu?'

# Menor distância
distance_less = len(phrase)

# Inicializa varivéis usadas no algoritmo
delta = 0
trigger = ''

# Inicia teste
for question in questions:
    # Calcula distância
    delta = edit_distance(phrase, question)
    # Verifica distância
    if delta < distance_less:
        # Atualiza resultados
        distance_less = delta
        trigger = question

print trigger, distance_less
