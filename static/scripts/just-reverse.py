# -*- coding: utf-8 -*-
from Bio.Seq import Seq
from sys import argv
from Bio.Alphabet import IUPAC


def run():
    data_record = argv[1]

    seq = Seq(data_record, IUPAC.unambiguous_dna)
    reversed_seq = seq[::-1]
    reversed_seq = str(reversed_seq)

    print("<input type='text' value='" + reversed_seq + "' name='seq_out' autocomplete='off' />")

if __name__ == "__main__":
    run()
