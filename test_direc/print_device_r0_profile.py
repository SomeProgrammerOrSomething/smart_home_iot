# In some cases, a word like "overview" might include the substring "view".
# To handle these, we're just going to consider cases where spaces, commas, periods, and exclamation marks function as delimeters or mark wordboundaries ( lol @ actual, accidental/unplanned, totally serendipitous "wordboundaries" )

def expand(normalWord):
	return [","+normalWord,
	normalWord+",",
	normalWord+".",
	normalWord+"!",
	normalWord ]
	# Deprecation #

	### > setProfile = set(profile.split(" ")
	### We're cutting out these words with spaces because the part where we split the list and then form it into a set gets rid of space as a delimiter
	###" "+normalWord,
	###normalWord+" ",

	# ^ Deprecation #

i = 0
devParam = []

while i < len(devices):
  profile = devices[i]["txtAll"]
  devParam.append ({"strIn":"","valIn":[],"strEx":"","valEx":[]})
  for word in word_bank:
    setProfile = set(profile.split(" "))
    if setProfile.isdisjoint(expand(word)):
      devParam[i]["strEx"] += "{}\n".format(word)
      devParam[i]["valEx"].append(word)
    else:
      devParam[i]["strIn"] += "{}\n".format(word)
      devParam[i]["valIn"].append(word)
  i+= 1