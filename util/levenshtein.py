# coding=utf-8
from nltk.metrics.distance import edit_distance

questions = [
    'OLÁ',
    'OI',
    'TUDO BEM',
    'QUEM É VOCÊ',
    'O QUE É * BOT',
    'SEU NOME',
    'QUAL A SUA PROFISSÃO'
]

phrase = 'meu nome é rodrigo e o seu?'

distance_less = len(phrase)

trigger = 'OI'

for q in questions:
    delta = edit_distance(phrase, q)
    if delta < distance_less:
        distance_less = delta
        trigger = q


print trigger, distance_less