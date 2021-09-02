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
import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score
from scipy import stats

t = timeit.default_timer()
print("start_time_in second=",t)

arr = os.listdir()
#print(arr)
pdeepmgf = []
experimentalmgf = []
csvfile = []
for names in arr:
	if names.endswith(".csv"):
		csvfile.append(names)
	elif names.endswith(".mgf"):
		experimentalmgf.append(names)
	elif names.startswith("out"):
		pdeepmgf.append(names)
print(pdeepmgf)
print(experimentalmgf)
print(csvfile)
#print(flh)


#filenum = 0
#for file in pdeepmgf:
	#pdeepmgf_file = pdeepmgf[filenum]
	#print(pdeepmgf_file)
	#filenum+=1
#print(dflh)


filenum = 0
for file in pdeepmgf:
	pdeepmgf_file = pdeepmgf[filenum]
	experimentalmgf_file = experimentalmgf[filenum]
	csvfile_file = csvfile[filenum]
	filenum+=1
	with open(csvfile_file,'r', newline='') as seq, open (experimentalmgf_file,'r') as fh, open (pdeepmgf_file,'r') as fh1, open(pdeepmgf_file, 'r') as f, open(csvfile_file+'exp_int.csv','w',newline='') as spec, open(csvfile_file+'cal_int.csv','w',newline='') as cal_spec, open(csvfile_file+'RESULT_CAL_VS_EXP.csv','w',newline='') as cal_vs_exp:
		csv_reader = csv.reader(seq, delimiter=',')
		csv_reader1 = next(csv_reader)
		store_values = csv.writer(f, delimiter=',')
		#store_values4 = csv.writer(spectra_key, delimiter=',')
		store_values5 = csv.writer(spec, delimiter=',')
		store_values6 = csv.writer(cal_spec, delimiter=',')
		store_values6 = csv.writer(cal_vs_exp, delimiter=',')

		store_values6.writerow(['key','spectrum_title','PSM_key','Modpep','Miss_cleavage','Protein','qvalue','Peptide_','Calculate_file_peptide','Charge_','Calculate_file_charge','rms','R2','pearson_coef','slope','intercept','r_value','r_value_square','p_value','std_err'])
	
	

		#Read mgf file and convert into dictionary 
		x = 0
		z=0
		d = dict()
		d_1 = dict()
		d_int = dict()
		d_mass = dict()
		line =fh.readline()
		while line:
			line = line.rstrip('\n')
			if 'BEGIN IONS' in line:
				key = x
				key_1 = z
				d[key] = ''
				d_1[key_1] = ''
				d_int[key_1] = ''
				d_mass[key_1] = ''
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
					d_int[key_1] += intencity_value +'|'
					d_mass[key_1] += key_value+'|'
				else:
					pass


			line =fh.readline()
		#print(d[35058])
		#Read CSV file and convert into dictionary 
		csv_dic = dict()
		for m_line in seq:
			#print(m_line)
			#print(m_line[1])
			line_1 = m_line.split(',')
			key_1 = line_1[5]
			spectrum_title = line_1[2]
			modpep = line_1[19]
			mc = line_1[20]
			protein = line_1[22]
			qvalue = line_1[47]
			peptide = line_1[16]
			charge = line_1[14]
			#print(line_1[50])
			if line_1[50] == '':
				pep_po_mod_charge = line_1[51]
				#print(pep_po_mod_charge)
				pep_po_mod_charge = peptide+'|'+charge
				#print(pep_po_mod_charge)
				pep_po_mod_charge = pep_po_mod_charge.split("|")
				#print(pep_po_mod_charge)
				pep_po_mod_charge = ''.join(pep_po_mod_charge)
				#print(pep_po_mod_charge)
			else:
				#print(lnv)

				pep_po_mod_charge = line_1[51]
				#print(pep_po_mod_charge)
				pep_po_mod_charge = pep_po_mod_charge
				#print(pep_po_mod_charge)
				pep_po_mod_charge = pep_po_mod_charge.split("|")
				#print(pep_po_mod_charge)
				pep_po_mod_charge = ''.join(pep_po_mod_charge)
				#print(pep_po_mod_charge)
				pep_po_mod_charge = pep_po_mod_charge.split(",")
				pep_po_mod_charge = ''.join(pep_po_mod_charge)
				#print(pep_po_mod_charge)
				pep_po_mod_charge = pep_po_mod_charge.split(";")
				pep_po_mod_charge = ''.join(pep_po_mod_charge)
				#print(pep_po_mod_charge)
				pep_po_mod_charge = pep_po_mod_charge.split('"')
				pep_po_mod_charge = ''.join(pep_po_mod_charge)
				pep_po_mod_charge = str(pep_po_mod_charge)
			#print(pep_po_mod_charge)
			#print(sdkjgvh)
			qvalue=qvalue.rstrip('\n')
			qvalue=qvalue.rstrip('\r')
			csv_dic[key_1] = spectrum_title+','+key_1+','+modpep+','+mc+','+protein+','+qvalue+','+peptide+','+charge+','+pep_po_mod_charge
	




		#read calculate intersity file and make dictionary
		pep_dic_1 = dict()
		pep_dic_mass_int = dict()
		pep_dic_int = dict()
		pep_dic_mass = dict()
		line_1 =fh1.readline()
		while line_1:
			line_1 = line_1.rstrip('\n')
			if 'BEGIN IONS' in line_1:
				pass
			elif 'TITLE=' in line_1:
				key_value = line_1
				key_value = key_value[6:]
				#key_value = ''.join(key_value)
				key_value = key_value.split("|")
				#print(key_value)
				key_value = ''.join(key_value)
				#print(key_value)
				key_value = key_value.split(",")
				key_value = ''.join(key_value)
				#print(key_value)
				key_value = key_value.split(";")
				key_value = ''.join(key_value)
				#print(key_value)
				#print(fhb)
				key_value = str(key_value)
				key_value_TITLE = key_value[:-1]
				charge_state =  key_value[-1]
				pep_detail = key_value
				peptide_mass_int = key_value
				peptide_int = key_value
				#print(peptide_int)
				#print(dkhgb)
				pep_dic_mass_int[peptide_mass_int] = ''
				pep_dic_int[peptide_int] = ''
				pep_dic_mass[peptide_int] = ''
				pep_dic_1[pep_detail] = ''
				#pep_num+=1
				pep_dic_1[pep_detail] = key_value_TITLE+''
			elif 'CHARGE' in line_1:
				key_value = line_1
				key_value = key_value.split("CHARGE=")
				key_value_CHARGE = ''.join(key_value)
				pep_dic_1[pep_detail] = key_value_TITLE+''+key_value_CHARGE+''
			elif 'pepinfo' in line_1:
				pass
			elif "b+1" in line_1:
				pass
			elif "b+2" in line_1:
				pass
			elif "y+1" in line_1:
				pass
			elif "y+2" in line_1:
				pass
			elif "PEPMASS" in line_1:
				key_value = line_1
				key_value = key_value.split("PEPMASS=")
				key_value_PEPMASS = ''.join(key_value)
				pep_dic_1[pep_detail] =  key_value_TITLE+'|'+key_value_CHARGE+'|'+key_value_PEPMASS+''
			else:
				if 'END IONS' not in line_1:
					firstword = line_1.split(' ')
					key_value = firstword[0]
					intencity_value = firstword[1]
					pep_dic_int[peptide_int] += intencity_value +','
					pep_dic_mass_int[peptide_mass_int] += key_value+" "+intencity_value +'|'
					pep_dic_mass[peptide_int] +=key_value+","
				else:
					pass
			line_1 =fh1.readline()


		#print(pep_dic_mass['TQEGTLTSDPYSFANSWALSSGEQHCQR26Carbamidomethyl[C]3'])
		#print(vfkjh)


		#compare calculated intensity with experimental intensity
		tol = 7
		key_1223 = ''
		for csv_file_value in csv_dic:
			csv_file_value_int = int(csv_file_value)
			csv_file_value_str = str(csv_file_value)
			cal_pep_key = csv_dic[csv_file_value_str]
			cal_pep_key = cal_pep_key.split(',')
			cal_pep_key_1 = cal_pep_key[8] #+cal_pep_key[7]
			cal_pep_key_1 = str(cal_pep_key_1)
			#print(cal_pep_key_1)
			spectra_mass_and_int = d_mass[csv_file_value_int].split("|")
			spectra_int = d_int[csv_file_value_int].split("|")
			cal_pep_key_1=cal_pep_key_1.rstrip('\n')
			cal_pep_key_1=cal_pep_key_1.rstrip('\r')
			#print(cal_pep_key_1)
			theo_mass = pep_dic_mass[cal_pep_key_1]#.split(",")
			theo_int = pep_dic_int[cal_pep_key_1].split(",")
			#print(theo_int)
			#print(fok)
			calculated_mass_and_intensity = pep_dic_mass_int[cal_pep_key_1]#.split("|")
			spectra_intensity_list = ''
			calculated_intensity_list = ''
			spectra_mass_list = ''
			calculated_mass_list = ''
			spectra_mass_list2 = []
			theo_mass = theo_mass[:-1]
			spectra_mass_and_int = spectra_mass_and_int[:-1]
			for spectra_mass_list_1 in spectra_mass_and_int:
				spectra_mass_list_1 = spectra_mass_list_1.strip()
				spectra_mass_list_1 = float(spectra_mass_list_1)
				spectra_mass_list2.append(spectra_mass_list_1)
				
			#print(theo_mass)
			theo_mass = theo_mass.split(',')
			#print(theo_mass)
			for theo_int_mass in theo_mass:
				#print(theo_int_mass)
				theo_int_mass_integer = float(theo_int_mass)
				def closest(lst, K): 
					return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
				nearest_mass = closest(spectra_mass_list2, theo_int_mass_integer)
				#print(nearest_mass)
				mass_tol = abs(theo_int_mass_integer-nearest_mass)
				tol_1 = (tol*theo_int_mass_integer)/1000000
				if mass_tol <= tol_1:
					#try:
						#nearest_mass = str(nearest_mass)
					spectra_mass_position = spectra_mass_list2.index(nearest_mass)
					#print(spectra_mass_position)
					#except ValueError:
						#nearest_mass = nearest_mass[:-2]
						#spectra_mass_position = spectra_mass_and_int.index(nearest_mass)		

					spectra_intensity_list += spectra_int[spectra_mass_position]+','
					spectra_mass_list+= str(nearest_mass)+','
					theo_int_mass = str(theo_int_mass)
					#print(theo_int_mass)
					theo_mass_position = theo_mass.index(theo_int_mass)
					#print(theo_mass_position)
					calculated_intensity_list += theo_int[theo_mass_position]+','
					calculated_mass_list += theo_int_mass+','	


			#print(spectra_intensity_list)
			#print(spectra_mass_list)
			#print(calculated_intensity_list)
			#print(calculated_mass_list)
			#print(dfkj)

			spectra_intensity_int = []
			spectra_intensity_list = spectra_intensity_list.split(',')
			for i in spectra_intensity_list:
				try:
					i = float(i)
				except ValueError:
					break;
				spectra_intensity_int.append(i)
			try:
				normalized_X = preprocessing.normalize([spectra_intensity_int])
			except ValueError:
				normalized_X = ''
				continue
			xyz = normalized_X.tolist()
			values = ','.join(str(v) for v in xyz)
			values = values.split(',')
			spec = open('exp_int.csv','w')
			spec_write = csv.writer(spec, lineterminator='\n')
			cal_spec = open('cal_int.csv','w')
			cal_write = csv.writer(cal_spec, lineterminator='\n')
			spec_write.writerow(['exp_int'])
			for int_list in values:
				int_list = str(int_list)
				int_list = int_list.strip('[')
				int_list = int_list.strip(']')
				spec_write.writerow([int_list])
			spec.close()

			spectra_int_count = len(values)
			calculated_intensity_list= calculated_intensity_list.split(',')
			calculate_int_count = len(calculated_intensity_list)
			if spectra_int_count < calculate_int_count:
				extranu = calculate_int_count-spectra_int_count
				calculated_intensity_list = calculated_intensity_list[:-extranu]
			elif spectra_int_count == calculate_int_count:
				pass
					

			cal_write.writerow(['cal_int'])
			#print(calculated_intensity_list)
			#calculated_intensity_list = calculated_intensity_list.split(',')
			for cal_spectra_int in calculated_intensity_list:
				cal_spectra_int = str(cal_spectra_int)
				cal_write.writerow([cal_spectra_int])
			
			cal_spec.close()
			expr_spectra = pd.read_csv('exp_int.csv')
			calu_spectra = pd.read_csv('cal_int.csv')
			ES = expr_spectra['exp_int']
			CS = calu_spectra['cal_int']
			rms1 = sqrt(mean_squared_error(ES,CS))
			R2 = r2_score(ES,CS)

			pearson_coef, p_value = stats.pearsonr(ES,CS)

			slope, intercept, r_value, p_value, std_err = stats.linregress(ES,CS)
			r_value_square = r_value**2
			PSM_detail = csv_dic[csv_file_value_str]
			PSM_detail = PSM_detail.split(',')
			spectrum_title_1 = PSM_detail[0]
			key_1 = PSM_detail[1]
			modpep_1 = PSM_detail[2]
			mc_1 = PSM_detail[3]
			protein_1 = PSM_detail[4]
			qvalue_1 = PSM_detail[5]
			peptide_1 = PSM_detail[6]
			charge_1 = PSM_detail[7]
			Calculate_file_peptide = pep_dic_1[cal_pep_key_1]
			Calculate_file_peptide = Calculate_file_peptide.split('|')
			Calculate_file_peptide_1 = Calculate_file_peptide[0]
			Calculate_file_charge = Calculate_file_peptide[1]

			store_values6.writerow([csv_file_value_str,spectrum_title_1,key_1,modpep_1,mc_1,protein_1,qvalue_1,peptide_1,Calculate_file_peptide_1,charge_1,Calculate_file_charge,rms1,R2,pearson_coef,slope,intercept,r_value,r_value_square,p_value,std_err])
			#filenum+=1
			#break


	os.remove(csvfile_file+'exp_int.csv')
	os.remove(csvfile_file+'cal_int.csv')
	os.remove('exp_int.csv')
	os.remove('cal_int.csv')

t1 = timeit.default_timer()
print("end_time_in second=",t1)
