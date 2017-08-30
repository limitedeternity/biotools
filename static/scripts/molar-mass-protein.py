# -*- coding: utf-8 -*-
from sys import argv

water = 18.01


def aa_mass(aminoacid):
    if aminoacid is 'A':
        return float(89.09)
    if aminoacid is 'B':
        return float(132.1179)
    if aminoacid is 'C':
        return float(132.12)
    if aminoacid is 'D':
        return float(133.11)
    if aminoacid is 'E':
        return float(147.13)
    if aminoacid is 'F':
        return float(165.19)
    if aminoacid is 'G':
        return float(75.0666)
    if aminoacid is 'H':
        return float(155.1546)
    if aminoacid is 'I':
        return float(131.1729)
    if aminoacid is 'K':
        return float(146.19)
    if aminoacid is 'L':
        return float(131.17)
    if aminoacid is 'M':
        return float(149.21)
    if aminoacid is 'N':
        return float(132.1179)
    if aminoacid is 'P':
        return float(115.13)
    if aminoacid is 'Q':
        return float(146.14)
    if aminoacid is 'R':
        return float(174.2)
    if aminoacid is 'S':
        return float(105.09)
    if aminoacid is 'T':
        return float(119.1192)
    if aminoacid is 'V':
        return float(117.151)
    if aminoacid is 'W':
        return float(204.225)
    if aminoacid is 'Y':
        return float(181.19)
    if aminoacid is 'Z':
        return float(146.14)
    if aminoacid is '*':
        return float(0.000)


def get_molar_mass(string):
    number_of_acids = 0
    mass = 0
    for aminoacid in string:
        aminoacid_mass = aa_mass(aminoacid)
        aminoacid_mass = float(aminoacid_mass)
        mass = mass + aminoacid_mass
        number_of_acids += 1

    mass_final = mass - (number_of_acids - 1) * water
    return mass_final


def get_sequence():
    protein = argv[1]
    return protein


def run():
    sequence = get_sequence()
    molar_mass = round(get_molar_mass(sequence), 4)
    molar_mass = str(molar_mass)

    print("<ul><li>" + molar_mass + " g/mole." + "</li></ul>")


if __name__ == "__main__":
    run()
