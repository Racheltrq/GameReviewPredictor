import csv

f1 = open('steam_games_only.csv', 'r')
#f2 = open('game_tags.csv', 'rw')

prices = []
with f1:
	reader = csv.reader(f1)
	for row in reader: 
		if row[18] != "original_price":
			if len(row[18]) == 0 or row[18][0] != "$":
				prices.append("0")
			else:
				prices.append(row[18][1:])
		

prices.insert(0, "prices")
with open('prices.csv', 'w') as f2:

	writer = csv.DictWriter(f2, fieldnames = ["prices"])
	#writer.writeheader()

	for i in prices:
		writer.writerow({"prices": i})
