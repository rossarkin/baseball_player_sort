import sys, os, re

#create the lists and dictionaries to store the data
players =[]
hits ={}
bats = {}
averages = {}

#Usage statement if no filename is entered
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])
 
filename = sys.argv[1]

#Error message if the filename is not valid
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])

f = open(filename)

for line in f:
	#matches a regular expression with the data found in the text files
	player_regex = re.compile(r"([\w]+\s[\w]+[^ \t\r\n]*[\w]+)\sbatted\s(\d)\stimes\swith\s(\d)\shits")
	match = player_regex.match(line)
	if match is not None:
		#if the match is valid, get the player's name, at bats, and hits from the file
		player = match.group(1) 
		bat = int(match.group(2))
		hit = int(match.group(3))
		#if the player has already been found add the hits and bats to the existing count
		if player in players:
			hits[player] += hit
			bats[player] += bat
		#if not, add him to the list of players
		else:
			players.append(player)
			hits[player] = hit
			bats[player] = bat

#calculate the batting averages for the players
for player in players:
	averages[player] = float(hits[player])/float(bats[player])

#sort both the names and averages in reverse order of the batting averages
player_sort = sorted(averages, key=averages.__getitem__, reverse=True)
average_sort = sorted(averages.values(), reverse=True)

#rounds the averages to three decimal places and adds a zero to averages that need one
round_sort = []
for avg in average_sort:
	avg = str(round(avg,3))
	if len(avg) < 5:
		avg = avg + "0"
	round_sort.append(avg)

#prints the data
for x in range (0, len(average_sort)):
	print player_sort[x] + ": " + round_sort[x]

f.close()


