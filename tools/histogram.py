#!/usr/bin/python

import sys
from decimal import *
from optparse import OptionParser

USAGE = "usage: %prog [options]"

oParser = OptionParser(usage=USAGE)

#oParser.add_option("-i", "--inputFile", default="-", help="input file. [default: stdin]")
#oParser.add_option("-d", "--inputDelim", default="|", help="input delimiter. [default: %default ]")
#oParser.add_option("-h", "--header", action="store_true", dest="hasHeader", default=False, help="has header. [default: %default]")
oParser.add_option("-n", "--numeric", action="store_true", dest="isNumeric", default=False, help="treat input as numeric. [default: %default]")
oParser.add_option("-f", "--sortByBin", action="store_true", dest="sortByBin", default=False, help="sort by bin. [default: %default]")
oParser.add_option("-p", "--prettyPrint", action="store_true", dest="prettyPrint", default=False, help="pretty print. [default: %default]")
oParser.add_option("-d", "--delim", default="\t", dest="delimiter", help="output delimiter: [Default: tab]")
oParser.add_option("-b", "--bin", default="1", dest="bin", help="bin numeric values by X: [Default: %default]")

(options,args) = oParser.parse_args()

nBin = Decimal(options.bin)

data = {}

for line in sys.stdin:
	val = line.strip('\n').strip('\r')
	if (options.isNumeric):
		nVal = (Decimal(val) - (Decimal(val) % nBin))
		data[nVal] = data.get(nVal,0) + 1
	else:
		data[val] = data.get(val,0) + 1

total = Decimal(sum(data.values()))

sortedData = None
sortFunction = None

if options.sortByBin:
	if (options.numeric):
		sortFunction = lambda tup: float(tup[0])
	else:
		sortFunction = lambda tup: tup[0]
else:
	sortfunction = lambda tup: tup[1]

sortedData = sorted(data.items(), key=sortFunction)

maxValLen = max(map(lambda tup: len(str(tup[0])), sortedData))
maxFreqLen = max(map(lambda tup: len(str(tup[1])), sortedData))

del(data)

header = ["BIN", "FREQUENCY", "BIN %", "CUME", "1-CUME"]
if (options.prettyPrint):
	header = ["BIN".rjust(maxValLen, ' '), "FREQUENCY".rjust(maxFreqLen, ' '), "BIN %", "CUME", "1-CUME"]

print(options.delimiter.join(header))
cumeSeen = 0
for (val,freq) in sortedData:
	cumeSeen += freq
	binPerc = (Decimal(freq) / total).quantize(Decimal('0.0000'))
	cumePerc = (Decimal(cumeSeen) / total).quantize(Decimal('0.0000'))
	m1CumePerc = 1-cumePerc
	if (options.prettyPrint):
		val = str(val).rjust(len(header[0]), ' ')
		freq = str(freq).rjust(len(header[1]), ' ')
		binPerc = str(binPerc).rjust(max(len(header[2]), len(str(binPerc))), ' ')
		cumePerc = str(cumePerc).rjust(max(len(header[3]), len(str(cumePerc))), ' ')
		m1CumePerc = str(m1CumePerc).rjust(max(len(header[4]), len(str(m1CumePerc))), ' ')
	
	print(options.delimiter.join([str(val),str(freq), str(binPerc),str(cumePerc),str(m1CumePerc)]))
print "Total: "+str(total)







# Read parameters
#inputFile = sys.argv[1]
#delim = sys.argv[2]
#outputFile = sys.argv[3]
#keyFields = sys.argv[4]
#outputKeyFieldName = sys.argv[5]

# Open file handlers
#  Handle - for sys.stdout/stdin
#fin = None
#if (inputFile == '-'):
#	fin = sys.stdin
#else:
#	fin = open(inputFile,'r')
#
#fout = None
#if outputFile == '-':
#	fout = sys.stdout
#else:
#	fout = open(outputFile,'w')

# Construct readers and writers
#headerStr = fin.readline()
#(headerList, parser) = data_util.makeParser(headerStr,delim)
#headerList = ['id'] + headerList
#writer = data_util.makeWriter(headerList, delim)


# Do the work
#i = 0
#fout.write(delim.join(headerList) + "\n")
#for line in fin:
#	(parsed, hadError, error) = parser(line)
#	parsed["id"] = i
#	i += 1
#	fout.write(writer(parsed))

# Close files
#fin.close()
#fout.close()
