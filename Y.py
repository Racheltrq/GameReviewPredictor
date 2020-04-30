import csv

with open("y_raw.csv", 'r') as infile, open("Xmat.csv") as infile1, open("XYmat.csv", 'w') as outfile:
	r = csv.DictReader(infile)
	r1 = csv.DictReader(infile1)
	fieldnames = next(r1)
	fieldnames["reviews"] = 0
	print(len(fieldnames))
	w = csv.DictWriter(outfile, fieldnames = fieldnames)
	w.writeheader()

	for row in r:
		
		if row["reviews"] != "NaN":
			xrow = next(r1)
			xrow["reviews"] = row["reviews"]
			w.writerow(xrow)


	

			