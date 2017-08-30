# -*- coding: utf-8 -*-
from Bio.Seq import Seq
from sys import argv
from Bio.Alphabet import IUPAC


def run():
    data_record = argv[1]

    dna_seq = Seq(data_record, IUPAC.unambiguous_dna)
    complement_dna_seq = dna_seq.complement()
    complement_dna_seq = str(complement_dna_seq)

    print("<input type='text' value='" + complement_dna_seq + "' name='seq_out' autocomplete='off' />")

if __name__ == "__main__":
    run()
