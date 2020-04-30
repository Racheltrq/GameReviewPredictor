import csv

f = open('steam_games_only.csv', 'r')
genre = []
with f:
    reader = csv.reader(f)
    for row in reader:
    	temp = row[13].split(",")
    	for i in temp:
    		if i not in genre:
    			genre.append(i)
print(len(genre))
print(genre)