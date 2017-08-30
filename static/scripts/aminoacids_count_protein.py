# -*- coding: utf-8 -*-
from sys import argv


def run():
	protein = argv[1]

	data_array = []
	for i in range(len(protein)):
		data_array.append(protein[:1])
		protein = protein[1:]

	all_aminoacids = []
	all_counts = []
	for base1 in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', '*']:
		aminoacid = base1
		count = data_array.count(aminoacid)
		all_aminoacids.append(aminoacid)
		all_counts.append(count)

	zipped_list = zip(all_counts, all_aminoacids)

	dictionary = {}
	for value, item in zipped_list:
		if value != 0:
			dictionary[item] = value

	dictionary = str(dictionary)
	dictionary = dictionary.replace("{", "")
	dictionary = dictionary.replace("}", "")
	dictionary = dictionary.replace("'", "")
	dictionary = dictionary.replace(":", " -")

	print("<input type='text' value='" + dictionary + "' name='seq_out' autocomplete='off' />")


if __name__ == "__main__":
	run()
