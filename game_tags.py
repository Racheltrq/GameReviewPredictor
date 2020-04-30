import csv

with open("steam_games_only.csv", 'r') as infile, open("game_tags.csv", 'w') as outfile:

	r = csv.DictReader(infile)
	w = csv.DictWriter(outfile, fieldnames=["name", "popular_tags"])
	w.writeheader()
	for row in r:
		
		w.writerow({"name": row["name"], "popular_tags": row["popular_tags"]})
