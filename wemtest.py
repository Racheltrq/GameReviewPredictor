import WordEmb

wem = WordEmb.docFeature("wvmodel.bin")
print("Model Succesfully Loaded.\n")

wem.buildCorpus("intense, of dark; horror fly battle war in magic")
ret = wem.getFeatures()
print(ret)