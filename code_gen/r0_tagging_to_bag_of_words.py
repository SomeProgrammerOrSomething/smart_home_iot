file = open("word_set_r0.txt","r")
raw_data = file.read()
file.close()

# Parse File ( originally copied-and-pasted-from csv ) to Separate Rows per Newline
data = raw_data.split("\n")

# Each Device is represented as single-column row per above code
# Each entry for said device is a string of keywords delimited by ;
tags = []
for dev in data:
	for tag in dev.split(";"):
		tags.append(tag)

# Now that we have said tags, we want to remove any repeated tags
word_bank = []
for tag in tags:
	if tag in word_bank:
		pass
	else:
		word_bank.append(tag.lower())

# There's a trailing empty string in there, let's get it!
word_bank.remove("")