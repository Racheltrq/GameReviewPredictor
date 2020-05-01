import csv

with open("steam_games_only.csv", 'r') as infile, open("lang_mat.csv", 'w') as outfile:
	fieldnames = ['English', 'French', 'Italian', 'German', 'Spanish - Spain', 'Japanese', 'Polish', 'Portuguese - Brazil', 'Russian', 'Traditional Chinese', 'Korean', 'Simplified Chinese', 'Arabic', 'Portuguese', 'Turkish', 'Thai', 'Ukrainian', 'Czech', 'Spanish - Latin America', 'Dutch', 'Hungarian', 'Danish', 'Finnish', 'Norwegian', 'Swedish', 'Greek', 'Bulgarian', 'Romanian', '', 'Vietnamese', 'Slovakian']
	r = csv.DictReader(infile)
	w = csv.DictWriter(outfile, fieldnames = fieldnames)
	w.writeheader()

	dic = {}
	for row in r:
		for key in fieldnames:
			dic[key] = 0
		for lang in row["languages"].split(","): 
			if lang != '':
				dic[lang] = 1
		#print(dic)
		w.writerow(dic)