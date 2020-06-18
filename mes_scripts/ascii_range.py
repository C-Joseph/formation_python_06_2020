#!/usr/bin/env python3
#
# ascii.py - Nicolas Pons
# Affiche les 128 caractères de la table ASCII
#
# Usage : ./ascii.py
#
# 2017.06.05 : version originale

#i=0
print("{:^12}{:^12}{:^12}{:^12}{:^12}".format("binaire","octal","hexadécimal","décimal","caractère"))
#while i<=128:
for i in range(0,128):
    print("{:>8b}    {:>8o}     {:>8X}     {:>8}  {:^12s}".format(i,i,i,i,chr(i)))
    i+=1
