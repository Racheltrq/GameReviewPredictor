import csv
import copy

with open("y_raw.csv", 'r') as infile, open("Xmat.csv") as infile1, open("XYmat.csv", 'w') as outfile:
	r = csv.DictReader(infile)
	r1 = csv.DictReader(infile1)
	fieldnames = next(r1)
	xrow = copy.deepcopy(fieldnames)
	#print(fieldnames)
	fieldnames.pop("name")
	header = ["name", "reviews"]
	for i in fieldnames:
		header.append(i)
	w = csv.DictWriter(outfile, fieldnames = header)
	w.writeheader()
	i = 0
	for row in r:
		
		if row["reviews"] != "NaN":
			if i != 0:
				xrow = next(r1)
			xrow["reviews"] = row["reviews"]
			w.writerow(xrow)
			i += 1

	

			