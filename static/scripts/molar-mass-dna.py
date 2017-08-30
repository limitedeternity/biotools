# -*- coding: utf-8 -*-
from sys import argv


def nd_mass(nucleotide):
    if nucleotide is 'A':
        return float(135.013)
    if nucleotide is 'C':
        return float(111.1)
    if nucleotide is 'G':
        return float(151.13)
    if nucleotide is 'T':
        return float(126.1133)


def get_molar_mass(string):
    mass = 0
    for nucleotide in string:
        nucleotide_mass = nd_mass(nucleotide)
        nucleotide_mass = float(nucleotide_mass)
        mass = mass + nucleotide_mass
    return mass


def get_sequence():
    dna = argv[1]
    return dna


def run():
    sequence = get_sequence()
    molar_mass = round(get_molar_mass(sequence), 4)
    molar_mass = str(molar_mass)

    print("<ul><li>" + molar_mass + " g/mole." + "</li></ul>")


if __name__ == "__main__":
    run()
