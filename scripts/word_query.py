import nltk
import re
import numpy as np
import pandas as pd

CHILDES_corpus = pd.read_csv("C:/Users/AzF/unit analysis/childes.csv")
query_list = ["blondie'is"]
utterance = CHILDES_corpus['stem']
utterance = utterance['stem'].astype(str)
utterance_list = []
print(utterance)

# for i in utterance:
#     for j in query_list:
#         if re.search(i,j):
#             #print(i)
            
#             utterance_list.append(i)

#print(utterance_list)    