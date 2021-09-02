#!/usr/bin/python
#NKS Program for pDeep tool for make peptide list
#28/08/2019
import csv
import re
from pyteomics import mzid, auxiliary
import timeit
import subprocess
import sys
import os


t = timeit.default_timer()
print("start_time_in second=",t)
with open('20180110_QE1_nLC2_BTW_SA_hs_293FT_p300tfxn-L_co_1.msgf_non_modified_PSM.csv','r', newline='') as seq, open ("20180110_QE1_nLC2_BTW_SA_hs_293FT_p300tfxn-L_co_1.mgf",'r') as fh, open ("20180110_QE1_nLC2_BTW_SA_hs_293FT_p300tfxn-L_co_1.mgf",'r') as fh1, open('out_PRESENT.csv', 'w',newline='') as f, open('out_ABSENT.csv', 'w',newline='') as FA:
	csv_reader = csv.reader(seq, delimiter=',')
	csv_reader1 = next(csv_reader)
	store_values = csv.writer(f, delimiter=',')
	store_values.writerow(["k","PSM_id_name","PSM_id_num","PSM_pep","PSM_MC","PSM_Protien","PSM_qvalue"])
	Resultfile = open("result_.mgf","w")
	Peptide_file = open("PEPTIDE_FILE.txt","w")
	Peptide_file.write("peptide")
	Peptide_file.write("\t")
	Peptide_file.write("modification")
	Peptide_file.write("\t")
	Peptide_file.write("charge")
	Peptide_file.write("\n")

	#Read mgf file and convert into dictionary 
	x = 0
	z=0
	d = dict()
	d_1 = dict()
	line =fh.readline()
	while line:
		line = line.rstrip('\n')
		if 'BEGIN IONS' in line:
			key = x
			key_1 = z
			d[key] = ''
			d_1[key_1] = ''
			x +=1
			z+=1
		elif 'TITLE' in line:
			key_1_value = line
			d_1[key_1] += key_1_value + ' '
			pass
		elif 'RTINSECONDS' in line:
			key_1_value = line
			d_1[key_1] += key_1_value + ' '
			pass
		elif 'PEPMASS' in line:
			key_1_value = line
			d_1[key_1] += key_1_value + ' '
			pass
		elif 'CHARGE' in line:
			key_1_value = line
			d_1[key_1] += key_1_value + ' '
			pass
		else:
			if 'END IONS' not in line:
				firstword = line.split(' ')
				key_value = firstword[0]
				intencity_value = firstword[1]
				d[key] += key_value+" "+intencity_value +'|'
			else:
				pass

		line =fh.readline()
	
	#Read CSV file and convert into dictionary 
	csv_dic = dict()
	for m_line in seq:
		line_1 = m_line.split(',')
		key_1 = line_1[4]
		spectrum_title = line_1[1]
		modpep = line_1[18]
		mc = line_1[19]
		protein = line_1[23]
		qvalue = line_1[48]
		peptide = line_1[15]
		qvalue=qvalue.rstrip('\n')
		qvalue=qvalue.rstrip('\r')
		csv_dic[key_1] = spectrum_title+','+key_1+','+modpep+','+mc+','+protein+','+qvalue+','+peptide

	#Read CSV and MGF file dictionary and seprate out match PSM spectra file
	try:
		for k in csv_dic:
			k_1 = int(k)
			peptide_mass_temp = d[k_1]
			spectra_detail = (d_1[k_1])
			peptide_mass = peptide_mass_temp.split("|")
			spectra_details_in_file = d_1[k_1].split()
			Resultfile.write(spectra_details_in_file[0])
			Resultfile.write('\n')
			Resultfile.write(spectra_details_in_file[1])
			Resultfile.write('\n')
			if 'CHARGE' in spectra_details_in_file[3]:
				Resultfile.write(spectra_details_in_file[2])
				Resultfile.write('\n')
				Resultfile.write(spectra_details_in_file[3])
				Resultfile.write('\n')

			else:
				Resultfile.write(spectra_details_in_file[2]+' '+spectra_details_in_file[3])
				Resultfile.write('\n')
				Resultfile.write(spectra_details_in_file[4])
		
			for mass_intst in peptide_mass:
				#print(mass_intst)
				Resultfile.write(mass_intst)
				Resultfile.write('\n')
			Resultfile.write("END IONS")
			Resultfile.write("\n")
			PSM_id_name = ''
			PSM_id_num = ''
			PSM_pep = ''
			PSM_MC = ''
			PSM_Protien = ''
			PSM_qvalue = ''
			num_1 = str(k)
			csv_dic_1 = csv_dic[num_1].split(',')
			PSM_id_name = csv_dic_1[0]
			PSM_id_num = csv_dic_1[1]
			PSM_pep = csv_dic_1[2]
			PSM_MC = csv_dic_1[3]
			PSM_Protien = csv_dic_1[4]
			PSM_qvalue = csv_dic_1[5]

			Peptide_file.write(csv_dic_1[6])
			Peptide_file.write("\t")
			#Peptide_file.write("")
			Peptide_file.write("\t")
			for spectra_charge in spectra_details_in_file:
				if "CHARGE" in spectra_charge:
					spectra_charge_1 = spectra_charge.split("CHARGE=")
					spectra_charge_1 = str(''.join(spectra_charge_1))
					spectra_charge_2 = spectra_charge_1[0]
					Peptide_file.write(spectra_charge_2)
					#Peptide_file.write("\t")
				else:
					pass
			Peptide_file.write("\n")

			store_values.writerow([k,PSM_id_name,PSM_id_num,PSM_pep,PSM_MC,PSM_Protien,PSM_qvalue])
	except ValueError:
		pass


Resultfile.close()
inp = open("result_.mgf", 'r')
out = open('result.mgf', 'w')
for line in inp:
	if len(line.strip()) > 0:
		out.write(line)
inp.close()
out.close()

os.remove('result_.mgf')

t1 = timeit.default_timer()
print("end_time_in second=",t1)
