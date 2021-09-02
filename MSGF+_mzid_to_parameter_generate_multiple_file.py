#!/usr/bin/python
#NKS Program for mzid file read and save in csv file
#11/4/2019
import csv
import re
from pyteomics import mzid, auxiliary
import timeit
import subprocess
import sys
import os

t = timeit.default_timer()
print("start_time_in second=",t)

#def install(package):
   # subprocess.call([sys.executable, "-m", "pip", "install", pyteomics])

#def install(package):
    #subprocess.call([sys.executable, "-m", "pip", "install", timeit])


#def read_sequencefile(line):
#with open("humanprotein.fasta", 'r') as fh:
arr = os.listdir()
#print(arr)
newlist = []
for names in arr:
	if names.endswith(".mzid"):
		newlist.append(names)
#print(newlist)


for filename in newlist:
	if '.mzid' in filename:
		print(filename)
		with mzid.read(filename) as fh, open(filename+'.csv','w',newline='') as csvFile:
			#csv_reader = csv.reader(seq, delimiter=',')
			#csv_reader1 = next(csv_reader)
			#print('a')

			store_values = csv.writer(csvFile, delimiter=',')
			store_values.writerow(["scanfile","spectrum_title","ID","spectrumID","spectrumID1","scan_number","rank","DissociationMethod","experimentalMassToCharge","calculatedMassToCharge","DM","absdM","IsotopeError","charge_state","precursorError","BasePeptideSequence","Petide_length","Peptide","Modifiedpeptide","miss_cleavage","Enery","enzN","enzC","Protein","protein_length","start_position","end_position","pre_position","post_position","isDecoy","MSGF_RawScore","MSGF_DeNovoScore","MSGF_SpecEValue","MSGF_EValue","ExplainedIonCurrentRatio","NTermIonCurrentRatio","CTermIonCurrentRatio","MS2IonCurrent","NumMatchedMainIons","MeanErrorAll","StdevErrorAll","MeanErrorTop7","StdevErrorTop7","MeanRelErrorAll","StdevRelErrorAll","MeanRelErrorTop7","StdevRelErrorTop7","ScoreRatio","MSGF_QValue","position and modification","pep_pos_mod_charge"])
			#spectrumID, charge_state, experimentalMassToCharge, calculatedMassToCharge, rank, passThreshold, start_position, end_position, pre_position, post_position, isDecoy, protein_length, accession_no, protein_description, numDatabaseSequences, decoy_DB_accession_regexp, PeptideSequence, MSGF_RawScore, MSGF_DeNovoScore, MSGF_SpecEValue, MSGF_EValue, MSGF_QValue, MSGF_PepQValue, IsotopeError, DissociationMethod, ExplainedIonCurrentRatio, NTermIonCurrentRatio, CTermIonCurrentRatio, MS2IonCurrent, NumMatchedMainIons, MeanErrorAll, StdevErrorAll, MeanErrorTop7, StdevErrorTop7, MeanRelErrorAll, StdevRelErrorAll, MeanRelErrorTop7, StdevRelErrorTop7, PeptideSequence, PeptideSequence, scan_number, scanfile
			#{'spectrumID': 'index=20086', 'SpectrumIdentificationItem': [{'chargeState': 3, 'experimentalMassToCharge': 1083.90869140625, 'calculatedMassToCharge': 1083.904052734375, 'rank': 1, 'passThreshold': True, 'PeptideEvidenceRef': [{'start': 441, 'end': 471, 'pre': 'R', 'post': '-', 'isDecoy': False, 'length': 471, 'accession': 'sp|P00634|PPB_ECOLI', 'protein description': 'sp|P00634|PPB_ECOLI ALKALINE PHOSPHATASE PRECURSOR (EC 3.1.3.1) (APASE) - Escherichia coli.', 'numDatabaseSequences': 3636, 'location': '/root/Desktop/MSGFPlus_v20190214_Copy/target_18mix_db_contaminants_haemofilus.fasta', 'FileFormat': 'FASTA format', 'DatabaseName': {'target_18mix_db_contaminants_haemofilus.fasta': ''}, 'DB composition target+decoy': '', 'decoy DB accession regexp': '^XXX', 'decoy DB type reverse': '', 'PeptideSequence': 'IAAYGPHAANVVGLTDQTDLFYTMKAALGLK'}], 'MS-GF:RawScore': 136.0, 'MS-GF:DeNovoScore': 153.0, 'MS-GF:SpecEValue': 1.5565752e-28, 'MS-GF:EValue': 1.7425549e-22, 'MS-GF:QValue': 0.0, 'MS-GF:PepQValue': 0.0, 'IsotopeError': 0.0, 'AssumedDissociationMethod': 'CID', 'ExplainedIonCurrentRatio': 0.022732995, 'NTermIonCurrentRatio': 0.0088539235, 'CTermIonCurrentRatio': 0.013879072, 'MS2IonCurrent': 12195.4795, 'NumMatchedMainIons': 9.0, 'MeanErrorAll': 8.037273, 'StdevErrorAll': 7.000131, 'MeanErrorTop7': 9.694502, 'StdevErrorTop7': 7.1135473, 'MeanRelErrorAll': -2.5907357, 'StdevRelErrorAll': 10.33865, 'MeanRelErrorTop7': -3.4391441, 'StdevRelErrorTop7': 11.522075, 'PeptideSequence': 'IAAYGPHAANVVGLTDQTDLFYTMKAALGLK'}], 'spectrum title': 'B06-11073.10100.6104.6104.3', 'scan number(s)': 6104.0, 'scan start time': 3933.02, 'location': '/root/Desktop/MSGFPlus_v20190214_Copy/Mix3_LTQFT.mgf', 'name': 'Mix3_LTQFT.mgf', 'FileFormat': 'Mascot MGF file', 'SpectrumIDFormat': 'multiple peak list nativeID format'}
			#print('b')
			z=0
			num = 0
			#m=''
			line =fh.readline()
			line = line.decode()
			while line:
		
				if "<SpectrumIdentificationResult" in line:
					line = line.rstrip('\n')
					line = line.rstrip('>')
					line1 = line.split('=')
			
					#print(line1)
					#print(line1[4][1:-1])
					s = line1[4]#[2]#[1:-3]
					s11 = s.strip('"')
					#print(s)
					s11 = s11[0:-3]
					#print(s11)
					#print(fkjhb)
					m = fh[s11]
					#print("m",m)
					#print(odgjn)
					#break;
					try:
						scanfile=''
						spectrumID=''
						scan_number=''
						rank=''
						DissociationMethod=''
						experimentalMassToCharge=''
						calculatedMassToCharge=''
						DM=''
						absdM=''
						IsotopeError=''
						charge_state=''
						precursorError=''
						PeptideSequence=''
						Petide_length=''
						Peptide=''
						modifiedpeptide=''
						miss_cleavage=''
						Enery=''
						enzN=''
						enzC=''
						Protein=''
						protein_length=''
						start_position=''
						end_position=''
						pre_position=''
						post_position=''
						isDecoy=''
						MSGF_RawScore=''
						MSGF_DeNovoScore=''
						MSGF_SpecEValue=''
						MSGF_EValue=''
						MSGF_QValue=''
						MSGF_PepQValue=''
						ExplainedIonCurrentRatio=''
						NTermIonCurrentRatio=''
						CTermIonCurrentRatio=''
						MS2IonCurrent=''
						NumMatchedMainIons=''
						MeanErrorAll=''
						StdevErrorAll=''
						MeanErrorTop7=''
						StdevErrorTop7=''
						MeanRelErrorAll=''
						StdevRelErrorAll=''
						MeanRelErrorTop7=''
						StdevRelErrorTop7=''
						ScoreRatio=''
						try:
							spectrumID = m['spectrumID']
							spectrumID1 = spectrumID.strip("index=")
							#print("spectrumID=",spectrumID1)

						except:
							pass

						try:
							spectrum_title = m["spectrum title"]
							#print('spectrum title= ', spectrum_title)
						except:
							pass

						try:
							scan_number = m['scan number(s)']
							#print('scan number(s)= ', m['scan number(s)'])
						except:
							pass

						try:
							scanfile = m['name']
							#print('scan file= ', m['name'])
						except:
							pass
		
						try:
							charge_state = m['SpectrumIdentificationItem'][0]['chargeState']
							#print('charge_state=', m['SpectrumIdentificationItem'][0]['chargeState'])
						except:
							pass

						try:
							experimentalMassToCharge = m['SpectrumIdentificationItem'][0]['experimentalMassToCharge']
							#print('experimentalMassToCharge= ', m['SpectrumIdentificationItem'][0]['experimentalMassToCharge'])
						except:
							pass

						try:
							calculatedMassToCharge = m['SpectrumIdentificationItem'][0]['calculatedMassToCharge']
							#print('calculatedMassToCharge= ', m['SpectrumIdentificationItem'][0]['calculatedMassToCharge'])
						except:
							pass
	
						try:
							rank = m['SpectrumIdentificationItem'][0]['rank']
							#print('rank= ', m['SpectrumIdentificationItem'][0]['rank'])
						except:
							pass
	
						try:
							passThreshold = m['SpectrumIdentificationItem'][0]['passThreshold']
							#print('passThreshold= ', m['SpectrumIdentificationItem'][0]['passThreshold'])
						except:
							pass

						try:
							start_position = m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['start']
							#print('start_position= ', m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['start'])
						except:
							pass

						try:
							end_position = m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['end']
							#print('end_position= ', m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['end'])
						except:
							pass
	
						try:
							pre_position = m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['pre']
							#print('pre_position= ', m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['pre'])
						except:
							pass

						try:
							post_position = m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['post']
							#print('post_position= ', m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['post'])
						except:
							pass
				
						try:
							isDecoy = m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['isDecoy']
							#print('isDecoy= ', m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['isDecoy'])
						except:
							pass			

						try:
							protein_length = m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['length']
							#print('protein_length= ', m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['length'])
						except:
							pass

						try:
							accession_no = m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['accession']
							#print('accession_no.= ', m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['accession'])
						except:
							pass

						#protein_description = m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['protein description']
						#print('protein_description= ', m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['protein description'])

						try:
							numDatabaseSequences = m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['numDatabaseSequences']
							#print('numDatabaseSequences= ', m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['numDatabaseSequences'])
						except:
							pass

						#decoy_DB_accession_regexp = m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['decoy DB accession regexp']
						#print('decoy DB accession regexp= ', m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['decoy DB accession regexp'])

						try:
							Protein=accession_no
							#print("Protein=",Protein)
						except:
							pass

						#if isDecoy == "True":
							#Protein=decoy_DB_accession_regexp+'_'+accession_no
							#print(Protein)
						#else:
							#Protein=accession_no
							#print(Protein)
		
						try:
							PeptideSequence = m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['PeptideSequence']
							#print('PeptideSequence= ', m['SpectrumIdentificationItem'][0]['PeptideEvidenceRef'][0]['PeptideSequence'])
						except:
							pass

						try:
							Peptide=pre_position+'.'+PeptideSequence+'.'+post_position
							#print('Peptide=',Peptide)
						except:
							pass

						try:
							MSGF_RawScore = m['SpectrumIdentificationItem'][0]['MS-GF:RawScore']
							#print('MS-GF:RawScore= ', m['SpectrumIdentificationItem'][0]['MS-GF:RawScore'])
						except:
							pass

						try:
							MSGF_DeNovoScore = m['SpectrumIdentificationItem'][0]['MS-GF:DeNovoScore']
							#print('MS-GF:DeNovoScore= ', m['SpectrumIdentificationItem'][0]['MS-GF:DeNovoScore'])
						except:
							pass

						try:
							MSGF_SpecEValue = m['SpectrumIdentificationItem'][0]['MS-GF:SpecEValue']
							#print('MS-GF:SpecEValue= ', m['SpectrumIdentificationItem'][0]['MS-GF:SpecEValue'])
						except:
							pass

						try:
							MSGF_EValue = m['SpectrumIdentificationItem'][0]['MS-GF:EValue']
							#print('MS-GF:EValue= ', m['SpectrumIdentificationItem'][0]['MS-GF:EValue'])
						except:
							pass

						#MSGF_QValue = m['SpectrumIdentificationItem'][0]['MS-GF:QValue']
						#print('MS-GF:QValue= ', m['SpectrumIdentificationItem'][0]['MS-GF:QValue'])

						#MSGF_PepQValue = m['SpectrumIdentificationItem'][0]['MS-GF:PepQValue']
						#print('MS-GF:PepQValue= ', m['SpectrumIdentificationItem'][0]['MS-GF:PepQValue'])
						try:
							IsotopeError = m['SpectrumIdentificationItem'][0]['IsotopeError']
							#print('IsotopeError= ', m['SpectrumIdentificationItem'][0]['IsotopeError'])
						except:
							pass

						try:
							DissociationMethod = m['SpectrumIdentificationItem'][0]['AssumedDissociationMethod']
							#print('AssumedDissociationMethod= ', m['SpectrumIdentificationItem'][0]['AssumedDissociationMethod'])
						except:
							pass

						try:
							ExplainedIonCurrentRatio = m['SpectrumIdentificationItem'][0]['ExplainedIonCurrentRatio']
							#print('ExplainedIonCurrentRatio= ', m['SpectrumIdentificationItem'][0]['ExplainedIonCurrentRatio'])
						except:
							pass

						try:
							NTermIonCurrentRatio = m['SpectrumIdentificationItem'][0]['NTermIonCurrentRatio']
							#print('NTermIonCurrentRatio= ', m['SpectrumIdentificationItem'][0]['NTermIonCurrentRatio'])
						except:
							pass

						try:
							CTermIonCurrentRatio = m['SpectrumIdentificationItem'][0]['CTermIonCurrentRatio']
							#print('CTermIonCurrentRatio= ', m['SpectrumIdentificationItem'][0]['CTermIonCurrentRatio'])
						except:
							pass
	
						try:
							MS2IonCurrent = m['SpectrumIdentificationItem'][0]['MS2IonCurrent']
							#print('MS2IonCurrent= ', m['SpectrumIdentificationItem'][0]['MS2IonCurrent'])
						except:
							pass

						try:
							NumMatchedMainIons = m['SpectrumIdentificationItem'][0]['NumMatchedMainIons']
							#print('NumMatchedMainIons= ', m['SpectrumIdentificationItem'][0]['NumMatchedMainIons'])
						except:
							pass

						try:
							MeanErrorAll = m['SpectrumIdentificationItem'][0]['MeanErrorAll']
							#print('MeanErrorAll= ', m['SpectrumIdentificationItem'][0]['MeanErrorAll'])
						except:
							pass

						try:
							StdevErrorAll = m['SpectrumIdentificationItem'][0]['StdevErrorAll']
							#print('StdevErrorAll= ', m['SpectrumIdentificationItem'][0]['StdevErrorAll'])
						except:
							pass

						try:
							MeanErrorTop7 = m['SpectrumIdentificationItem'][0]['MeanErrorTop7']
							#print('MeanErrorTop7= ', m['SpectrumIdentificationItem'][0]['MeanErrorTop7'])
						except:
							pass

						try:
							StdevErrorTop7 = m['SpectrumIdentificationItem'][0]['StdevErrorTop7']
							#print('StdevErrorTop7= ', m['SpectrumIdentificationItem'][0]['StdevErrorTop7'])
						except:
							pass
	
						try:
							MeanRelErrorAll = m['SpectrumIdentificationItem'][0]['MeanRelErrorAll']
							#print('MeanRelErrorAll= ', m['SpectrumIdentificationItem'][0]['MeanRelErrorAll'])
						except:
							pass

						try:
							StdevRelErrorAll = m['SpectrumIdentificationItem'][0]['StdevRelErrorAll']
							#print('StdevRelErrorAll= ', m['SpectrumIdentificationItem'][0]['StdevRelErrorAll'])
						except:
							pass

						try:
							MeanRelErrorTop7 = m['SpectrumIdentificationItem'][0]['MeanRelErrorTop7']
							#print('MeanRelErrorTop7= ', m['SpectrumIdentificationItem'][0]['MeanRelErrorTop7'])
						except:
							pass

						try:
							StdevRelErrorTop7 = m['SpectrumIdentificationItem'][0]['StdevRelErrorTop7']
							#print('StdevRelErrorTop7= ', m['SpectrumIdentificationItem'][0]['StdevRelErrorTop7'])
						except:
							pass

						try:
							PeptideSequence = m['SpectrumIdentificationItem'][0]['PeptideSequence']
							#print('PeptideSequence= ', m['SpectrumIdentificationItem'][0]['PeptideSequence'])
							PeptideSequence=str(PeptideSequence)
						except:
							pass
				
						try:
							s = 0
							#c=m['SpectrumIdentificationItem'][0]['Modification']
							if 'Modification' in m['SpectrumIdentificationItem'][0]:
								#print('hello')
								x = m['SpectrumIdentificationItem'][0]['Modification']
								#print("x",x)
								z = len(x)
								z -=1
								#print("z",z)
								t = 0
								PeptideSequence1 = PeptideSequence
								modification_type_list = []
								while s<=z:
									Modification_location = m['SpectrumIdentificationItem'][0]['Modification'][s]['location']
									#print('Modification_location= ', m['SpectrumIdentificationItem'][0]['Modification'][s]['location'])
				
									monoisotopicMassDelta = m['SpectrumIdentificationItem'][0]['Modification'][s]['monoisotopicMassDelta']
									#print('monoisotopicMassDelta= ', m['SpectrumIdentificationItem'][0]['Modification'][s]['monoisotopicMassDelta'])
									monoisotopicMassDelta = ("{0:.3f}".format(monoisotopicMassDelta))
									monoisotopicMassDelta=str(monoisotopicMassDelta)
						
									Modification_type = m['SpectrumIdentificationItem'][0]['Modification'][s]['name']
									#print('Modification_type= ', m['SpectrumIdentificationItem'][0]['Modification'][s]['name'])

									Modification_location +=t
					
									modifiedpeptide1 = PeptideSequence1[:Modification_location]+'+'+monoisotopicMassDelta+PeptideSequence1[Modification_location:]
									#modifiedpeptide = PeptideSequence+'+'+monoisotopicMassDelta+PeptideSequence
									#print('modifiedpeptide1=',modifiedpeptide1)
									PeptideSequence1 = modifiedpeptide1
									s+=1
									t+=7
			
							else:
								Modification_type ="none"
								#print("Modification_type=",Modification_type)
								Modification_location ="none"
								#print("Modification_location=",Modification_location)
								modifiedpeptide1 = PeptideSequence
								#print("modifiedpeptide1=",modifiedpeptide1)
						except:
							pass

						try:
							modifiedpeptide = pre_position+'.'+modifiedpeptide1+'.'+post_position
							#print('modifiedpeptide=',modifiedpeptide)
						except:
							pass
	
				
						try:
							ScoreRatio = MSGF_RawScore/MSGF_DeNovoScore
							#print("ScoreRatio=",ScoreRatio)
						except:
							pass

						try:
							Enery = MSGF_RawScore-MSGF_DeNovoScore
							#print("Enery=",Enery)
						except:
							pass

						try:
							Petide_length = len(PeptideSequence)
							#print("Petide_length",Petide_length)
						except:
							pass

						try:					
								#Difference between theoritical mass and experimental mass
								DM = calculatedMassToCharge-experimentalMassToCharge 
								#print("DM=",DM)
						except:
							pass

						try:
							#abstulute value of mass
							absdM = abs(DM)
							#print("abstulute value=",absdM)
						except:
							pass

						try:
							if Peptide[-3:]=='R.P':
								enzC="false"
								#print("enzC=",enzC)

							elif Peptide[-3:]=='K.P':
								enzC="false"
								#print("enzC=",enzC)

							else:
								enzC="true"
								#print("enzC=",enzC)

							if Peptide[:-3]=='R.D' :
								enzN="true"
								#print("enzN=",enzN)

							elif Peptide[:-3]== "K.D":
								enzN="true"
								#print("enzN=",enzN)

							else:
								enzN="false"
								#print("enzN=",enzN)
						except:
							pass

						try:
							C = 12.0
							C13 = 13.00335483
							IsotopeMass = C13 - C
							adjExpMz = experimentalMassToCharge-IsotopeMass*IsotopeError/charge_state
							#print("adjExpMz=",adjExpMz)
							precursorError=(adjExpMz-calculatedMassToCharge)/calculatedMassToCharge*1000000
							#print("precursorError=",precursorError)
						except:
							pass

						try:
							#Misscleavage calculate
							miss_cleavage_K = PeptideSequence.count("K")
							miss_cleavage_R =PeptideSequence.count("R")
							miss_cleavage_KP = PeptideSequence.count(('KP'))
							miss_cleavage_RP = PeptideSequence.count("RP")
							if PeptideSequence[-1] == 'K' or  PeptideSequence[-1] == 'R':
								miss_cleavage = miss_cleavage_K + miss_cleavage_R - miss_cleavage_KP - miss_cleavage_RP - 1
							else:
								miss_cleavage = miss_cleavage_K + miss_cleavage_R - miss_cleavage_KP - miss_cleavage_RP
							#print("miss_cleavage=",miss_cleavage)
						except:
							pass
				
						#print(z)
						#store_values.writerow([spectrumID,charge_state,experimentalMassToCharge,calculatedMassToCharge,rank,passThreshold,start_position,end_position,pre_position,post_position,isDecoy,protein_length,accession_no,numDatabaseSequences,decoy_DB_accession_regexp,PeptideSequence,MSGF_RawScore,MSGF_DeNovoScore,MSGF_SpecEValue,MSGF_EValue,MSGF_QValue,MSGF_PepQValue,IsotopeError,DissociationMethod,ExplainedIonCurrentRatio,NTermIonCurrentRatio,CTermIonCurrentRatio,MS2IonCurrent,NumMatchedMainIons,MeanErrorAll,StdevErrorAll,MeanErrorTop7,StdevErrorTop7,MeanRelErrorAll,StdevRelErrorAll,MeanRelErrorTop7,StdevRelErrorTop7,PeptideSequence,PeptideSequence,Modificationtype,Modification_location,scan_number,scanfile,Protein,Peptide,modifiedpeptide,precursorError,miss_cleavage,enzN,enzC])
						#row+=1
						z+=1
						#print(z)
					except:
						pass
					try:
						MSGF_QValue = m['SpectrumIdentificationItem'][0]['MS-GF:QValue']
					except:
						pass	
						
					mod_dic = {'+79.966':'Phosphorylation[S-T-Y]','+57.021':'Carbamidomethyl[C]','+15.995':'Oxidation[M]','+42.011':'Acetylation[*]'}
					total_modification = modifiedpeptide.count('+')
					#print(total_modification)
					d_num =0
					mod_pos_list = []
					mod_type_list = []
					for A,N in enumerate(modifiedpeptide):
						if '+' in N:
							P = A+7
							mod_mass = modifiedpeptide[A:P]
							try:
								mod_type = mod_dic[mod_mass]
							except:
								pass
							A -=2+d_num
							mod_pos_list.append(A)
							mod_type_list.append(mod_type)
							d_num+=7
					#print(mod_pos_list)
					#print(mod_type_list)
					lisnum =0
					pos_and_mod_list = []
					for list in mod_pos_list:
						mod_pos = mod_pos_list[lisnum]
						mod_type = mod_type_list[lisnum]
						mod_pos = str(mod_pos)
						pos_and_mod_list.append(mod_pos)
						#pos_and_mod_list.append(',')
						pos_and_mod_list.append(mod_type)
						pos_and_mod_list.append(';')
						lisnum+=1
					#print(pos_and_mod_list)
					pos_and_mod_list_1 = ''.join(pos_and_mod_list)
					charge_state_1 = str(charge_state)
					pep_pos_mod_charge = PeptideSequence+'|'+pos_and_mod_list_1+'|'+charge_state_1
					#print(pos_and_mod_list_1)
					#break;
					store_values.writerow([scanfile,spectrum_title,num,spectrumID,spectrumID1,scan_number,rank,DissociationMethod,experimentalMassToCharge,calculatedMassToCharge,DM,absdM,IsotopeError,charge_state,precursorError,PeptideSequence,Petide_length,Peptide,modifiedpeptide,miss_cleavage,Enery,enzN,enzC,Protein,protein_length,start_position,end_position,pre_position,post_position,isDecoy,MSGF_RawScore,MSGF_DeNovoScore,MSGF_SpecEValue,MSGF_EValue,ExplainedIonCurrentRatio,NTermIonCurrentRatio,CTermIonCurrentRatio,MS2IonCurrent,NumMatchedMainIons,MeanErrorAll,StdevErrorAll,MeanErrorTop7,StdevErrorTop7,MeanRelErrorAll,StdevRelErrorAll,MeanRelErrorTop7,StdevRelErrorTop7,ScoreRatio,MSGF_QValue,pos_and_mod_list_1,pep_pos_mod_charge])
					num+=1
					#scanfile,spectrumID,scan_number,rank,DissociationMethod,experimentalMassToCharge,calculatedMassToCharge,DM,absdM,IsotopeError,charge_state,precursorError,PeptideSequence,Petide_length,Peptide,modifiedpeptide,miss_cleavage,Enery,enzN,enzC,Protein,start_position,end_position,pre_position,post_position,isDecoy,protein_length,MSGF_RawScore,MSGF_DeNovoScore,MSGF_SpecEValue,MSGF_EValue,MSGF_QValue,MSGF_PepQValue,ExplainedIonCurrentRatio,NTermIonCurrentRatio,CTermIonCurrentRatio,MS2IonCurrent,NumMatchedMainIons,MeanErrorAll,StdevErrorAll,MeanErrorTop7,StdevErrorTop7,MeanRelErrorAll,StdevRelErrorAll,MeanRelErrorTop7,StdevRelErrorTop7,ScoreRatio
						#row+=1
					#store_values.writerow([spectrumID,charge_state,experimentalMassToCharge,calculatedMassToCharge,rank,passThreshold,start_position,end_position,pre_position,post_position,isDecoy,protein_length,accession_no,numDatabaseSequences,decoy_DB_accession_regexp,PeptideSequence,MSGF_RawScore,MSGF_DeNovoScore,MSGF_SpecEValue,MSGF_EValue,MSGF_QValue,MSGF_PepQValue,IsotopeError,DissociationMethod,ExplainedIonCurrentRatio,NTermIonCurrentRatio,CTermIonCurrentRatio,MS2IonCurrent,NumMatchedMainIons,MeanErrorAll,StdevErrorAll,MeanErrorTop7,StdevErrorTop7,MeanRelErrorAll,StdevRelErrorAll,MeanRelErrorTop7,StdevRelErrorTop7,PeptideSequence,PeptideSequence,Modificationtype,Modification_location,scan_number,scanfile,Protein,Peptide,modifiedpeptide])
					#row+=1
					
					
				else:
						pass
				line =fh.readline()
				line = line.decode()
				#print(m)
				#store_values.writerow([m])
				#row+=1
				#break;
	else:
		pass

t = timeit.default_timer()
print("end_time_in second=",t)