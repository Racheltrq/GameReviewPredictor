import csv
import copy

with open("y_raw.csv", 'r') as infile, open("Xmat_lang.csv") as infile1, open("desc.csv") as infile2, open("XYmat_lang_desc.csv", 'w') as outfile:
	y_raw = csv.DictReader(infile)
	Xmat = csv.DictReader(infile1)
	desc_mat = csv.DictReader(infile2)
	fieldnames = next(Xmat)
	xrow = copy.deepcopy(fieldnames)
	#print(fieldnames)
	fieldnames.pop("name")
	header = ["name", "reviews", "desc_snippet"]
	for i in fieldnames:
		header.append(i)
	w = csv.DictWriter(outfile, fieldnames = header)
	w.writeheader()
	i = 0
	desc_row = next(desc_mat)

	for row in y_raw:
		
		if row["reviews"] != "NaN" and len(desc_row["desc_snippet"]) > 0:
			if i != 0:
				xrow = next(Xmat)
			xrow["reviews"] = row["reviews"]
			xrow["desc_snippet"] = desc_row["desc_snippet"]
			desc_row = next(desc_mat)
			w.writerow(xrow)
			i += 1
