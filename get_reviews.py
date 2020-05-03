import csv
#print("hello")
with open("steam_games_only.csv", 'r') as infile, open("all_reviews.csv", 'w') as outfile:
	#print("hello")
	r = csv.DictReader(infile)
	w = csv.DictWriter(outfile, fieldnames = ["all_reviews"])
	w.writeheader()
	i = 2
	testing = []
	for row in r:
		
			
		percent_index = row["all_reviews"].find("%")
		if len(row["all_reviews"]) > 0 and percent_index > 0:
			parL = row["all_reviews"].find("(")
			parR = row["all_reviews"].find(")")
			num = (row["all_reviews"][parL+1:parR])
			while "," in num:
				com = num.find(",")
				num = num[:com] + num[com+1:]


			if int(num) < 30:
				w.writerow({"all_reviews":"NaN"})
				testing.append(i)
			else:
				if row["all_reviews"][percent_index - 1].isdigit() and row["all_reviews"][percent_index - 2].isdigit() and row["all_reviews"][percent_index - 3].isdigit():
					#print(row["all_reviews"][percent_index - 2: percent_index])
					w.writerow({"all_reviews": row["all_reviews"][percent_index - 3: percent_index]})
					#print(i, row["all_reviews"][percent_index - 3: percent_index])
					i += 1
				else:
					if row["all_reviews"][percent_index - 1].isdigit() and row["all_reviews"][percent_index - 2].isdigit():
						w.writerow({"all_reviews": row["all_reviews"][percent_index - 2: percent_index]})
						i += 1
					else: 
						w.writerow({"all_reviews": row["all_reviews"][percent_index - 1]})
						i += 1
		else:

			w.writerow({"all_reviews":"NaN"})
			#print(i)
			testing.append(i)
			i += 1
		
	#print(testing)