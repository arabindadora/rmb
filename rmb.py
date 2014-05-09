#!/usr/bin/env python
import os
count = 0
fname = {}

print "RMB - ReMove Backup: Gedit backup files remover."

for (dirname, dirs, files) in os.walk('/home'):
	for filename in files:
		if filename.endswith('~'):
			count = count + 1
			fname[dirname] = filename		

for dname in fname.keys():
	f =  dname + "/" + fname[dname]
	os.remove(f)
	# print "[+] removed: " +f

if count:
	print "[*]", count, "file(s) removed."
else:
	print "[!] No files found."