#!/usr/bin/python
#NKS Program for acetylation and trimethylation identication
#28/08/2019
import csv
import re
from pyteomics import mzid, auxiliary
import timeit
import subprocess
import sys

t = timeit.default_timer()
print("start_time_in second=",t)
with open('Tackett_052015_WM115_1rep1.csv','r', newline='') as seq, open ("Tackett_052015_WM115_1rep1.mgf",'r') as fh:
	csv_reader = csv.reader(seq, delimiter=',')
	#csv_reader1 = next(csv_reader)

	x = 0
	d = dict()
	line =fh.readline()
	while line:
		line = line.rstrip('\n')
		#print('\n')
		if 'BEGIN IONS' in line:
			#d[key] = key_value
			key = x
			d[key] = ''
			x +=1
			#print(d)
		elif 'TITLE' in line:
			pass
		elif 'RTINSECONDS' in line:
			pass
		elif 'PEPMASS' in line:
			pass
		elif 'CHARGE' in line:
			pass
		else:
			if 'END IONS' not in line:
				#(firstWord, rest) = line.split(maxsplit=1)
				firstword = line.split(' ')
				key_value = firstword[0]
				d[key] += key_value + ' '
				#print(d)
			else:
				pass
		#print(d)
	
		line =fh.readline()

#print(d[2])

n = input("please enter spectra number",)
n = int(n)
peptide_mass_temp = d[n]
peptide_mass = peptide_mass_temp.split()
#print(peptide_mass)

AcTol = (20*126.012831)/1000000;
#AcTol = (20*42.04695)/1000000;
print(AcTol)
#for acetylation
for num, mass in enumerate(peptide_mass):
	#print(num)
	#print(mass)
	#print('\n')
	mass = float(mass)
	delta_mass = abs(mass-126.012831)
	for num1, mass_a in enumerate(peptide_mass):
		mass_a = float(mass_a)
		mass_diff = abs(delta_mass-mass_a)
		#print(mass_diff)
		if mass_diff <= AcTol:
			print("acetylation present in this peptide")
			print(mass_a)

		else:
			#print("acetylation not present in this peptide")
			#print(num1)
			#print(mass1)
			pass