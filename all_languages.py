import csv

f = open('steam_games_only.csv', 'r')
language = []
with f:
    reader = csv.reader(f)
    for row in reader:
    	temp = row[11].split(",")
    	for i in temp:
    		if i not in language:
    			language.append(i)
print(len(language))
print(language)