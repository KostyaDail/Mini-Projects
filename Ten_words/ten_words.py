"""
Программа принимает на вход строку (текст) и считает количество слов в этой строке, затем выводит на печать 10
самых часто встречающихся слов. Для слов, имеющих одинаковую частотность, сортировка осуществляется по алфавиту.
"""

# введите свой текст и нажмите ctrl+D

import sys
from operator import itemgetter

input_strings = sys.stdin.readlines()
input_strings = "".join(input_strings).replace("…", "")
input_strings = input_strings.lower()
my_str = ""
for i in input_strings:
    my_str += i.strip("!?,.:-—")
my_str = my_str.split()
my_arr = ([i for i in my_str if len(i) >= 3])
my_arr.sort()

uniques = []
for word in my_arr:
    if word not in uniques:
        uniques.append(word)

counts = []
for unique in uniques:
    count = 0
    for word in my_arr:
        if word == unique:
            count += 1
    counts.append((count, unique))
counts.reverse()
counts = sorted(counts, key=itemgetter(0))
counts.reverse()

print("10 самых часто встречающихся слов в этом тексте:", end="\n\n")

for i in range(min(10, len(counts))):
    count, word = counts[i]
    print(f'{word}: {count}')
