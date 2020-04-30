import csv
#print("hello")
with open("steam_games_only.csv", 'r') as infile, open("recent_reviews.csv", 'w') as outfile:
	#print("hello")
	r = csv.DictReader(infile)
	w = csv.DictWriter(outfile, fieldnames = ["recent_reviews"])
	w.writeheader()
	i = 2
	testing = []
	for row in r:
		
			
		percent_index = row["recent_reviews"].find("%")
		if len(row["recent_reviews"]) > 0 and percent_index > 0:
			#if i == 
			if row["recent_reviews"][percent_index - 1].isdigit() and row["recent_reviews"][percent_index - 2].isdigit() and row["recent_reviews"][percent_index - 3].isdigit():
				#print(row["all_reviews"][percent_index - 2: percent_index])
				w.writerow({"recent_reviews": row["recent_reviews"][percent_index - 3: percent_index]})
				#print(i, row["all_reviews"][percent_index - 3: percent_index])
				i += 1
			else:
				if row["recent_reviews"][percent_index - 1].isdigit() and row["recent_reviews"][percent_index - 2].isdigit():
					w.writerow({"recent_reviews": row["recent_reviews"][percent_index - 2: percent_index]})
					i += 1
				else: 
					w.writerow({"recent_reviews": row["recent_reviews"][percent_index - 1]})
					i += 1
		else:
			if i == 55:
				print(row)
			w.writerow({"recent_reviews":"NaN"})
			#print(i)
			testing.append(i)
			i += 1
		
	#print(testing)