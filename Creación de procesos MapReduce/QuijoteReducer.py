#!/usr/bin/python3

import sys
from collections import defaultdict

# Creamos un diccionario para almacenar las cuentas de palabras

word_counts = defaultdict(int)

# Sobre cada línea de entrada separamos la palabra de su conteo e incrementamos el contador

for line in sys.stdin:
    word, count = line.strip().split('\t')
    word_counts[word] += int(count)

# Ordenamos las palabras por sus recuentos y obtenemos las 10 más usadas
    
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# Imprimimos las 10 palabras más usadas

for word, count in sorted_word_counts:
    print(f"{word}\t{count}")
