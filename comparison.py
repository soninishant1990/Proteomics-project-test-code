#!/usr/bin/python
import csv
import re
import os
import sys
import shutil


with open('cluster0.csv','r', newline='') as f, open('fdr.csv','r', newline='') as fh, open('cluster0_match_with_fdr_result.csv','w',newline='') as cluster_result, open('cluster0_not_match_with_fdr_result_result.csv','w',newline='') as fdr_result:
	csv_reader = csv.reader(f, delimiter=',')
	csv_reader1 = csv.reader(fh, delimiter=',')
	x = []
	for n in csv_reader1:
		e = n
		for lines in e:
			x.append(lines)
	#print("x",x)
	
	for m in csv_reader:
		d = m
		for line in d:
			if line in x:
				#print("line",line)
				#print("x",x)
				#print("match")
				cluster_result.write(line)
			else:
				#print("not_match")
				fdr_result.write(line)

		


with open('cluster1.csv','r', newline='') as f1, open('fdr.csv','r', newline='') as fh1, open('cluster1_match_with_fdr_result.csv','w',newline='') as cluster_result1, open('cluster1_not_match_with_fdr_result_result.csv','w',newline='') as fdr_result1:
	csv_reader1 = csv.reader(f1, delimiter=',')
	csv_reader11 = csv.reader(fh1, delimiter=',')
	x1 = []
	for n1 in csv_reader11:
		e1 = n1
		for lines1 in e1:
			x1.append(lines1)
	#print("x",x)
	for m1 in csv_reader1:
		d1 = m1
		for line1 in d1:
			if line1 in x1:
				#print("line",line)
				#print("x",x)
				#print("match")
				cluster_result1.write(line1)
			else:
				#print("not_match")
				fdr_result1.write(line1)
	
	
	
	#print("d",line)		
					