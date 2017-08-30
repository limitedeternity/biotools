# -*- coding: utf-8 -*-
from sys import argv
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


def run():

    data_record = argv[1]

    dna_seq = Seq(data_record, IUPAC.unambiguous_dna)
    messenger_rna = dna_seq.transcribe()
    messenger_rna = str(messenger_rna)

    print("<input type='text' value='" + messenger_rna + "' name='seq_out' autocomplete='off' />")

if __name__ == "__main__":
    run()
