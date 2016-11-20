# coding=utf-8
from nltk.metrics.distance import edit_distance
import codecs

# Reading aiml file
aiml = codecs.open("./core/base/cybora.aiml", "r", encoding="utf-8")

print aiml

questions = []

for line in aiml.readlines():
    print line.encode("utf-8")



phrase = 'meu nome é rodrigo e o seu?'


distance_less = len(phrase)

trigger = 'OI'

for q in questions:
    delta = edit_distance(phrase, q)
    if delta < distance_less:
        distance_less = delta
        trigger = q


print trigger, distance_less