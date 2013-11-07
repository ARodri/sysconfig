#!/usr/bin/python
import sys
#input_file = "final_out_FORCLOSURE_BELOW_50K_20121001_20130331.psv"

input_file = sys.argv[1]

delim = sys.argv[2]

fin = open(input_file,'r')

lines = fin.readlines()

header = lines[0].strip('\n').split(delim)

labels = {}
cnts = {}

for i in range(0,len(header)):
  field = header[i]
  labels[i] = field
  cnts[i] = 0

total = 0
expected_size = len(header)

for line in lines[1:]:
  parsed = line.strip('\n').split(delim)
  if len(parsed) != expected_size:
    print("Non rectagularity. Expected "+str(expected_size)+", found "+str(len(parsed)))
  else:
    for i in range(0,len(parsed)):
       if parsed[i].strip() != "":
         cnts[i] += 1
    total += 1

for i in labels.keys():
  field = labels[i]
  perc_pop = cnts[i] / float(total)
  
  lbl = ("%s-%s" % (i, field)).ljust(40," ")

  print("%s %s" % (lbl, perc_pop)) 
