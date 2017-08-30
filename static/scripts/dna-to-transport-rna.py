# -*- coding: utf-8 -*-
from Bio.Seq import Seq
from sys import argv
from Bio.Alphabet import IUPAC


def run():
    data_record = argv[1]

    dna_seq = Seq(data_record, IUPAC.unambiguous_dna)
    temp_rna_seq = dna_seq.transcribe()
    temp_rna_seq = str(temp_rna_seq)
    temp_rna_seq = Seq(temp_rna_seq, IUPAC.unambiguous_rna)
    transport_rna_seq = temp_rna_seq.complement()
    transport_rna_seq = str(transport_rna_seq)

    print("<input type='text' value='" + transport_rna_seq + "' name='seq_out' autocomplete='off' />")

if __name__ == "__main__":
    run()
