# -*- coding: utf-8 -*-
from Bio.Seq import Seq
from sys import argv
from Bio.Alphabet import IUPAC


def run():
    data_record = argv[1]

    transport_rna_seq = Seq(data_record, IUPAC.unambiguous_rna)
    temp_rna_seq = transport_rna_seq.back_transcribe()
    temp_rna_seq = str(temp_rna_seq)
    temp_rna_seq = Seq(temp_rna_seq, IUPAC.unambiguous_dna)
    dna_seq = temp_rna_seq.complement()
    dna_seq = str(dna_seq)

    print("<input type='text' value='" + dna_seq + "' name='seq_out' autocomplete='off' />")

if __name__ == "__main__":
    run()
