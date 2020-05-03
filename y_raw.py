import csv

with open("recent_and_all_reviews.csv", 'r') as infile, open("y_raw.csv", 'w') as outfile:
	r = csv.DictReader(infile)
	w = csv.DictWriter(outfile, fieldnames = ["reviews"])
	w.writeheader()
	for row in r:
		if row["all_reviews"] == "NaN":
			w.writerow({"reviews": row["recent_reviews"]})
			print(row["recent_reviews"])
		else:
			w.writerow({"reviews": row["all_reviews"]})
			print(row["all_reviews"])
