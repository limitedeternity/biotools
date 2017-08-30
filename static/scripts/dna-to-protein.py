from Bio.Seq import Seq
from sys import argv
from Bio.Alphabet import IUPAC


def run():
    data_record = argv[1]

    dna_seq = Seq(data_record, IUPAC.unambiguous_dna)
    protein_seq = dna_seq.translate()
    protein_seq = str(protein_seq)

    print("<input type='text' value='" + "".join(protein_seq) + "' name='seq_out' autocomplete='off' />")

if __name__ == "__main__":
    run()
