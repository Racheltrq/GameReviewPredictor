import csv

with open("steam_games_only.csv", 'r') as infile, open("desc.csv", 'w') as outfile:
	r = csv.DictReader(infile)
	w = csv.DictWriter(outfile, fieldnames = ["name", "desc_snippet"])
	w.writeheader()
	for row in r:
		w.writerow({"name": row["name"], "desc_snippet": row["desc_snippet"]})
		#if row["name"] == "DOOM":
			#print({"name": row["name"], "desc_snippet": row["desc_snippet"]})


		
