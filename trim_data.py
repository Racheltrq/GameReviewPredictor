import csv

with open("steam_games.csv", 'r') as infile, open("steam_games_only.csv", 'w') as outfile:

     r = csv.DictReader(infile)
     w = csv.DictWriter(outfile, r.fieldnames)
     w.writeheader()
     for row in r:
     	if row["types"] == "app":
     		print(row["types"])
     		w.writerow({"url": row["url"], "types": row["types"], "name": row["name"], "desc_snippet": row["desc_snippet"], "recent_reviews": row["recent_reviews"], "all_reviews": row["all_reviews"], "release_date": row["release_date"], "developer": row["developer"], "publisher": row["publisher"], "popular_tags": row["popular_tags"], "game_details": row["game_details"], "languages": row["languages"], "achievements": row["achievements"], "genre": row["genre"], "game_description": row["game_description"], "mature_content": row["mature_content"], "minimum_requirements": row["minimum_requirements"], "recommended_requirements": row["recommended_requirements"], "original_price": row["original_price"], "discount_price": row["discount_price"]})