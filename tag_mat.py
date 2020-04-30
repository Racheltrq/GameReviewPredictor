import csv

with open("steam_games_only.csv", 'r') as infile, open("genre_mat.csv", 'w') as outfile:
	fieldnames = ['Action', 'Adventure', 'Massively Multiplayer', 'Strategy', 'Free to Play', 'RPG', 'Indie', 'Early Access', 'Simulation', 'Racing', 'Casual', 'Sports', 'Valve', 'Animation & Modeling', 'Design & Illustration', 'Utilities', 'Game Development', 'Education', 'Software Training', 'Web Publishing', 'Video Production', 'Audio Production', 'Photo Editing', 'Accounting', 'Movie', 'HTC']
	r = csv.DictReader(infile)
	w = csv.DictWriter(outfile, fieldnames = fieldnames)
	w.writeheader()

	dic = {}
	for row in r:
		for key in fieldnames:
			dic[key] = 0
		for genre in row["genre"].split(","): 
			if genre != '':
				dic[genre] = 1
		#print(dic)
		w.writerow(dic)





