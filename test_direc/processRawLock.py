# This program processes & handles the raw lock set data in the google doc
# Internaly, the datasheet has the following:
# row1> col1 - col2 - .... -buffer1- - Overview - -buffer2- - Specificaitons
# row2> col1 ...
# ....
#  Basically the file "raw_lock_sets.txt" has the form where:
#->		'-buffer1-' is just "#####"
#->		 overview part has text data
#->		'-buffer2-' functions as a delimiter having "%%%%%"
#->		and then specifications has more data
#
#  In actuality, the names of those sets are kind of useless.
#  I'm going to consider a device of the form device = (,)


## Code Time
# First, we'll grab the file, parse it and use "#####" as the first delimiter and then %%%%%" as the delimiter
file_name = "raw_lock_sets.txt"
file = open(file_name,"r")
text = file.read()

parse1 = text.split("#####")
parse2 = []

for x in parse1:
	parse2.append( x.split("%%%%%") )
del parse2[0]


isIoTList =  ["wifi","wi-fi","poe","ethernet","internet","iot","wireless"]



def isSmart(devText):
	"""The device has mention of one of the following keywords:
	wifi, wi-fi, poe, ethernet, internet, iot, wireless"""
	report = ""
	test = devText.lower()
	for word in isIoTList:
		report = report+word+":"+ str(word in test) + "\n"
	print(report)

# tesitng
n = 0
while n < len(parse2):
	isSmart(parse2[n][0])
	isSmart(parse2[n][1])
	n+=1

