import csv
from collections import Counter

file_name = input()

word_counter = Counter()

with open(file_name, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        for word in row:
            word_counter[word] += 1

for word, frequency in word_counter.items():
    print(f'{word} - {frequency}')
