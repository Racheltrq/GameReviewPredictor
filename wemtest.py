import WordEmb

wem = WordEmb.docFeature("wvmodel.bin")
print("Model Succesfully Loaded.\n")

wem.buildCorpus("PLAYERUNKNOWN'S BATTLEGROUNDS is a battle royale shooter that pits 100 players against each other in a struggle for survival. Gather supplies and outwit your opponents to become the last person standing.")
ret = wem.getFeatures()
print(type(ret))