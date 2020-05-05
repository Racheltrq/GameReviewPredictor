import pandas as pd
import numpy as np
import string
import gensim
# big helper for implementing word2vec features

class docFeature:
    # Attributes #
    numWords = 5
    DEBUG = False

    def __init__(self, modelName="wvmodel.bin", inDoc=None):
        # Load model with name from fs
        self.model = gensim.models.KeyedVectors.load_word2vec_format(modelName, binary=True)

    def buildCorpus(self, inDoc):
        stoplist = set('a an and as are the this that then you your to of is in for by can will could would with has'.split(' '))
        
        doc = inDoc.translate(str.maketrans('', '', string.punctuation))
        self.corpus = [word for word in doc.lower().split() if word not in stoplist]
        
    def getVectors(self):
        wvs = [];
        curWords = 0;
        i = 0;
        while(curWords < self.numWords) and (i < len(self.corpus)):
            cWord = self.corpus[i]
            print(i, ": ", cWord) if self.DEBUG else 0
            try:
                cVec = self.model[cWord]
            except KeyError:
                #print("/!\\ Key Not Found")
                i+=1
                continue
            wvs.append(cVec)
            curWords += 1
            i += 1
        return wvs

    def getFeatures(self):
        wvs = self.getVectors()
        try:
            wvsize = wvs[0].shape

            print(wvs[0].shape) if self.DEBUG else 0
            sumv = np.zeros(wvs[0].shape[0])
            for v in wvs:
                sumv = sumv + v
            fv = sumv / len(wvs)
            print(sumv) if self.DEBUG else 0
            return fv
        except IndexError:
            print("IndexError")
            print("wvs:", wvs)
            return False

