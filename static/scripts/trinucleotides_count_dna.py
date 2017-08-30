# -*- coding: utf-8 -*-
from sys import argv


def run():
    dna = argv[1]

    data_array = []
    for i in range(int(len(dna) / 3)):
        data_array.append(dna[:3])
        dna = dna[3:]

    all_trinucleotides = []
    all_counts = []
    for base1 in ['A', 'T', 'G', 'C']:
        for base2 in ['A', 'T', 'G', 'C']:
            for base3 in ['A', 'T', 'G', 'C']:
                trinucleotide = base1 + base2 + base3
                count = data_array.count(trinucleotide)
                all_trinucleotides.append(trinucleotide)
                all_counts.append(count)

    zipped_list = zip(all_counts, all_trinucleotides)
    dictionary = {}
    for value, item in zipped_list:
        if value != 0:
            dictionary[item] = value

    dictionary = str(dictionary)
    dictionary = dictionary.replace("{", "")
    dictionary = dictionary.replace("}", "")
    dictionary = dictionary.replace("'", "")
    dictionary = dictionary.replace(":", " -")

    print("<ul><li>" + dictionary + "</li></ul>")


if __name__ == "__main__":
    run()
