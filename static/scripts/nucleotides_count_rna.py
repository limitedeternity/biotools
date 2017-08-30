# -*- coding: utf-8 -*-
from sys import argv


def run():
	rna = argv[1]

	data_array = []
	for i in range(len(rna)):
		data_array.append(rna[:1])
		rna = rna[1:]

	all_nucleotides = []
	all_counts = []
	for base1 in ['A', 'U', 'G', 'C']:
		nucleotide = base1
		count = data_array.count(nucleotide)
		all_nucleotides.append(nucleotide)
		all_counts.append(count)

	zipped_list = zip(all_counts, all_nucleotides)
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
