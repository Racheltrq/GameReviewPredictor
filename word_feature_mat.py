import WordEmb
import csv

wem = WordEmb.docFeature("wvmodel.bin")
print("Model Succesfully Loaded.\n")

header = ["name", "desc_snippet"]
for i in range(1, 101):
	header.append("wf" + str(i))
#print(header)


with open("desc.csv", 'r') as infile, open("word_feature_mat.csv", 'w') as outfile:
	r = csv.DictReader(infile)
	w = csv.DictWriter(outfile, fieldnames = header)
	w.writeheader()
	#count=1
	for row in r:
		if row["desc_snippet"] != "NaN":
			#print("print input text")
			#print(row["desc_snippet"])
			wem.buildCorpus(row["desc_snippet"])
			ret = wem.getFeatures()
			try:
				type(ret)
				dic = {}
				print(row["name"])
				index = 0
				for i in header:
					dic[i] = ret[index]
					index += 1
				dic["name"] = row["name"]
				dic["desc_snippet"] = row["desc_snippet"]
				w.writerow(dic)
			except:
				pass
			#count += 1
			#print(dic)
	#print(count)
